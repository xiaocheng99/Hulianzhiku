import openpyxl
import pandas as pd
from openpyxl import load_workbook


class ReadFenci:
    def __int__(self):
        pass

    def get_fenci_list(fileName, departName, sheet):
        wb = load_workbook(fileName)
        ws = wb[sheet]
        result_str = ''
        result_list = []
        for row in ws.rows:  # 获取每一行的数据
            count = 0
            for data in row:  # 获取每一行中单元格的数据
                if count == 0:
                    if data.value != departName:
                        continue
                    else:
                        # print(data.value)
                        pass
                if count == 2:
                    result_str += '/' + data.value
                    # print(data.value)
                count += 1
        result_list = result_str.split('/')
        # print(result_list)
        return result_list
