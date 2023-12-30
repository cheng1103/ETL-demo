import os
'''
依據現有的資料表，生成資料模型

輸入：表格名稱、存放路徑、檔案名稱
輸出：資料模型

'''


def generate_model(table_name, path, file_name):

    command = f'sqlacodegen postgresql://postgres:Kinmen82@localhost:5432/practice --table {table_name} --outfile={path}/{file_name}.py'
    os.system(command)


if __name__ == '__main__':
    table_name = input("請輸入表格名稱：")
    path = input("請輸入存放位置：")
    file_name = input("請輸入檔案名稱：")
    generate_model(table_name, path, file_name)
