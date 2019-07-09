# coding:utf-8
import re
text = """
<script type="text/javascript" src="https://ss1.bdstatic.cn/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/jquery/jquery-1.10.2.min_65682a2.js"></script>
"""
print(text)
print(re.findall(r"src=\"(.*)\"",text)[0])
ret = re.findall(r"src=\"(.*)\"",text)[0]
def replace(result):
    print(result.group(1))
    ret = result.group(1)
    return ret


print(re.sub("(\.\w?\w?\w/).*",replace,ret))



