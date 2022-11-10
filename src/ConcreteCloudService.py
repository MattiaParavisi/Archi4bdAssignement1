from AbstractCloudService import AbstractCloudService
from QueryBuilder import QueryBuilder
from sqlalchemy import create_engine

class ConcreteCloudService(AbstractCloudService):
    def connect(self, connString):
        self.conn = create_engine(connString)
    
    def read_data(self, table, timestamp):
        qb = QueryBuilder()
        qb.columns(['*'])
        qb.from_table(table)
        if timestamp != "":
            qb.where(timestamp)
        return self.conn.execute(qb.build_select())