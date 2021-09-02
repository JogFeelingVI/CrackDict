#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/28 12:37 AM
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link    : blog.sina.com.cn/lifelse
# @Name    : test
import itertools

def main():
    x = itertools.count(start=0, step=1)
    while True:
        print(x())

if __name__ == '__main__':
    main()
