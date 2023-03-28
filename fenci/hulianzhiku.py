import pymysql
import pymysql.cursors


class Data:
    def __int__(self):
        pass

    def get_call_content(sql):
        cnn = pymysql.connect(host='210.45.212.126',  # IP
                              user='hulianzhiku',  # 用户名
                              password='hulianzhiku',  # 密码
                              port=10010,  # 端口号
                              charset='utf8',
                              database='hulianzhiku')  # 注意是utf8不是utf-8
        # 使用cursor()方法获取操作游标
        cursor = cnn.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
