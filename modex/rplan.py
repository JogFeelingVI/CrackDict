# @Author: JogFeelingVi
# @Date: 2021-08-31 00:18:17
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-08-31 00:18:17
import enum, pathlib as plib
import itertools, time
import re


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


def readplanforkey(key: str = 's') -> list:
    plan_d = plan.__members__
    if key in plan_d.keys():
        item = plan.__members__[key]
        if key in 'MDh':
            item = item.value.split(',')
        else:
            item = list(item.value)
        return item
    else:
        return None


def pathx(file: str) -> plib.PosixPath:
    p = plib.Path(file).absolute()
    return p


def jionStr(*lis):
    fx = '{}' * lis.__len__()
    return fx.format(*lis)


class wfileplus:
    file = None
    xist = None
    total = 0
    Minimum = 8

    def __init__(self, file: plib.PosixPath, xlis: itertools.product,
                 total: int) -> None:
        self.file = file
        self.xist = xlis
        self.total = total

    def minpw(self, Vx: int = -1):
        if Vx == -1:
            return self.Minimum
        else:
            self.Minimum = Vx
            return self.Minimum

    def jionStr(self, *lis):
        fx = '{}' * lis.__len__()
        fxs = fx.format(*lis)
        return fxs if len(fxs) >= self.minpw() else 'NULL'

    def fromtlis(self) -> list:
        for i, x in enumerate(self.xist):
            yield [i, self.jionStr(*x)]

    def writels(self):
        buffer, count, bs, save = list(), 0, 50000, 0
        STN = time.time()
        with self.file.open(mode='w+', encoding='utf-8',
                            buffering=4096) as wfs:
            for i, xL in self.fromtlis():
                print(f'debug: {i} {xL}')
                if xL not in [
                        'NULL',
                ]:
                    buffer.append(f'{xL}\n')
                    save += 1
                    count += 1
                if count == bs or self.total - i == 1:
                    wfs.writelines(buffer)
                    count = 0
                    buffer.clear()
                    tmpt = f'{time.time()-STN:.2f}'
                    print(
                        f'\rProgress: {save/10000:,}xW {tmpt}s [{i/self.total*100:.2f}%]',
                        end='')
        ust = f'{time.time() - STN:.2f} seconds'
        size = f'{self.file.stat().st_size/1024.0:.2f}kb'
        print(f'\nWrite completion Use time {ust} File size {size}')
