import pymysql
import csv
import socket
import struct
import time
import chardet

# mysql的配置
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

conn = pymysql.connect(**config)

count = 0;


def read_csv(filename):
    with open(filename) as f:
        return csv.reader(f)


def ip2long(ip):
    print(ip)
    # uip = ip.decode("utf-8-sig")
    # u8 = uip.encode("utf-8")
    # 检查字符编码
    # print(chardet.detect(str.encode(ip)))
    return struct.unpack("!L", socket.inet_aton(ip))[0]


if __name__ == '__main__':
    start_time = time.time()
    filename = 'H:\\dbip-city-2018-06-utf8.csv'
    # f_csv = read_csv(filename)
    try:
        with conn.cursor() as cursor:
            for row in csv.reader(open(filename, encoding='utf-8-sig')):
                count = count + 1
                # sql
                sql = 'INSERT INTO ip_store (from_ip,to_ip,country,province,city) VALUES (%s,%s,%s,%s,%s)'

                cursor.execute(sql, (ip2long(row[0]), ip2long(row[1]), row[2], row[3], row[4]))

        conn.commit()

    finally:
        conn.close()

    end_time = time.time()
    print('insert total row ', count, '---> cost time :', end_time - start_time, 's')
