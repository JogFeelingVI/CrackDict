# @Author: JogFeelingVi
# @Date: 2021-08-30 23:14:22
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-30 23:14:22
from . import ryaml
from itertools import zip_longest, repeat, product
from functools import reduce


class curls:
    Archives = {'var': 1.02}
    Custom = []
    Synthesis = []
    __act_dict = {
        'cust': lambda l: curls.__act_cust__(l),
        'plan': lambda p: curls.__act_plan__(p),
        'out': lambda o: curls.__act_out__(o),
        'list': lambda b: curls.__act_list__(b),
    }

    @classmethod
    def __act_cust__(cls, l: list):
        curls.Custom = l
        print(f'Save Custom list {curls.Custom}, Use -p c!')

    @classmethod
    def __act_plan__(cls, S: str):
        plan = list(S)
        print(f'Number of password digits {len(plan)}')
        if curls.Custom != []:
            lists = [[ryaml.readyaml(x), curls.Custom][x == 'c'] for x in plan]
        else:
            lists = [ryaml.readyaml(x) for x in plan]
        curls.Synthesis = product(*lists)
        # ('0', '1', '2', '7', '7', '5', '9', '7')
        lens = reduce(lambda x, y: x * y, [len(x) for x in lists])
        start = ''.join([f'{x[0]}' for x in lists])
        ends = ''.join([f'{x[-1]}' for x in lists])
        print(f'Scope: {start}-{ends}')
        print(f'Count: {lens:,} Done!')

    @classmethod
    def __act_out__(cls, o: str):
        pass

    @classmethod
    def __act_list__(cls, b: bool):
        if b == False:
            return
        plankeys = 'M,D,d,s,S,f,p,P'.split(',')
        for key in plankeys:
            value = ','.join(ryaml.readyaml(key))
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