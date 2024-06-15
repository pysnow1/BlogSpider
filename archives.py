import time

import requests
from parsel import Selector

from config import *


def get_all_article_links(archive_url):
    black_list = ["http", "xml", "json", ".css", ".js", ".jpg", ".png", ".gif", ".jpeg", ".ico", "/archives", "cdn",
                  "/friends", "/about", "/search","/page", "/tags", "/categories", "gallery", "javascript:", "/link"]

    blog_file = open(os.path.join(dir_path, "blogs_url", f"{blog_name}.txt"), "w")

    def fetch_page(url):
        try:
            print(f'正在处理页面: {url}')
            # , verify=False
            response = requests.get(url, proxies=proxy, timeout=10)
            response.raise_for_status()
            return response.text
        except requests as e:
            print(f"{url}页面访问错误")

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

        # 二次过滤
        # result_links = [link for link in result_links if not any(word in link for word in black_list)]

        return result_links

    def parse_next_page_link(url,html):
        selector = Selector(html)
        xpath = select
        print(f"[*]{url} 使用 {xpath} 选择器")

        next_link = selector.xpath(xpath).get()
        print(next_link)
        return next_link

    current_url = archive_url
    while current_url:
        html = fetch_page(current_url)
        parse_article_links(html)

        # 获取下一页链接
        next_page_link = parse_next_page_link(current_url,html)
        if next_page_link:
            current_url = blog_url + next_page_link
        else:
            print("[!]获取下一页失败")
            time.sleep(2)
            current_url = None

    blog_file.close()
    return True
