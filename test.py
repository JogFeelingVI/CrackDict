#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/28 12:37 AM
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link    : blog.sina.com.cn/lifelse
# @Name    : test
from modex import rplan

def main():
    plan = 'h'
    vals = rplan.readplanforkey(plan)
    print(vals)

if __name__ == '__main__':
    main()
