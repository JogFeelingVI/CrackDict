# @Author: JogFeelingVi
# @Date: 2021-08-31 00:18:17
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-31 00:18:17
import enum, pathlib as plib
import itertools, functools, re, time
from typing import Any
from . import fmu
import multiprocessing as multp


class plan(enum.Enum):
    M = '1,2,3,4,5,6,7,8,9,10,11,12'
    D = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31'
    d = '0123456789'
    T = '3456789'
    s = 'qwertyuiopasdfghjklzxcvbnm'
    S = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    f = '`~!@#$%^&*()_-+=[]{}\|;:,<.>/?'
    p = 'bpmfdtnlgkhjqxrzcs'
    P = 'BPMFDTNLGKHJQXRZCS'
    h = 'ba,pa,ma,fa,da,tu,na,la,ga,ka,ha,zha,cha,sha,za,ca,sa,a,bo,po,mo,fo,o,me,de,te,ne,le,ge,ke,he,zhe,che,she,re,ze,ce,se,e,zhi,chi,shi,ri,zi,ci,si,er,bai,pai,mai,dai,tai,nai,lai,gai,kai,hai,zhai,chai,shai,zai,cai,sai,ai,bei,pei,mei,fei,dei,tei,nei,lei,gei,hei,zhei,shei,zei,ei,bao,pao,mao,dao,tao,nao,lao,gao,kao,hao,zhao,chao,shao,rao,zao,cao,sao,ao,pou,mou,fou,dou,tou,nou,lou,gou,kou,hou,zhou,chou,shou,rou,zou,cou,sou,ou,ban,pan,man,fan,dan,tan,nan,lan,gan,kan,han,zhan,chan,shan,ran,zan,can,san,an,ben,pen,men,fen,den,nen,gen,ken,hen,zhen,chen,shen,ren,zen,cen,sen,en,bang,pang,mang,fang,dang,tang,nang,lang,gang,kang,hang,zhang,chang,shang,rang,zang,cang,sang,ang,dong,tong,nong,long,gong,kong,hong,zhong,chong,rong,zong,cong,song,bi,pi,mi,di,ti,ni,li,ji,qi,xi,yi,dia,lia,jia,qia,xia,ya,bie,pie,mie,die,tie,nie,lie,jie,qie,xie,ye,biao,piao,miao,diao,tiao,niao,liao,jiao,qiao,xiao,yao,miu,diu,niu,liu,jiu,qiu,xiu,you,bian,pian,mian,dian,tian,nian,lian,jian,qian,xian,yan,bin,pin,min,nin,lin,jin,qin,xin,yin,niang,liang,jing,qiang,xiang,yang,bing,ping,ming,ding,ting,ning,ling,jing,qing,xing,ying,jiong,qiong,xiong,yong,bu,pu,mu,fu,du,tu,nu,lu,gu,ku,hu,zhu,chu,shu,ru,zu,cu,su,wu,gua,kua,hua,zhua,shua,wa,duo,tuo,nuo,luo,guo,kuo,huo,zhuo,chuo,shuo,ruo,zuo,cuo,suo,wo,guai,kuai,huai,zhuai,chuai,shuai,wai,dui,tui,gui,kui,hui,zhui,chui,shui,rui,zui,cui,sui,wei,duan,tuan,nuan,luan,guan,kuan,huan,zhuan,chuan,shuan,ruan,zuan,zuan,cuan,suan,wan,dun,tun,lun,gun,kun,hun,zhun,chun,shun,run,zun,cun,sun,wen,guang,kuang,huang,zhuang,chuang,shuang,wang,weng,nu,lu,ju,qu,xu,yu,nue,lue,jue,que,xue,yue,juan,quan,xuan,yuan,jun,qun,xun,yun'
    H = 'Ba,Pa,Ma,Fa,Da,Tu,Na,La,Ga,Ka,Ha,Zha,Cha,Sha,Za,Ca,Sa,A,Bo,Po,Mo,Fo,O,Me,De,Te,Ne,Le,Ge,Ke,He,Zhe,Che,She,Re,Ze,Ce,Se,E,Zhi,Chi,Shi,Ri,Zi,Ci,Si,Er,Bai,Pai,Mai,Dai,Tai,Nai,Lai,Gai,Kai,Hai,Zhai,Chai,Shai,Zai,Cai,Sai,Ai,Bei,Pei,Mei,Fei,Dei,Tei,Nei,Lei,Gei,Hei,Zhei,Shei,Zei,Ei,Bao,Pao,Mao,Dao,Tao,Nao,Lao,Gao,Kao,Hao,Zhao,Chao,Shao,Rao,Zao,Cao,Sao,Ao,Pou,Mou,Fou,Dou,Tou,Nou,Lou,Gou,Kou,Hou,Zhou,Chou,Shou,Rou,Zou,Cou,Sou,Ou,Ban,Pan,Man,Fan,Dan,Tan,Nan,Lan,Gan,Kan,Han,Zhan,Chan,Shan,Ran,Zan,Can,San,An,Ben,Pen,Men,Fen,Den,Nen,Gen,Ken,Hen,Zhen,Chen,Shen,Ren,Zen,Cen,Sen,En,Bang,Pang,Mang,Fang,Dang,Tang,Nang,Lang,Gang,Kang,Hang,Zhang,Chang,Shang,Rang,Zang,Cang,Sang,Ang,Dong,Tong,Nong,Long,Gong,Kong,Hong,Zhong,Chong,Rong,Zong,Cong,Song,Bi,Pi,Mi,Di,Ti,Ni,Li,Ji,Qi,Xi,Yi,Dia,Lia,Jia,Qia,Xia,Ya,Bie,Pie,Mie,Die,Tie,Nie,Lie,Jie,Qie,Xie,Ye,Biao,Piao,Miao,Diao,Tiao,Niao,Liao,Jiao,Qiao,Xiao,Yao,Miu,Diu,Niu,Liu,Jiu,Qiu,Xiu,You,Bian,Pian,Mian,Dian,Tian,Nian,Lian,Jian,Qian,Xian,Yan,Bin,Pin,Min,Nin,Lin,Jin,Qin,Xin,Yin,Niang,Liang,Jing,Qiang,Xiang,Yang,Bing,Ping,Ming,Ding,Ting,Ning,Ling,Jing,Qing,Xing,Ying,Jiong,Qiong,Xiong,Yong,Bu,Pu,Mu,Fu,Du,Tu,Nu,Lu,Gu,Ku,Hu,Zhu,Chu,Shu,Ru,Zu,Cu,Su,Wu,Gua,Kua,Hua,Zhua,Shua,Wa,Duo,Tuo,Nuo,Luo,Guo,Kuo,Huo,Zhuo,Chuo,Shuo,Ruo,Zuo,Cuo,Suo,Wo,Guai,Kuai,Huai,Zhuai,Chuai,Shuai,Wai,Dui,Tui,Gui,Kui,Hui,Zhui,Chui,Shui,Rui,Zui,Cui,Sui,Wei,Duan,Tuan,Nuan,Luan,Guan,Kuan,Huan,Zhuan,Chuan,Shuan,Ruan,Zuan,Zuan,Cuan,Suan,Wan,Dun,Tun,Lun,Gun,Kun,Hun,Zhun,Chun,Shun,Run,Zun,Cun,Sun,Wen,Guang,Kuang,Huang,Zhuang,Chuang,Shuang,Wang,Weng,Nu,Lu,Ju,Qu,Xu,Yu,Nue,Lue,Jue,Que,Xue,Yue,Juan,Quan,Xuan,Yuan,Jun,Qun,Xun,Yun'


