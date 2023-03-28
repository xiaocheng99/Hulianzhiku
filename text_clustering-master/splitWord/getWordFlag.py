# encoding=utf-8
import paddle
import jieba
import jieba.posseg as pseg
from connector import Data
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
def excute_data(res, workbook, worksheetName):
    worksheet = workbook.add_worksheet(worksheetName)  # 创建子表
    worksheet.activate()  # 激活表
    title = ['word', 'flag']  # 设置表头
    worksheet.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for re in res:
        re = str(re)
        words = pseg.cut(re, use_paddle=True)  # paddle模式
        print('============================================================')
        for word, flag in words:
            print("{}---{}".format(word, flag))
            insertData = [word, flag]
            row = 'A' + str(i)
            worksheet.write_row(row, insertData)
            i += 1
            print(i)


if __name__ == '__main__':
    start = time.time()
    # 返回数据分别为 call_content undertaking_department
    nameSpace = ['建设', '健康', '保障']
    workbook = xw.Workbook('./getWordFlag.xlsx')  # 创建工作簿 传入文件地址
    for name in nameSpace:
        # 记得注意看空格！！！
        sql = "SELECT `call_content` FROM `work_order` where `undertaking_department` LIKE '%" + name + "%'"
        res = get_data(sql)
        excute_data(res, workbook, name)
    workbook.close()  # 关闭表
    end = time.time()
    print('程序运行时间:' + str(end - start) + 's')


