import os
import configparser

'''
依據現有的資料表，生成資料模型
需使用Command Line 執行此程式，指令為：python3 sqlmodelgen.py 

輸入：表格名稱、存放路徑、檔案名稱
輸出：資料模型

'''


def generate_model(table_name, path, file_name):

    # 讀取設定檔
    config = configparser.ConfigParser()
    config.read('/home/cheng1103/workspace/ETL/config.ini')
    user = config.get('postgresql', 'user')
    key = config.get('postgresql', 'password')
    host = config.get('postgresql', 'host')
    port = config.get('postgresql', 'port')
    db = config.get('postgresql', 'database')

    # 建構指令
    command = f'sqlacodegen postgresql://{user}:{key}@{host}:{port}/{db} --table {table_name} --outfile={path}/{file_name}.py'

    # 執行指令
    os.system(command)


if __name__ == '__main__':

    print('您正在執行：SQL模型生成程式')

    table_name = input("請輸入表格名稱：")
    path = input("請輸入存放位置：")
    file_name = input("請輸入檔案名稱：")

    generate_model(table_name, path, file_name)
