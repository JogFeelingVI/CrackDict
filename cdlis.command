#!/usr/bin/env python3
# @Author: JogFeelingVi
# @Date: 2021-08-30 22:32:39
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-30 22:32:39
from modex import core
import argparse


def main():
    command = argparse.ArgumentParser(prog='cdlis',
                                      description='WIFI Dict for china')
    command.add_argument('-c',
                         dest='cust',
                         nargs='*',
                         metavar='Custom',
                         help='Customized Phrases -c xxx yyy ccc')
    command.add_argument('-p',
                         dest='plan',
                         metavar='plan list',
                         help='Combination method, def -p Pppddddd',
                         type=str)
    command.add_argument('-o',
                         dest='out',
                         metavar='outfile',
                         default='./curlis.lst',
                         help='save to file'),
    command.add_argument('--list',
                         action='store_true',
                         default=False,
                         help='List -p char')
    args = command.parse_args()
    ccurls = core.curls(args=args.__dict__)
    ccurls.Action()


if __name__ == '__main__':
    main()