def pathdat(path: str):
    try:
        import sys
        p = plib.Path(path).parent
        data = plib.Path(p, 'phonedat/phone.py')
        sys.path.append(data)
        import phonedat.phone
        ph = phonedat.phone.Phone()
        return ph
    except:
        return None


def pathx(file: str) -> plib.PosixPath:
    p = plib.Path(file).absolute()
    return p


def jionStr(*lis):
    fx = '{}' * lis.__len__()
    return fx.format(*lis)


class yieldxlis:
    index = 0
    pgcount = -1
    pgsize = 0

    def __init__(self, Total: int, GPS: list, pgsize: int = 100000) -> None:
        self.xgps = itertools.product(*GPS)
        self.pgcount = Total // pgsize
        self.pgsize = pgsize

    def page(self) -> list:
        '''
            Read Page
        '''
        while self.index <= self.pgcount:
            yield itertools.islice(self.xgps, self.pgsize)
            self.index += 1


class logs_ex:
    def __init__(self, text:str) -> None:
        self.T = text

    def __call__(self, func, *args: Any, **kwds: Any) -> Any:
        @functools.wraps(func)
        def inner(*args: Any, **kwds: Any) -> Any:
            self.StoLog(func)
            retx = func(*args, **kwds)
            return retx
        return inner
    
    def StoLog(self, func):
        logS = f'{time.localtime()} {self.T} {func.__name__}'
        with open('./Logs.log', 'a+', 'utf-8') as wlogs:
            wlogs.write(logS)


