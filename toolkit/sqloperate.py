# 後續修改為非同步
# 延伸為新增或修改 upsert

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

    # API 查詢資料
        '''
        防止API利用SQL注入
        
        輸入：SQL語法、查詢參數
        輸出：返回查詢資料
        '''

    def pg_api_query(self, syntax, syntax_params_dict):
        with Session(self.pg_sql_engine) as session:
            query_result = session.execute(text(syntax), syntax_params_dict)
            query_result = query_result.fetchall()

        return query_result

    # 查詢資料
    def pg_query(self, syntax):
        with Session(self.pg_sql_engine) as session:
            query_result = session.execute(text(syntax))
            query_result = query_result.fetchall()

        return query_result

    # 新增資料
    def pg_insert(self, table, data, batch_size=10000):
        batches = []
        for idx in range(0, len(data), batch_size):
            batch = data[idx: idx + batch_size]
            batches.append(batch)

        with Session(self.pg_sql_engine) as session:
            for batch_data in tqdm(batches, desc='資料寫入進度'):

                try:
                    insert_result = session.execute(insert(table), batch_data)
                    session.commit()

                except Exception as e:
                    print(e)
