from data import db
from utils import log

# Model 是一个 ORM（object relation mapper）
# 好处就是不需要关心存储数据的细节，直接使用即可
class Model(object):
    @classmethod
    def save(cls,form):
        db.db_insert(form)

    @classmethod
    def delete(cls,form):
        db.db_remove(form)

    @classmethod
    def find(cls,form):
        """
        返回所需查找的
        :param form: 字典，如空返回全部
        :return: 
        """
        return db.db_query(form)
