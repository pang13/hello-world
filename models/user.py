from models import Model
from utils import log

class User(Model):
    """
    User 是一个保存用户数据的 model
    现在只有两个属性 username 和 password
    """
    def __init__(self, form):
        self.uid = form.get('uid', None)
        self.name = form.get('name', '')
        self.password = form.get('password', '')

    def salted_password(self, password, salt='$!@><?>HUI&DWQa`'):
        import hashlib
        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()

        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2

    def hashed_password(self, pwd):
        import hashlib
        # 用 ascii 编码转换成 bytes 对象
        p = pwd.encode('ascii')
        s = hashlib.sha256(p)
        # 返回摘要字符串
        return s.hexdigest()

    @classmethod
    def validate_login(cls, form):
        u = User(form)
        dic = {
            "uid":form.get("uid",""),
        }
        user = User.find(dic)
        if user is not None and user[0]["password"] == u.password: #u.hashed_password(u.password):
            return u
        else:
            return None
