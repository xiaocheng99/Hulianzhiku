# encoding=utf-8
import paddle
import jieba
from hulianzhiku import Data
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


# 数据分词 并存入excel文件
def excute_data(res):
    workbook = xw.Workbook('D://home//cut_all.xlsx')  # 创建工作簿 传入文件地址
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['department', 'origin_content', 'fenci_content']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for re in res:
        seg_list = jieba.cut(re[0], cut_all=True)  # 切换模式
        seg_str = '/'.join(list(seg_list))
        print(seg_str)
        insertData = [re[1], re[0], seg_str]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
        print(i)
    workbook.close()  # 关闭表


if __name__ == '__main__':
    start = time.time()
    # 返回数据分别为 call_content undertaking_department
    sql = "SELECT `call_content`,`undertaking_department` FROM `work_order` "
    res = get_data(sql)
    excute_data(res)
    end = time.time()
    print('程序运行时间:' + str(end - start) + 's')
