from collections import Counter
from read_fenci import ReadFenci
import numpy as np
import time


def excute_counter(fileName, departName, sheet):
    print('开始获取分词数据中.........')
    fenci_list = ReadFenci.get_fenci_list(fileName, departName, sheet)

    print('开始获取停顿词中.........')
    orig_path = './stopwords-master/cn_stopwords.txt'
    f = open(orig_path, encoding='utf8')
    lines = f.readlines()
    list_stop_words = []
    for line in lines:
        list_stop_words.append(line.strip('\n'))
    f.close()

    print('开始去除停顿词中.........')
    for list_stop_word in list_stop_words:
        for fenci in fenci_list:
            if fenci == list_stop_word:
                try:
                    # print('正在删除：' + list_stop_word)
                    fenci_list.pop(fenci_list.index(fenci))
                except Exception as e:
                    print(e)

    # print(fenci_list)
    counter_list = Counter(fenci_list)
    counter_list_dict = dict(counter_list.most_common(len(counter_list) - 1))
    print(counter_list_dict)
    return counter_list_dict


if __name__ == "__main__":
    start = time.time()
    fileName = r'D:\home\基于jieba的paddle分词模式全量数据.xlsx'
    departNames = ['桂溪街道', '市场监督管理局', '公园城市建设局', '中和街道', '石羊街道', '生态环境和城市管理局', '高新区市场监督管理局', '教育文化和卫生健康局'
        , '高新区公园城市建设局'
        , '公安局'
        , '西园街道'
        , '高新区教育文化和卫生健康局'

                   ]
    sheet = 'sheet1'
    for departName in departNames:
        try:
            print('开始提取部门：' + departName)
            res_counter = excute_counter(fileName, departName, sheet)
            np.save(str('./split_data/' + departName) + '.npy', res_counter)
        except Exception as e:
            print(e)
    end = time.time()
    print('程序运行时间:' + str(end - start) + 's')
