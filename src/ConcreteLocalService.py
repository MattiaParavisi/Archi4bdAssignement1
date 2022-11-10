from AbstractLocalService import AbstractLocalService
from sqlalchemy import create_engine
from QueryBuilder import QueryBuilder

class ConcreteLocalService(AbstractLocalService):

    def connect(self, connString):
        self.conn = create_engine(connString)
    
    def read_data(self, table, timestamp):
        qb = QueryBuilder()
        qb.columns(['*'])
        qb.from_table(table)
        if timestamp != "":
            qb.where(timestamp)
        return self.conn.execute(qb.build_select())

    def write_data(self, table, data):
        qb = QueryBuilder()
        qb.from_table(table)
        qb.value(data)
        self.conn.execute(qb.build_insert())