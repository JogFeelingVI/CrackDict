#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/28 12:37 AM
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link    : blog.sina.com.cn/lifelse
# @Name    : test
from modex import ryaml as rys

def main():
    plan = 'h'
    vas = rys.readyaml(plan)
    print(f' test {vas}')

if __name__ == '__main__':
    main()
