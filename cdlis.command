#!/usr/bin/env python3
# @Author: JogFeelingVi
# @Date: 2021-08-30 22:32:39
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-30 22:32:39
from modex import core, rplan
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
                         help='Save to file')
    command.add_argument('--list',
                         action='store_true',
                         default=False,
                         help='List -p char')
    command.add_argument('--dual-m',
                         action='store_true',
                         default=False,
                         help='M Parsed as MM 1 -> 01')
    command.add_argument('--dual-d',
                         action='store_true',
                         default=False,
                         help='D Parsed as DD 2 -> 02')
    command.add_argument('--dual-md',
                         action='store_true',
                         default=False,
                         help='--dual-m and --dual-d')
    command.add_argument('--minpw',
                         default=8,
                         type=int,
                         metavar='',
                         help='Minimum password length')
    command.add_argument('--fmu',
                         nargs='*',
                         metavar='fmu',
                         help='Filter Mobile Mumbers ShangHai 20000 az 021')
    args = command.parse_args().__dict__
    if (plus_fmu := rplan.pathdat(__file__)) != None and 'fmu' in args.keys():
        args['plus_fmu'] = plus_fmu
    ccurls = core.curls(args)
    ccurls.Action()


if __name__ == '__main__':
    main()