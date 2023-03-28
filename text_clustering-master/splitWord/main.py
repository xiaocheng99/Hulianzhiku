# encoding=utf-8
import paddle
import jieba
from connector import Data
import csv
import time

import xlsxwriter as xw

paddle.enable_static()
jieba.enable_paddle()


# 传入sql语句获取数据库数据
def get_data(sql):
    res = Data.get_call_content(sql)
    print(len(res))
    return res


if __name__ == '__main__':
    start = time.time()
    # 返回数据分别为 call_content undertaking_department
    nameSpace = ['桂溪街道']
    with open('./raw_data_txt/桂溪街道.txt', 'w', encoding='utf-8') as f:
        for name in nameSpace:
            # 记得注意看空格！！！
            sql = "SELECT `call_content`,`undertaking_department` FROM `work_order` where `undertaking_department` LIKE '%" + name + "%'"
            res = get_data(sql)
            res = str(res)
            f.write(res)
    end = time.time()
    print('程序运行时间:' + str(end - start) + 's')


