__author__ = 'zjy'
# -*- coding:utf-8 -*-
import re


# 处理页面标签类
class Tool:
    # 去除img标签,1-7位空格,
    removeImg = re.compile('<img.*?>| {1,7}| ')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    # 将多行空行删除
    removeNoneLine = re.compile('\n+')
    findMul= re.compile('.*?\?')
    removeMul = re.compile('\?')
    # 将 < > / \ | : " * ? 剔除
    removeDirectory = re.compile('<|>|/|\\\|:|"|\\*|\\?|\\|')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        # strip()将前后多余内容删除
        return x.strip()

    def replaceImgmark(self, x):
       m=re.match(self.findMul, x)
       if m:
        s=m.group()
        x = re.sub(self.removeMul, "", s)
       return x.strip()

# tool = Tool()
# res = tool.replaceXg('2017年9月2<2>日/推广|为何亚果会?果蔬展每年*都:是十一月份\开？.txt')
# print(res)