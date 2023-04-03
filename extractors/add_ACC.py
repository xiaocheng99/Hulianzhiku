label=' nt'

ff = open('58q.txt', 'w', encoding='utf8')  #打开一个文件，可写模式
with open('accused_similair_tittle.txt', 'r', encoding='utf8') as f:  #打开一个文件只读模式
    line = f.readlines()
    i = 0
    for line_list in line:
        line_new =line_list.replace('\n','')  #将换行符替换为空('')
        b = str(label) #主要是这一步 将之前列表数据转为str才能加入列表
        line_new = line_new + b +'\n'
        i += 1
        print(line_new)
        ff.write(line_new) #写入一个新文件中
