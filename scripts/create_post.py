import os
import datetime
import click

@click.command()
@click.option("-t", "--title", required=True, help="博客标题")
@click.option("-c", "--categories", default="", help="博客分类")
@click.option("-g", "--tags", default="", help="博客标签")
@click.option("--math/--no-math", default=False, help="是否使用数学公式")
def create_blog_post(title, categories, tags, math):
    # 获取当前日期和时间
    current_datetime = datetime.datetime.now()

    # 格式化日期和时间
    formatted_datetime = current_datetime.strftime(r"%Y-%m-%d %H:%M:%S")

    # 创建文件名
    filename = f"{current_datetime.strftime(r'%Y-%m-%d')}-{title}.md"

    # 创建文件路径
    file_path = os.path.join("_posts", filename)

    categories = ", ".join(categories.split(","))
    tags = ", ".join(tags.split(","))

    # 构建文件内容
    content = f'''---
title: {title}
date: {formatted_datetime} +/-TTTT
categories: [{categories}]
tags: [{tags}]
math: {str(math).lower()}
---'''

    # 写入文件
    with open(file_path, "w") as file:
        file.write(content)

    click.echo(f"blog '{filename}' create successfully!")

if __name__ == "__main__":
    # py scripts/create_post.py -t test2 -c 1,2,3 -g 1,2
    create_blog_post()