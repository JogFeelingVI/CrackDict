# @Author: JogFeelingVi
# @Date: 2021-08-30 23:14:22
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-30 23:14:22
from . import rplan
from itertools import zip_longest, repeat, product
from functools import reduce
import re


class curls:
    Archives = {
        'var': 1.02,
    }
    Custom = []
    fmu = []
    Synthesis = None
    nName = ''
    Count = 0
    Dataforplan = {'plan': 'TMDsSpPhHf'}

    __act_dict = {
        'cust': lambda s, l: curls.__act_cust__(s, l),
        'plan': lambda s, p: curls.__act_plan__(s, p),
        'out': lambda s, o: curls.__act_out__(s, o),
        'list': lambda s, b: curls.__act_list__(s, b),
        'dual_md': lambda s, m: curls.__act_dual_md__(s, m),
        'dual_m': lambda s, m: curls.__act_dual_m__(s, m),
        'dual_d': lambda s, m: curls.__act_dual_d__(s, m),
        'minpw': lambda s, d: curls.__act_minpw__(s, d),
        'fmu': lambda s, l: curls.__act_fmu__(s, l),
    }

    def __act_fmu__(self, l: list):
        if l is None:
            return
        self.fmu = l
        print(f'Save fmu {self.fmu} --fmu 442000 027')

    def __act_dual_m__(self, m: bool):
        if m == False:
            return
        tmp = [f'{int(m):02}' for m in self.Dataforplan['M']]
        self.Dataforplan['M'] = tmp

    def __act_dual_d__(self, m: bool):
        if m == False:
            return
        tmp = [f'{int(m):02}' for m in self.Dataforplan['D']]
        self.Dataforplan['D'] = tmp

    def __act_dual_md__(self, m: bool):
        if m == False:
            return
        self.__act_dual_m__(True)
        self.__act_dual_d__(True)

    def __act_minpw__(self, d: int):
        self.Archives['minpw'] = d

    def __act_cust__(self, l: list):
        if l is None:
            return
        self.Custom = l
        print(f'Save Custom list {self.Custom}, Use -p c!')

    def __act_plan__(self, S: str):
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
                GPS.append([self.rPlan(cl), self.Custom][cl == 'c'])
                # end
            else:
                return
        #('0', '1', '2', '7', '7', '5', '9', '7')
        self.Count = reduce(lambda x, y: x * y, [len(x) for x in GPS])
        start = rplan.jionStr(*[x[0] for x in GPS])
        ends = rplan.jionStr(*[x[-1] for x in GPS])
        lse = {len(start), len(ends)}
        minpw = self.Archives['minpw']
        # mksnumber
        bijiao = {True if x >= minpw else False for x in lse}
        if True in bijiao:
            self.Synthesis = product(*GPS)
            print(f'Number of password digits {lse}')
            print(f'Scope: {start}-{ends}')
            self.nName = f'{ends}'
            print(f'Count: {self.Count:,} Done!')
        else:
            print(
                f'minpw seting {minpw}, [ -p {S} ] Not eligible. Refer {lse}')

    def __act_out__(self, o: str):
        if self.Synthesis is None:
            return
        else:
            path = f'./{self.nName}.lst' if o is None else o
            outf = rplan.pathx(path)
            print(f'OutFile: {outf}')
            #rplan.wfilefor(outf, curls.Synthesis)
            wplan = rplan.wfileplus(outf, self.Synthesis, self.Count)
            minpw = self.Archives['minpw']
            if self.fmu != None and 'plus_fmu' in self.Archives.keys():
                wplan.fmus(self.fmu, self.Archives['plus_fmu'])
            else:
                print('Plus_fmu Start Error!')
            # wplan.fumc = {'fum': funcobj, 'args': [x, y, z]}
            print(f'Minimum password length {wplan.minpw(minpw)}')
            wplan.writeLc()

    def __act_list__(self, b: bool):
        if b == False:
            return
        plankeys = 'M,D,d,s,S,f,p,P,T'.split(',')
        for key in plankeys:
            value = ','.join(self.rPlan(key))
            print(f'- {key} {value}')
        print('- h ba,pa,ma,fa,da,tu...')
        print('- H Ba,Zhang,Zhao,Yun...')
        print('- c Custom list, -c xxx yyy zzz')

    def rPlan(self, key: str):
        if key in self.Dataforplan.keys():
            return self.Dataforplan[key]
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
        Sequence = 'minpw,cust,fmu,dual_m,dual_d,dual_md,plan,out,list'.split(
            ',')
        for Seq in Sequence:
            vals = self.Archives[Seq]
            self.__act_dict[Seq](self, vals)