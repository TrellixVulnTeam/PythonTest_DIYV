#-*-coding:utf-8-*-
import mysql.connector
import random

count = 200
size = 20
code_list = []
for i in range(10):#������0~9��ӵ��б�
    code_list.append(str(i))
for i in range(65, 91):#����д��ĸ��ӵ��б�
    code_list.append(chr(i))
for i in range(97, 123):#��Сд��ĸ��ӵ��б�
    code_list.append(chr(i))

conn = mysql.connector.connect(user='root',password='1402929679zs',database='test')#�������ݿ�
cursor = conn.cursor()

#�����Ż����
cursor.execute('create table if NOT EXISTS Code(id VARCHAR (20) PRIMARY key,code VARCHAR (20))')
for i in range(200):
    myslice = random.sample(code_list, size)  # ��ȡ�б���size���ȵ��������
    code = ''.join(myslice)
    cursor.execute('insert into Code(id,code)VALUES (%s,%s)',[i+1,code])
conn.commit()#�ύ����
cursor.close()#�ر��α�
