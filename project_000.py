#-*-coding:utf-8-*-
from PIL import Image,ImageFont,ImageDraw
import sys

headPath = r'C:\\Users\\zengshuai\\Desktop\\'  #ͷ��·��
outPath = r'C:\\Users\\zengshuai\\Desktop\\'  #���ͷ��·��
fontPath = r"C:\\Windows\\Fonts\\"#����·��

headFile = 'butterfly.jpg'#ͷ���ļ�
outFile = 'output.jpg'#����ļ�

with Image.open(headPath+headFile) as img:#��ͼƬ
    draw = ImageDraw.Draw(img)#��������

    fontSize = min(img.size)//4#����ͼƬ��Сȷ�������С

    fontobj = ImageFont.truetype(font=fontPath+"AdobeHeitiStd-Regular.otf",size=fontSize,index=0,encoding="",layout_engine=None)#ʵ���������
    draw.text((img.size[0]-fontSize,0),text='5',fill=(255,0,0),font=fontobj,anchor=None)#��draw�����text�����������

    img.save(outPath+outFile)


