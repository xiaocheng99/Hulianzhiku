from pprint import pprint
from paddlenlp import Taskflow
from connector import Data
import time
import xlsxwriter as xw


# 传入sql语句获取数据库数据
def get_data(sql):
    res = Data.get_call_content(sql)
    print(len(res))
    return res

# 数据分词 并存入excel文件
def excute_data(res, worksheet):
    maxLenAddress = ''
    address = ''
    worksheet.activate()  # 激活表
    title = ['call_content', 'address', 'maxLenaddress']  # 设置表头
    worksheet.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for resItem in res:
        resItem = str(resItem)
        keyword = ie(resItem)
        pprint(keyword)
        for item in schema:
            try:
                keywordAddress = keyword[0][item][0]['text']
            except KeyError:
                keywordAddress = 'N'
            address = address + ' / ' + keywordAddress
            if len(maxLenAddress) < len(keywordAddress):
                maxLenAddress = keywordAddress
        insertData = [resItem, address, maxLenAddress]
        address = ''
        maxLenAddress = ''
        row = 'A' + str(i)
        worksheet.write_row(row, insertData)
        i += 1
    print(i)


if __name__ == '__main__':
    start = time.time()

    schema = ['位置', '详细位置', '地址', '机构', '商场', '道路', '地区', '公司', '被诉主体']  # Define the schema for entity extraction
    ie = Taskflow('information_extraction', schema=schema)


    # 返回数据分别为 call_content undertaking_department
    nameSpace = ['高新区法院']
    for name in nameSpace:
        workbook = xw.Workbook('被诉主体地址_full.xlsx')  # 创建工作簿 传入文件地址
        worksheet = workbook.add_worksheet(name)  # 创建子表
        # 记得注意看空格！！！
        sql = "SELECT `call_content` FROM `work_order` where `undertaking_department` LIKE '%" + name + "%'"
        res = get_data(sql)
        excute_data(res, worksheet)
        workbook.close()  # 关闭表
    end = time.time()
    print('程序运行时间:' + str(end - start) + 's')