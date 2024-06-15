import os

# 当前路径
dir_path = os.path.dirname(os.path.abspath(__file__))

# wkhtmltopdf路径
pdf_bin = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# 文章输出位置
output = dir_path + "/output/"

# 代理设置
proxy = {'http': '127.0.0.1:7890'}
proxy_url = 'http://127.0.0.1:7890'

# 错误日志
error_log = dir_path + "log.txt"

# next-selector，默认'a.next::attr(href)'
selecter = 'a.jump-btn i::attr(href)'

