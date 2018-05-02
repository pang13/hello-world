import pymongo


# 连接 mongo 数据库, 主机是本机, 端口是默认的端口
client = pymongo.MongoClient("mongodb://localhost:27017")

# 设置要使用的数据库
mongodb_name = 'StudentMessage'
# 直接这样就使用数据库了，相当于一个字典
db = client[mongodb_name]

def db_insert(form):
    return db.user.insert(form)


#返回数据列表
def db_query(form=None):
    fild={
        '_id':0,
    }
    return list(db.user.find(form,fild))


#删除数据，只删一个
def db_remove(form):
    return db.user.remove(form,1)
