from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
)
from utils import log
from models.user import User

main = Blueprint('index',__name__)

def current_users():
    # 从 session 中找到 user_id 字段, 找不到就 -1
    # 然后 User.find_by 来用 id 找用户
    # 找不到就返回 None
    uid = session.get('user_id',-1)
    log(uid)
    u = User.find({"uid":uid})
    if u:
        log(User(u[0]).name)
        return User(u[0])
    return None

"""
用户在这里可以
    访问首页(会被设置 cookie)
    注册
    登录
用户登录后, 会写入 session, 并且定向到 /profile
"""
@main.route('/')
def index():
    u = current_users()
    template = render_template('index.html',user=u)
    # 如果要写入 cookie, 必须使用 make_response 函数
    # 然后再用 set_cookie 来设置 cookie
    r = make_response(template)
    r.set_cookie('cookie_name', 'GUA')
    return r
    #todo 设置cookie


@main.route('/login',methods=['post'])
def login():
    form = request.form
    log("form",form)
    u = User.validate_login(form)
    log('user',u)
    if u is None:
        return redirect(url_for('.index'))
    session['user_id']=u.uid
    return redirect(url_for('.profile'))



@main.route('/profile')
def profile():
    u = current_users()
    if u is None:
        return redirect(url_for('.index'))
    r = render_template('user_profile.html',user=u)
    return r


