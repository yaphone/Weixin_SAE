#coding=utf-8

import youdao
import sys
reload(sys)
sys.setdefaultencoding('utf8')

content = "好"

print content
print youdao.youdao(content)