class wfileplus:
    file = None
    total = 0
    Minimum = 8
    fmua = None
    plus_fmu = None
    save = 0
    __STN = time.time()
    __PSN = time.time()

    def __init__(self, file: plib.PosixPath, GPS: list, total: int) -> None:
        self.file = file
        self.total = total
        self.yieldxlis = yieldxlis(total, GPS)

    def Progress(self, r: int):
        self.save += r
        if time.time() - self.__PSN >= 1.31:
            tmpt = round(time.time() - self.__STN, 2)
            speed = round(self.save / tmpt, 2)
            timeleft = round((self.total - self.save) / speed, 2)
            progressv = f'[ {self.save/self.total*100:.2f} %]'
            print(f'\rProgress: {speed}kb/s {tmpt}s {timeleft}TLs {progressv}',
                  end='')
            self.__PSN = time.time()

    
    def Compared_Zi_T(self, Zip_item: list):
        zi_str = self.jionStr(*Zip_item)
        zi_str = self.filter_fmu(zi_str)
        if zi_str != 'NULL':
            zi_str = f'{zi_str}\n'
        return zi_str

    def SaveAs(self, info: list):
        '''
        Save to File
        '''
        with self.file.open(mode='a', encoding='utf-8', buffering=4096) as wfs:
            info = ''.join((f'{i}\n' for i in info))
            wfs.write(info)

    def minpw(self, Vx: int = -1):
        if Vx == -1:
            return self.Minimum
        else:
            self.Minimum = Vx
            return self.Minimum

    def fmus(self, fl: list, lsof):
        self.fmua: list = fl
        self.plus_fmu: fmu = fmu.fMoblieNumber(lsof)

    def jionStr(self, *lis):
        fx = '{}' * lis.__len__()
        fxs = fx.format(*lis)
        return fxs if len(fxs) >= self.minpw() else 'NULL'

    # def fromtlis(self) -> list:
    #     for i, x in enumerate(self.xist):
    #         yield [i, self.jionStr(*x)]

    def filter_fmu(self, xL) -> itertools.product:
        if self.fmua != [] and self.plus_fmu != None:
            xL = xL if self.plus_fmu.filter(xL, self.fmua) == True else 'NULL'
        return xL

    def writeLc(self):
        Jie = self.yieldxlis.page()
        CpuSize = multp.cpu_count()
        p = multp.Pool(processes=CpuSize)
        for jQun in Jie:
            Rns = p.map(self.Compared_Zi_T, jQun)
            buffer = [z for z in Rns if z != 'NULL']
            if buffer != []:
                self.SaveAs(buffer)
            self.Progress(len(Rns))
        size = f'{self.file.stat().st_size/1024.0:.2f}kb'
        ust = f'{time.time() - self.__STN:.2f}s'
        print(f'\rWrite completion Use time {ust} File size {size}')

        # Rns = self.RunCode_N(self.Compared_Zi, Jie)
        # ust = f'{time.time() - self.__STN:.2f} seconds'
        # sRns = sum(Rns)
        # size = f'{self.file.stat().st_size/1024.0:.2f}kb' if sRns > 0 else '0kb'
        # print(f'\nWrite completion Use time {ust} File size {size} {sRns}items')
