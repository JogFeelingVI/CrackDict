#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2019-04-17 11:50
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link	: blog.sina.com.cn/lifelse
# @Name	: CusList
import argparse
import enum
import functools
import itertools as iters
import multiprocessing
import operator
import sys
import time


class Sx(enum.Enum):
    M = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    D = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
         'v', 'b', 'n', 'm']
    S = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
         'V', 'B', 'N', 'M']
    f = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}', '\\', '|',
         ';', ':', ',', '<', '.', '>', '/', '?', ' ']
    p = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'r', 'z', 'c', 's', 'zh', 'ch', 'sh']
    y = ['ba', 'pa', 'ma', 'fa', 'da', 'tu', 'na', 'la', 'ga', 'ka', 'ha', 'zha', 'cha', 'sha', 'za', 'ca', 'sa', 'a',
         'bo', 'po', 'mo', 'fo', 'o', 'me', 'de', 'te', 'ne', 'le', 'ge', 'ke', 'he', 'zhe', 'che', 'she', 're', 'ze',
         'ce', 'se', 'e', 'zhi', 'chi', 'shi', 'ri', 'zi', 'ci', 'si', 'er', 'bai', 'pai', 'mai', 'dai', 'tai', 'nai',
         'lai', 'gai', 'kai', 'hai', 'zhai', 'chai', 'shai', 'zai', 'cai', 'sai', 'ai', 'bei', 'pei', 'mei', 'fei',
         'dei', 'tei', 'nei', 'lei', 'gei', 'hei', 'zhei', 'shei', 'zei', 'ei', 'bao', 'pao', 'mao', 'dao', 'tao',
         'nao', 'lao', 'gao', 'kao', 'hao', 'zhao', 'chao', 'shao', 'rao', 'zao', 'cao', 'sao', 'ao', 'pou', 'mou',
         'fou', 'dou', 'tou', 'nou', 'lou', 'gou', 'kou', 'hou', 'zhou', 'chou', 'shou', 'rou', 'zou', 'cou', 'sou',
         'ou', 'ban', 'pan', 'man', 'fan', 'dan', 'tan', 'nan', 'lan', 'gan', 'kan', 'han', 'zhan', 'chan', 'shan',
         'ran', 'zan', 'can', 'san', 'an', 'ben', 'pen', 'men', 'fen', 'den', 'nen', 'gen', 'ken', 'hen', 'zhen',
         'chen', 'shen', 'ren', 'zen', 'cen', 'sen', 'en', 'bang', 'pang', 'mang', 'fang', 'dang', 'tang', 'nang',
         'lang', 'gang', 'kang', 'hang', 'zhang', 'chang', 'shang', 'rang', 'zang', 'cang', 'sang', 'ang', 'dong',
         'tong', 'nong', 'long', 'gong', 'kong', 'hong', 'zhong', 'chong', 'rong', 'zong', 'cong', 'song', 'bi', 'pi',
         'mi', 'di', 'ti', 'ni', 'li', 'ji', 'qi', 'xi', 'yi', 'dia', 'lia', 'jia', 'qia', 'xia', 'ya', 'bie', 'pie',
         'mie', 'die', 'tie', 'nie', 'lie', 'jie', 'qie', 'xie', 'ye', 'biao', 'piao', 'miao', 'diao', 'tiao', 'niao',
         'liao', 'jiao', 'qiao', 'xiao', 'yao', 'miu', 'diu', 'niu', 'liu', 'jiu', 'qiu', 'xiu', 'you', 'bian', 'pian',
         'mian', 'dian', 'tian', 'nian', 'lian', 'jian', 'qian', 'xian', 'yan', 'bin', 'pin', 'min', 'nin', 'lin',
         'jin', 'qin', 'xin', 'yin', 'niang', 'liang', 'jing', 'qiang', 'xiang', 'yang', 'bing', 'ping', 'ming',
         'ding', 'ting', 'ning', 'ling', 'jing', 'qing', 'xing', 'ying', 'jiong', 'qiong', 'xiong', 'yong', 'bu', 'pu',
         'mu', 'fu', 'du', 'tu', 'nu', 'lu', 'gu', 'ku', 'hu', 'zhu', 'chu', 'shu', 'ru', 'zu', 'cu', 'su', 'wu',
         'gua', 'kua', 'hua', 'zhua', 'shua', 'wa', 'duo', 'tuo', 'nuo', 'luo', 'guo', 'kuo', 'huo', 'zhuo', 'chuo',
         'shuo', 'ruo', 'zuo', 'cuo', 'suo', 'wo', 'guai', 'kuai', 'huai', 'zhuai', 'chuai', 'shuai', 'wai', 'dui',
         'tui', 'gui', 'kui', 'hui', 'zhui', 'chui', 'shui', 'rui', 'zui', 'cui', 'sui', 'wei', 'duan', 'tuan', 'nuan',
         'luan', 'guan', 'kuan', 'huan', 'zhuan', 'chuan', 'shuan', 'ruan', 'zuan', 'zuan', 'cuan', 'suan', 'wan',
         'dun', 'tun', 'lun', 'gun', 'kun', 'hun', 'zhun', 'chun', 'shun', 'run', 'zun', 'cun', 'sun', 'wen', 'guang',
         'kuang', 'huang', 'zhuang', 'chuang', 'shuang', 'wang', 'weng', 'nu', 'lu', 'ju', 'qu', 'xu', 'yu', 'nue',
         'lue', 'jue', 'que', 'xue', 'yue', 'juan', 'quan', 'xuan', 'yuan', 'jun', 'qun', 'xun', 'yun']


