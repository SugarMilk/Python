# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

# Podfile

import os

project_name = None

print os.environ

path = os.environ['HOME'] + '/Desktop/Test'

for file_name in os.listdir(path):
    (file_short_name, file_extension) = os.path.splitext(file_name);

    if file_extension == '.xcodeproj':
        project_name = file_short_name


print project_name
