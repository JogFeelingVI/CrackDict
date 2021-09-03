# @Author: JogFeelingVi
# @Date: 2021-08-30 23:14:22
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-30 23:14:22
from . import rplan
from itertools import zip_longest, repeat, product
from functools import reduce
import re


class curls:
    Archives = {'var': 1.02,}
    Custom = []
    Synthesis = None
    nName = ''
    Count = 0
    Dataforplan = {'plam': 'TMDsSpPhf'}

    __act_dict = {
        'cust': lambda l: curls.__act_cust__(l),
        'plan': lambda p: curls.__act_plan__(p),
        'out': lambda o: curls.__act_out__(o),
        'list': lambda b: curls.__act_list__(b),
        'dual_md': lambda m: curls.__act_dual_md__(m),
        'dual_m': lambda m: curls.__act_dual_m__(m),
        'dual_d': lambda m: curls.__act_dual_d__(m),
        'minpw': lambda d: curls.__act_minpw__(d),
    }

    @classmethod
    def __act_dual_m__(cls, m:bool):
        if m == False:
            return
        tmp = [f'{int(m):02}' for m in curls.Dataforplan['M']]
        curls.Dataforplan['M'] = tmp

    @classmethod
    def __act_dual_d__(cls, m:bool):
        if m == False:
            return
        tmp = [f'{int(m):02}' for m in curls.Dataforplan['D']]
        curls.Dataforplan['D'] = tmp

    @classmethod
    def __act_dual_md__(cls, m:bool):
        if m == False:
            return
        cls.__act_dual_m__(True)
        cls.__act_dual_d__(True)

    @classmethod
    def __act_minpw__(cls, d:int):
        curls.Archives['minpw'] = d

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
        # add [3456789] {1}
        GPS = []
        plan_m = re.finditer('(\[([^\[\]]*)\])|([TMDdSspPfhcH])', S)
        for m in plan_m:
            x, y = m.span()
            if y - x > 1:
                # []
                #kh = m.string[x:y].replace('[', '').replace(']','')
                kh = m.string[x:y][1:-1]
                GPS.append([f'{x}' for x in kh])
                # end
            elif y - x == 1:
                # TMDdSspPfhc
                cl = m.string[x:y]
                GPS.append([cls.rPlan(cl), curls.Custom][cl == 'c'])
                # end
            else:
                return
        #('0', '1', '2', '7', '7', '5', '9', '7')
        curls.Count = reduce(lambda x, y: x * y, [len(x) for x in GPS])
        start = rplan.jionStr(*[x[0] for x in GPS])
        ends = rplan.jionStr(*[x[-1] for x in GPS])
        lse = {len(start), len(ends)}
        minpw = curls.Archives['minpw']
        # mksnumber
        bijiao = {True if x >= minpw else False for x in lse}
        if True in bijiao:
            curls.Synthesis = product(*GPS)
            print(f'Number of password digits {lse}')
            print(f'Scope: {start}-{ends}')
            curls.nName = f'{ends}'
            print(f'Count: {curls.Count:,} Done!')
        else:
            print(f'minpw seting {minpw}, [ -p {S} ] Not eligible. Refer {lse}')

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
            minpw = curls.Archives['minpw']
            print(f'Minimum password length {wplan.minpw(minpw)}')
            wplan.writels()

    @classmethod
    def __act_list__(cls, b: bool):
        if b == False:
            return
        plankeys = 'M,D,d,s,S,f,p,P,T'.split(',')
        for key in plankeys:
            value = ','.join(rplan.readplanforkey(key))
            print(f'- {key} {value}')
        print('- h ba,pa,ma,fa,da,tu...')
        print('- H Ba,Zhang,Zhao,Yun...')
        print('- c Custom list, -c xxx yyy zzz')

    @classmethod
    def rPlan(cls, key:str):
        if key in curls.Dataforplan.keys():
            return curls.Dataforplan[key]
        else:
            return None

    def InitializationPlan(self):
        plan_d = rplan.plan.__members__
        for k, v in plan_d.items():
            if k in 'MDhH':
                tmp = v.value.split(',')
            else:
                tmp = list(v.value)
            self.Dataforplan[k] = tmp

    def __init__(self, args: dict) -> None:
        self.Archives = {**self.Archives, **args}
        self.InitializationPlan()
        print(f'Archives: {self.Archives}')


    def Action(self):
        Sequence = 'minpw,cust,dual_m,dual_d,dual_md,plan,out,list'.split(',')
        for Seq in Sequence:
            vals = self.Archives[Seq]
            self.__act_dict[Seq](vals)