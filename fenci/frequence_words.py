from collections import Counter
from read_fenci import ReadFenci

fileName = r'D:\home\基于jieba的paddle分词模式全量数据.xlsx'
departName = '公安局'
sheet = 'sheet1'
fenci_list = ReadFenci.get_fenci_list(fileName, departName, sheet)
counter_list = Counter(fenci_list)
print(dict(counter_list.most_common(len(counter_list)-1)))


