import urllib.parse
import archives
import config
import pdf
from config import *


def process_blog_urls():
    file_path = os.path.join(dir_path, "blogs_url", f"{blog_name}.txt")

    folder_path = os.path.join(dir_path, "output", blog_name)

    if not os.path.exists(folder_path):
        # 创建文件夹
        os.makedirs(folder_path)
        print(f"文件夹 {folder_path} 已创建")
    else:
        print(f"文件夹 {folder_path} 已存在")

    with open(file_path, 'r', encoding='utf-8') as file:
        urls = file.readlines()

    for url in urls:
        url = blog_url.rstrip('/') + url.strip()
        if url:
            output_pdf_path = os.path.join(dir_path, "output", blog_name,
                                           f"{os.path.basename(urllib.parse.unquote(url.rstrip('/')))}.pdf")
            try:
                pdf.url_pdf(url, output_pdf_path)
                print(f"成功处理 URL: {url} FILE: {output_pdf_path}")
            except Exception as e:
                print(f"处理 URL {url} 时出错: {e}")


if __name__ == '__main__':
    print("[+]开始爬取博客: " + blog_name)
    if not pdf_mode:
        archives.get_all_article_links(archives_url)
    process_blog_urls()
