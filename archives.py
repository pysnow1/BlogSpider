import requests
from parsel import Selector
from config import *


def get_all_article_links(archive_url, blog):
    """
    通过归档链接获取博客所有文章的链接列表，包括处理分页情况。

    :param blog:
    :param archive_url: 归档页面的 URL 链接
    :return: 所有文章链接的列表
    """
    black_list = ["http", "xml", "json", ".css", ".js", ".jpg", ".png", ".gif", ".jpeg", ".ico", "/archives", "cdn",
                  "/friends", "/about", "/search", "/tags", "/categories", "gallery", "javascript:", "/link"]



    def fetch_page(url):
        print(f'正在处理页面: {current_url}')
        # , verify=False
        response = requests.get(url, proxies=proxy)
        response.raise_for_status()
        return response.text

    def parse_article_links(html):

        result_links = []
        selector = Selector(html)
        article_links = selector.css('a::attr(href)').getall()

        for link in article_links:
            if not link or link == "/":
                continue
            if any(word in link for word in black_list):
                continue
            result_links.append(link)

        # 二次过滤
        # result_links = [link for link in result_links if not any(word in link for word in black_list)]

        return result_links

    def parse_next_page_link(html):
        selector = Selector(html)
        css = 'a.next::attr(href)'
        if selecter:
            css = selecter
            print("[*]自定义选择器" + css)

        next_page_link = selector.xpath('//a[@class="jump-btn"]/@href')[1].get()
        return next_page_link

    current_url = archive_url
    all_article_links = []

    while current_url:
        html = fetch_page(current_url)
        article_links = parse_article_links(html)
        all_article_links.extend(article_links)

        # 获取下一页链接
        next_page_link = parse_next_page_link(html)
        if next_page_link:

            current_url = blog + next_page_link
            print(next_page_link)
        else:
            print(next_page_link)
            current_url = None

    # 去重
    all_article_links = list(set(all_article_links))

    return all_article_links
