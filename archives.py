import time
from wsgiref import headers

import requests
from parsel import Selector

from config import *


def get_all_article_links(archive_url):
    black_list = ["http", "xml", "json", ".css", ".js", ".jpg", ".png", ".gif", ".jpeg", ".ico", "/archives", "cdn",
                  "/friends", "/about", "/search", "/page", "/tags", "/categories", "gallery", "javascript:", "/link"]

    blog_file = open(os.path.join(dir_path, "blogs_url", f"{blog_name}.txt"), "w")

    def fetch_page(url):
        global retry
        while retry > 0:
            try:
                print(f'正在处理页面: {url}')
                # , verify=False
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/125.0.0.0 Safari/537.36'}
                response = requests.get(url, proxies=proxy, timeout=10, verify=False, headers=headers)
                return response.text
            except Exception as e:
                print(f"{url} 页面访问错误")

                retry -= 1
                print(f"重试{url} 还剩{str(retry)}次")

        print(f"{url}访问失败，停止解析并开始下载pdf")
        retry = max_retry
        return False

    def parse_article_links(res_html):
        print(f"[*]正在获取当前页面所有文章链接")
        result_links = []
        selector = Selector(res_html)
        all_links = selector.css('a::attr(href)').getall()
        # 去重
        all_links = list(set(all_links))

        for link in all_links:
            if not link or link == "/":
                continue
            if any(word in link for word in black_list):
                continue
            print(f"[+]{blog_name}.txt写入link: {link}")
            blog_file.write(link + "\n")

        return result_links

    def parse_next_page_link(url, html):
        selector = Selector(html)
        xpath = select
        print(f"[*]{url} 使用 {xpath} 选择器")

        next_link = selector.xpath(xpath).get()
        print(next_link)
        return next_link

    current_url = archive_url

    while current_url:
        html = fetch_page(current_url)
        if not html:
            break
        parse_article_links(html)

        # 获取下一页链接
        next_page_link = parse_next_page_link(current_url, html)
        if next_page_link:
            current_url = blog_url.rstrip("/") + next_page_link
            if console_mode:
                mode = input(f"[~]下一页链接为{next_page_link},是否停止爬取(0为中止) ")
                if mode == "0":
                    current_url = None
        else:
            print("[!]获取下一页失败")
            time.sleep(2)
            current_url = None

    blog_file.close()
    return True
