#-*-coding:utf-8-*-
from collections import Counter

with open(r'C:\Users\zengshuai\Desktop\Test\text.txt','r') as file:#���ı��ļ�
    s = file.readlines()#��ȡ�ı����������б�
    ss = ''.join(s)#�����б�����
    sss = ss.split()#���ַ����ָ�
    print(s)
    l = []
    for word in sss:
        if word.isalpha():#�жϵ����Ƿ�ȫ����ĸ���
            l.append(word)
    count = Counter(l)
    print(count)