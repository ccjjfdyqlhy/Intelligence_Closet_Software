import time
import sys
import os
import codecs
a=input('警告：如果你已经安装了智能衣柜管理系统，再次运行该程序会覆盖所有的程序文件，用户数据不予保留。真的要运行吗？(Y/其他)')
if a == 'Y':
    pass
else:
    quit()
os.system('cls')
print('Intelligence_Closet - Install\nCopyright.Darkstar Software,inc 2022\n此工具将自动完成对软件的安装和设定')
time.sleep(2)
print('正在下载程序文件...')
cwd=os.getcwd()
os.system('git clone https://github.com/ccjjfdyqlhy/Intelligence_Closet.git '+cwd+'/code')
print('正在检查支持库状态...')
try:
    import requests
except ModuleNotFoundError:
    print('正在补全支持库...')
    os.system('pip3 install requests')
o1=input('输入你所在的城市，以便获取天气（输入错误默认北京）>>>')
filename = '.\code\config.ICset'
with codecs.open(filename,'a',encoding='utf-8')as file_object:
    file_object.write('[ICsetupfile]\n')#抬头
    file_object.write('1\n')#首次安装
    file_object.write(o1+'\n')#设定的城市
print('写入成功')
print('正在运行程序...')
os.system('python ./code/main.py')


