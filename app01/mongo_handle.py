from pymongo import MongoClient

def db_conn():
    client = MongoClient(host='192.168.225.128', port=27017)
    return client

def kitchenDB():
    conn = db_conn()
    return conn.kitchenDB