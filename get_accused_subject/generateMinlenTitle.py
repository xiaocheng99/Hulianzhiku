from collections import Counter

import pymysql


def conn():
    conn = pymysql.connect(host='127.0.0.1',  # IP
                           user='root',  # 用户名
                           password='19991019',  # 密码
                           port=3306,  # 端口号
                           database='gxsys')  # 注意是utf8不是utf-8

    return conn


# 输入是一个列表[s1,s2,s3....]
def find_dup_min_str(strs):
    min_str = min(strs, key=len)  # 找到最短的字符串
    sub_min_str = ''
    # KMP魔改 最长相同字符串
    for char in min_str:
        sub_min_str_bak = sub_min_str
        sub_min_str = sub_min_str + char
        for str in strs:
            res_KMP = str.find(sub_min_str)
            if res_KMP == -1:
                return sub_min_str_bak
    return sub_min_str


def get_company_name_list(cursor):
    sql = "select DISTINCT company_name from accused_subject_copy1"
    cursor.execute(sql)
    result = cursor.fetchall()
    company_name_list = []
    for item in result:
        company_name_list.append(item[0])
    # print(company_name_list)
    return company_name_list


def get_similar_title_list(cursor, company_name):
    sql = "select similar_title from accused_subject_copy1 where company_name = '" + str(company_name) + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    similar_title_list = []
    # 格式化一下获取的数据
    for item in result:
        similar_title_list.append(item[0])
    return similar_title_list
    # print(similar_title_list)


def insert_min(cursor, min_len_title, company_name):
    min_len_title = "'" + str(min_len_title) + "'"
    company_name = "'" + str(company_name) + "'"
    sql = "INSERT INTO gxsys.min_title (min_len_title,company_name) VALUES (" + min_len_title + "," + company_name + ")"
    print(sql)
    cursor.execute(sql)


def generate(cursor):
    company_name_list = get_company_name_list(cursor)
    for company_name in company_name_list:
        similar_title_list = get_similar_title_list(cursor, company_name)
        min_len_title = find_dup_min_str(similar_title_list)
        for similar_title in similar_title_list:
            if similar_title == min_len_title:
                min_len_title = ''
                break
        if len(min_len_title) < 2 or min_len_title.isdigit() or min_len_title == '成都':
            min_len_title = ''
        if min_len_title != '':
            insert_min(cursor, min_len_title, company_name)
            print("min_len_title:", min_len_title)


if __name__ == "__main__":
    '''str1 = '阿里巴巴'
    str2 = '阿里巴巴成都分公司'
    str3 = '阿里云'
    list = [str1, str2, str3]
    res = find_dup_min_str(list)
    print(res)
'''
    conn = conn()
    cursor = conn.cursor()
    generate(cursor)
    conn.commit()
    # get_company_name_list(cursor)
    # get_similar_title_list(cursor, '比特易国际儿童教育中心')
    # generate(cursor)
