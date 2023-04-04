# encoding=utf-8
from __future__ import print_function, unicode_literals
import jieba
import pymysql
import xlsxwriter as xw

from get_accused_subject.connector import Data

import jieba.posseg as pseg


# 数据库连接
def cnn():
    cnn = pymysql.connect(host='127.0.0.1',  # IP
                          user='root',  # 用户名
                          password='19991019',  # 密码
                          port=3306,  # 端口号
                          database='gxsys')  # 注意是utf8不是utf-8

    return cnn


def get_data(sql):
    res = Data.get_call_content(sql)
    print(len(res))
    return res


def get_accused(cnn):
    jieba.load_userdict("./dict/accused_similair_tittle_nt.txt")
    is_use_min = 0
    workbook = xw.Workbook('被诉主体地址_full.xlsx')  # 创建工作簿 传入文件地址
    worksheet = workbook.add_worksheet('name')  # 创建子表
    title = ['call_content', 'multi_subject', 'accused_subject']  # 设置表头
    worksheet.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    test_sents = get_data(
        "SELECT `call_content`,`undertaking_department` FROM `work_order` WHERE undertaking_department = '高新区-滴滴'")
    # test_sents=["情况：来话人2月21日和2月22日均在天府大道中段1366号2栋11称19号虎魄网络科技有限公司购买了商家年票，消费金额198元。市民反映商家要求需验证后才能使用消费，但平台却一直不发送验证信息，导致市民无法消费。"]
    for test_sent in test_sents:
        is_use_min = 0
        print(test_sent[0])
        result = pseg.cut(test_sent[0])
        accused_lists = []
        for w in result:
            if w.flag == 'nt':
                accused_lists.append(w.word)
                print(w.word, "/", w.flag, ", ", end=' ')
        # 如果accused_lists中有数据 就将数据存入数据库中 如果没有 就将数据用min_len_title提取实体
        if len(accused_lists) == 0:
            print("换到min_len_title_nt")
            jieba.load_userdict("./dict/min_len_title_nt.txt")
            is_use_min = 1
            result = pseg.cut(test_sent[0])
            for w in result:
                if w.flag == 'nt':
                    accused_lists.append(w.word)
                    print(w.word, "/", w.flag, ", ", end=' ')
        if is_use_min == 1:
            print("换到accused_similair_tittle_nt")
            jieba.load_userdict("./dict/accused_similair_tittle_nt.txt")
        if len(accused_lists) != 0:
            # multi_subject 写入
            multi_subject_str = ''
            for accused_item in accused_lists:
                multi_subject_str += '/' + accused_item

            # accused_subject 写入
            accused_subject_str = ''
            company_names = get_company_name(accused_lists, cnn)
            if len(company_names) == 0:
                company_names = get_company_name_min(accused_lists, cnn)
            for company_name in company_names:
                accused_subject_str += '/' + company_name

            insertData = [test_sent[0], multi_subject_str, accused_subject_str]
            row = 'A' + str(i)
            worksheet.write_row(row, insertData)
            i += 1
        else:
            insertData = [test_sent[0], 'NULL', 'NULL']
            row = 'A' + str(i)
            worksheet.write_row(row, insertData)
            i += 1
        print(i)
        print("\n" + "=" * 40, is_use_min)
    workbook.close()  # 关闭表


def get_company_name(accused_lists, cnn):
    # 使用cursor()方法获取操作游标
    cursor = cnn.cursor()
    company_names = []
    for accused_item in accused_lists:
        # 使用execute方法执行SQL语句
        sql = "SELECT company_name FROM accused_subject WHERE similar_title = '" + str(accused_item) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            continue
        result = result[0]
        # 判断当前数组中是否含有这个主体了 如果含有则不添加
        is_same = 0
        for company_name in company_names:
            if str(company_name) == str(result):
                is_same = 1
        if is_same == 0:
            company_names.append(result)

    return company_names


def get_company_name_min(accused_lists, cnn):
    # 使用cursor()方法获取操作游标
    cursor = cnn.cursor()
    company_names = []
    for accused_item in accused_lists:
        # 使用execute方法执行SQL语句
        sql = "SELECT company_name FROM min_title WHERE min_len_title = '" + str(accused_item) + "'"
        cursor.execute(sql)
        result = cursor.fetchone()
        print("---------------result------------", result)
        if result is None:
            continue
        result = result[0]
        # 判断当前数组中是否含有这个主体了 如果含有则不添加
        is_same = 0
        for company_name in company_names:
            if str(company_name) == str(result):
                is_same = 1
        if is_same == 0:
            company_names.append(result)

    return company_names


if __name__ == "__main__":
    cnn = cnn()
    accused_lists = ['滴滴', '滴滴', '滴滴平台']
    get_accused(cnn)
    cnn.close()
