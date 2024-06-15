import os

# 需要每次设置

# 博客地址
blog_url = "https://drun1baby.top/"
# xpath
select = '(//div[@class="btn-wrap allowed"]/a[@class="jump-btn"])[last()]/@href'
# 选择模式，每次解析下一页的时候会询问是否继续，用于xpath查询语句不好写的时候进行半自动解析
console_mode = False
# 只通过txt文件进行下载，而不进行解析操作
pdf_mode = True
# 重试最大次数
max_retry = 5

# ----------------------------------------------------
# 脚本配置
# 当前路径
dir_path = os.path.dirname(os.path.abspath(__file__))
# wkhtmltopdf路径
pdf_bin = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# 文章输出位置
output = dir_path + "/output/"
# 代理设置
proxy_url = 'http://127.0.0.1:7890'

# 不需要设置
# 博客作者
blog_name = blog_url.replace("http://", "").replace("https://", "").rstrip('/').split(".")[-2]
# 博客归档地址
archives_url = blog_url + "archives/"
proxy = {'http': proxy_url[7:]}
retry = max_retry