class anyargs:
    __func = None
    __args = None
    __Stdx = {'1': 'cus_1', '2': 'cus_2', '3': 'cus_3', '4': 'cus_4', 'd': Sx.d.value, 's': Sx.s.value, 'S': Sx.S.value,
              'f': Sx.f.value, 'p': Sx.p.value, 'y': Sx.y.value, 'M': Sx.M.value, 'D': Sx.D.value}

    def __init__(self):
        parg = argparse.ArgumentParser(prog='CusList.py', description='Cuslist by FeelingVi 1.2', usage='lifelse')
        parg.add_argument('-c1', dest='cus_1', help='Custom parameter', type=str)
        parg.add_argument('-c2', dest='cus_2', help='Custom parameter', type=str)
        parg.add_argument('-c3', dest='cus_3', help='Custom parameter', type=str)
        parg.add_argument('-c4', dest='cus_4', help='Custom parameter', type=str)
        parg.add_argument('-l', dest='plan_list', help='-l 123dS4d', type=str, default='Sssddddd')
        parg.add_argument('-o', dest='outfile', help='-o ~/Download/file.lst', type=str, default='cuslist.lst')
        parg.add_argument('--psmin', dest='password_min', help='Minimum password length', type=str, default='8')
        self.__args = parg.parse_args()
        self.args = {'username': 'JogFeelingVi'}

    @staticmethod
    def p_init(s, l):
        global gs, gl, gx
        gs = s
        gl = l
        gx = 198

    def sav_2(self, pl):
        gl.acquire()
        for x in pl:
            gs.write(x + '\n')
        gs.flush()
        gl.release()

    def __Ptostr(self, x: list) -> str:
        # 列表转化为字符串
        fx = '{}' * x.__len__()
        fx = fx.format(*x)
        fx = fx if fx.__len__() >= int(self.args['password_min']) else ''
        return fx

    def fix_2(self, pl: list):
        sTime = time.time()
        rn = [''.join(map(str, x)) for x in pl]
        self.sav_2(rn)
        return {'len': rn.__len__(), 'time': time.time() - sTime, 'exp': '{}'.format(rn[-1])}

    def Stdout(self, keyn, val):
        # progress rate
        pbar = '\r{:.<20}: {}'.format(keyn, val)
        sys.stdout.write(pbar)
        sys.stdout.flush()

    def format_arg(self):
        for k, v in self.__args.__dict__.items():
            if v is not None:
                self.args[k] = [x for x in v.split(',') if x != ''] if v.find(',') != -1 else v
                print('{:.<20}: {}'.format('[A]' + k, v))

        self.__args = list()
        for x in list(self.args['plan_list']):
            vx = self.__Stdx.get(x)
            vx = vx if type(vx) == list else list(self.args.get(vx))
            self.__args.append(vx)
        glist = Generate_list(*self.__args)
        print('{:.<20}: [ {} ]'.format('Password length', glist.Lens))
        print('{:.<20}: {:,}'.format('Total number', glist.total))
        print('{:.<20}: {:,}'.format('Page size', glist.size))

        lock = multiprocessing.Lock()
        cpu_core = multiprocessing.cpu_count()

        print('{:.<20}: {:,}'.format('Cpu Core', cpu_core))
        with open(self.args['outfile'], 'w+', encoding='utf=8') as save:
            mpls = multiprocessing.Pool(processes=cpu_core * 2, initializer=self.p_init, initargs=(save, lock))
            vals, tval = 0, 0
            for x in mpls.imap(self.fix_2, glist.Islice):
                # print('{:.<20}: {}'.format('Progress_rate', x))
                vals += x.get('len')
                tval += x.get('time')
                rate = float(vals) / float(glist.total) * 100
                self.Stdout('Progress rate', '{:>6.2f}% / {: <20}'.format(rate, x.get('exp')))

            print('')
            print('{:.<20}: {:.2f}s'.format('Time consuming', tval))


class Generate_list:

    def __init__(self, *lis):
        lis = [self.convtolist(x) for x in lis]
        self.total = self.count(*lis)
        self.size = 99999
        self.list = iters.product(*lis)
        self.Lens = self.__CalcLen(*lis)

    @property
    def Islice(self):
        return (list(iters.islice(self.list, self.size)) for x in range(0, self.total, self.size))

    def count(self, *lis):
        return functools.reduce(operator.mul, (len(x) for x in lis))

    def convtolist(self, nL) -> list:
        types = {list: lambda x: x, arg: lambda x: x.value, str: lambda x: list(x), int: lambda x: (x,)}
        return types.get(type(nL))(nL)

    def __CalcLen(self, *pl: list) -> str:
        # 计算数组长度
        ex = [list({i.__len__() for i in p}) for p in pl]
        ex = list(iters.product(*ex))
        ex = {sum(x) for x in ex}
        return str(min(ex)) if ex.__len__() == 1 else '{} ~ {}'.format(min(ex), max(ex))


class Save_data:
    # 写入数据
    __index = 0

    def __init__(self, outfile):
        self.Fn = open(outfile, 'w+', encoding='utf-8')

    def __del__(self):
        self.Fn.close()

    def join_str(self, *lis) -> str:
        # list 格式化为 字符串
        fx = '{}' * lis.__len__()
        return fx.format(*lis)

    def fixs(self, pl):
        rn = [self.join_str(*x) for x in pl]
        self.__index += 1
        return rn


if __name__ == '__main__':
    arg = anyargs()
    arg.format_arg()
