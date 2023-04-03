#encoding=utf-8
from __future__ import print_function, unicode_literals
import jieba
import xlsxwriter as xw
from get_accused_subject.connector import Data

jieba.load_userdict("58q.txt")
import jieba.posseg as pseg

def get_data(sql):
    res = Data.get_call_content(sql)
    print(len(res))
    return res

def get_accused():
    workbook = xw.Workbook('被诉主体地址_full.xlsx')  # 创建工作簿 传入文件地址
    worksheet = workbook.add_worksheet('name')  # 创建子表
    title = ['call_content', 'multi_subject', 'accused_subject']  # 设置表头
    worksheet.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据

    test_sents = get_data("SELECT `call_content`,`undertaking_department` FROM `work_order` WHERE undertaking_department = '高新区-滴滴'")
    # test_sents=["情况：来话人2月21日和2月22日均在天府大道中段1366号2栋11称19号虎魄网络科技有限公司购买了商家年票，消费金额198元。市民反映商家要求需验证后才能使用消费，但平台却一直不发送验证信息，导致市民无法消费。"]
    for test_sent in test_sents:
        print(test_sent[0])
        result = pseg.cut(test_sent[0])
        accused_lists = []
        for w in result:
            if w.flag == 'nt':
                accused_lists.append(w.word)
                print(w.word, "/", w.flag, ", ", end=' ')
        print("\n" + "=" * 40)
        # 如果accused_lists中有数据 就将数据存入数据库中 如果没有 就将数据用主题词提取实体
        if len(accused_lists) != 0 :
            accused_str = ''
            for accused_item in accused_lists:
                accused_str += '/' + accused_item
            insertData = [test_sent, accused_str]
            row = 'A' + str(i)
            worksheet.write_row(row, insertData)
            i += 1
get_accused()
