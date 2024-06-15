import os
import time
import urllib.parse
import archives
import pdf
from config import *


def process_blog_urls(current_url, current_name):
    """
    读取指定目录下的文本文件中的每一行 URL，并调用 pdf.url_pdf 函数处理这些 URL。

    :param current_url:
    :param current_name: 文本文件的名称（不包含扩展名）
    """
    file_path = os.path.join(dir_path, "blogs_url", f"{current_name}.txt")

    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在")
        return
    folder_path = os.path.join(dir_path, "output", current_name)

    if not os.path.exists(folder_path):
        # 创建文件夹
        os.makedirs(folder_path)
        print(f"文件夹 {folder_path} 已创建")
    else:
        print(f"文件夹 {folder_path} 已存在")

    with open(file_path, 'r', encoding='utf-8') as file:
        urls = file.readlines()

    for url in urls:
        url = current_url[:-1] + url.strip()
        if url:
            output_pdf_path = os.path.join(dir_path, "output", current_name,
                                           f"{os.path.basename(urllib.parse.unquote(url.rstrip('/')))}.pdf")
            try:
                pdf.url_pdf(url, output_pdf_path)
                print(f"成功处理 URL: {url} FILE: {output_pdf_path}")
            except Exception as e:
                print(f"处理 URL {url} 时出错: {e}")


def archive_urls(archive, name,blog):
    url = archive
    article_links = archives.get_all_article_links(url, blog)
    filename = dir_path + "/blogs_url/" + name + ".txt"
    with open(filename, 'w') as f:
        for item in article_links:
            print(f"获取到文章链接: {item}")
            f.write(f"{item}\n")
    print(f"[*]获取完成,请到{filename}手动去除错误文章链接")


if __name__ == '__main__':
    blog_archives = open("ctfer.txt", "r").readlines()

    for blogs in blog_archives:
        if "||" in blogs:
            # 博客地址
            blog_url = blogs.split("||")[0]
            # 博客归档地址
            archives_url = blog_url + blogs.split("||")[1]
        else:
            blog_url = blogs
            archives_url = blog_url + "archives/"
        # 博客作者
        blog_name = blog_url.replace("http://", "").replace("https://", "")[:-1].split(".")[-2]

        print("[+]开始获取文章链接" + blog_name)
        archive_urls(archives_url, blog_name, blog_url)

        process_blog_urls(blog_url, blog_name)
