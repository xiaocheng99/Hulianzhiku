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
    departNames = [
         '合作街道'
        , '芳草街街道'
        , '高新区生态环境和城市管理局'
        , '肖家河街道'
        , '社区发展治理和社会保障局'
        , '高新区公安局'
        , '税务局'
        , '高新区社区发展治理和社会保障局'
        , '企业服务中心'
        , '高新区税务局'
        , '高投集团'
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
