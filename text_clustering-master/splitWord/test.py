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
        '高新区政法委、应急管理局'
        , '高新区-滴滴'
        , '高新区科技和人才工作局'
        , '成都高新区电子信息产业发展有限公司'
        , '高新区新经济发展局'
        , '政务服务和网络理政办公室'
        , '国际合作投服局'
        , '高新发展股份有限公司'
        , '天府软件园公司'
        , '高新区政务服务和网络理政办公室'
        , '社事投资发展有限公司'
        , '高新区电子信息产业局'
        , '高新区国际合作投服局'
        , '电子信息产业局'
        , '交子投资公司'
        , '高新区交子投资公司'
        , '高新未来科技城发展集团'
        , '党工委管委会办公室'
        , '成都高新区社事投资发展有限公司'
        , '生物产业发展局'
        , '纪工委监察局审计局'
        , '成都高新区党工委管委会办公室'
        , '市场监管-联联'
        , '检察院'
        , '成都高新发展股份有限公司'
        , '高科公司'
        , '市场监管-快手'
        , '成都高新未来科技城发展集团'
        , '高新区政协'
        , '高新区检察院'
        , '高新区业企服务中心'
        , '成都高新区生物产业发展局'
        , '成都高新区空港办'
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
