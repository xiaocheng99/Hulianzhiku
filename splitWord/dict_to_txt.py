import numpy as np
from openpyxl import load_workbook


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


data = np.load('./split_data/桂溪街道.npy', allow_pickle=True).item()
file = open('dict.txt', 'w')
for k, v in data.items():
    file.write(str(k) + ' ' + str(v) + '\n')
file.close()
print(data)
