# @Author: JogFeelingVi
# @Date: 2021-08-30 23:14:22
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-30 23:14:22
from . import rplan
from itertools import zip_longest, repeat, product
from functools import reduce


class curls:
    Archives = {'var': 1.02}
    Custom = []
    Synthesis = None
    nName = ''
    Count = 0
    __act_dict = {
        'cust': lambda l: curls.__act_cust__(l),
        'plan': lambda p: curls.__act_plan__(p),
        'out': lambda o: curls.__act_out__(o),
        'list': lambda b: curls.__act_list__(b),
    }

    @classmethod
    def __act_cust__(cls, l: list):
        if l is None:
            return
        curls.Custom = l
        print(f'Save Custom list {curls.Custom}, Use -p c!')

    @classmethod
    def __act_plan__(cls, S: str):
        if S is None:
            return
        plan = list(S)
        if curls.Custom != []:
            lists = [[rplan.readplanforkey(x), curls.Custom][x == 'c']
                     for x in plan]
        else:
            lists = [rplan.readplanforkey(x) for x in plan]
        curls.Synthesis = product(*lists)
        # ('0', '1', '2', '7', '7', '5', '9', '7')
        curls.Count = reduce(lambda x, y: x * y, [len(x) for x in lists])
        start = rplan.jionStr(*[x[0] for x in lists])
        ends = rplan.jionStr(*[x[-1] for x in lists])
        lse = {len(start), len(ends)}
        print(f'Number of password digits {lse}')
        print(f'Scope: {start}-{ends}')
        curls.nName = f'{ends}'
        print(f'Count: {curls.Count:,} Done!')

    @classmethod
    def __act_out__(cls, o: str):
        if curls.Synthesis is None:
            return
        else:
            path = f'./{curls.nName}.lst' if o is None else o
            outf = rplan.pathx(path)
            print(f'OutFile: {outf}')
            #rplan.wfilefor(outf, curls.Synthesis)
            wplan = rplan.wfileplus(outf, curls.Synthesis, curls.Count)
            wplan.writels()
    @classmethod
    def __act_list__(cls, b: bool):
        if b == False:
            return
        plankeys = 'M,D,d,s,S,f,p,P'.split(',')
        for key in plankeys:
            value = ','.join(rplan.readplanforkey(key))
            print(f'- {key} {value}')
        print('- h ba,pa,ma,fa,da,tu,na,la,ga,ka,ha,zha,cha...')
        print('- c Custom list, -c xxx yyy zzz')

    def __init__(self, args: dict) -> None:
        self.Archives = {**self.Archives, **args}
        print(f'Archives: {self.Archives}')

    def Action(self):
        Sequence = 'cust,plan,out,list'.split(',')
        for Seq in Sequence:
            vals = self.Archives[Seq]
            self.__act_dict[Seq](vals)