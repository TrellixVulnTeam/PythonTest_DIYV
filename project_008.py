#-*-coding:utf-8-*-
import io
import sys
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
soup = BeautifulSoup(open("sina.html",'rb'),'html.parser')
print(soup.get_text())#��ӡ�ı�
links = soup.find_all('link')#��ӡ����
for link in links:
    print(link)