import MySQLdb
from dbutils.pooled_db import PooledDB
from settings import dev

config = {
    'creator': MySQLdb,
    'host': '127.0.0.1',
    'port': 3306,
    'user':'meiduo',
    'password': 'meiduo',
    'db': 'meiduo_mall',
    'charset': 'utf8mb4',
    'maxconnections': 20,  # 连接池最大连接数量
}

mysqlpool = PooledDB(**config)