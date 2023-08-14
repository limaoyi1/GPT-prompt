# -*- coding: utf-8 -*-
# @Time    : 2023/8/14 9:06
# @Author  : limaoyi
# @File    : all_class_table.py
# @Software: PyCharm
# @GitHub  : https://github.com/limaoyi1/GPT-prompt

import os
import imp
import inspect


def get_all_class_from_modules(modules_list):
    """可以用inspect直接根据module拿到其中所有的类 wangxiaofeng01@corp.netease.com

    :param modules_list:
    :return:
    """
    class_list = {}
    for module in modules_list:
        for name, obj in inspect.getmembers(module, inspect.isclass):
                class_list[name] = obj
    return class_list



def get_all_modules(modules_path_list):
    """ 根据文件的路径，可以通过imp直接引入这个文件module wangxiaofeng01@corp.netease.com

    :param modules_path_list:
    :return:
    """
    all_modules = []
    for path in modules_path_list:
        module = imp.load_source('', path)
        all_modules.append(module)
    return all_modules


def get_all_modules_path(dir):
    """../代表上层路径开始，直接写相当于当前路径开始 wangxiaofeng01@corp.netease.com
    用os.walk可以递归找到所有的文件

    :param dir: the modules you need dir
    :return: list[modules]
    """
    all_modules_path = []
    # root就是你输入的目录，作为根目录
    # dirs就是当前目录下的目录列表
    # files就是当前遍历的目录下所有的文件
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".py") and file != '__init__.py' and file != 'all_class_table.py':
                all_modules_path.append(root + '/' + file)
    return all_modules_path

# 实例化对象示例
# todo: md表头: 类名 , 英文, 中文 ,繁体中文
# 构建Markdown表格头部
markdown_table = "| class | english | 中文 | 繁體中文 |\n|------|------|------|----------|"
table_rows = []

instances = {}  # 创建一个字典来存储实例化的对象
class_dict = get_all_class_from_modules(get_all_modules(get_all_modules_path('../../gpt_prompt')))
for key, value in class_dict.items():
    print(key, value)
    try:
        instance = value()  # 创建类的实例
        instances[value] = instance  # 将实例添加到字典中
        print(f"Instance of {key} created successfully.")
        table_row = [key, instance.english.replace('\n', ' ').strip(), instance.chinese.replace('\n', ' ').strip(), instance.traditional_chinese.replace('\n', ' ').strip()]
        table_rows.append(table_row)
    except Exception as e:
        print(f"Failed to create instance of {key}: {e}")

# 构建Markdown格式的表格内容
for row in table_rows:
    markdown_table += f"\n| {' | '.join(row)} |"

# 输出Markdown表格
print(markdown_table)

# 原文链接：https://blog.csdn.net/qq_40666620/article/details/107988639