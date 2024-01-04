import configparser
from tqdm import tqdm
from sqlalchemy import create_engine, insert, text
from sqlalchemy.orm import Session


class SqlOperate:
    def __init__(self):
        # 讀取設定檔
        config = configparser.ConfigParser()
        config.read('/home/cheng1103/workspace/ETL/config.ini')

        # PG_SQL
        pg_user = config.get('postgresql', 'user')
        pg_key = config.get('postgresql', 'password')
        pg_host = config.get('postgresql', 'host')
        pg_port = config.get('postgresql', 'port')
        pg_db = config.get('postgresql', 'database')

        # 資料庫路徑
        DATABASE_URL = f"postgresql://{pg_user}:{pg_key}@{pg_host}:{pg_port}/{pg_db}"
        self.pg_sql_engine = create_engine(DATABASE_URL)  # 使用create_engine建立連線

    # 查詢資料
    def pg_query(self, query):
        with Session(self.pg_sql_engine) as session:
            query_result = session.execute(text(query))
            query_result = query_result.fetchall()

        return query_result

    # 分割資料
    def __split_data(self, data, batch_size):
        batches = []
        for idx in range(0, len(data), batch_size):
            batch = data[idx: idx + batch_size]
            batches.append(batch)
        return batches

    # 新增資料
    def pg_insert(self, table, data, batch_size=10000):
        with Session(self.pg_sql_engine) as session:
            for batch_data in tqdm(self.__split_data(data, batch_size), desc='資料寫入進度'):

                try:
                    insert_result = session.execute(insert(table), batch_data)
                    session.commit()

                except Exception as e:
                    print(e)
