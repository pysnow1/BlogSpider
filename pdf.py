import pdfkit

from config import *

# 配置 wkhtmltopdf 的路径
path_wkhtmltopdf = pdf_bin
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
options = {
    'encoding': "utf-8",
    'page-size': 'A4',
    'margin-top': '10mm',
    'margin-right': '10mm',
    'margin-bottom': '0mm',
    'margin-left': '10mm',
    'no-outline': None,  # 禁用 PDF 大纲
    'load-error-handling': 'ignore',  # 忽略加载错误
    'load-media-error-handling': 'ignore',  # 忽略媒体加载错误
    'enable-local-file-access': None,  # 允许访问本地文件
    'proxy': proxy_url

}


def url_pdf(url, filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
        pdfkit.from_url(url, filename, options=options, configuration=config)
        print('完成 ' + filename)
    except Exception as e:
        print("[*]爬取失败" + url)


def html_pdf():
    pass
