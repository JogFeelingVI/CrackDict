#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/28 12:37 AM
# @Author  : Lifelse (Lifelse@outlook.com)
# @Link    : blog.sina.com.cn/lifelse
# @Name    : test
import itertools

def main():
    h = 'ba,pa,ma,fa,da,tu,na,la,ga,ka,ha,zha,cha,sha,za,ca,sa,a,bo,po,mo,fo,o,me,de,te,ne,le,ge,ke,he,zhe,che,she,re,ze,ce,se,e,zhi,chi,shi,ri,zi,ci,si,er,bai,pai,mai,dai,tai,nai,lai,gai,kai,hai,zhai,chai,shai,zai,cai,sai,ai,bei,pei,mei,fei,dei,tei,nei,lei,gei,hei,zhei,shei,zei,ei,bao,pao,mao,dao,tao,nao,lao,gao,kao,hao,zhao,chao,shao,rao,zao,cao,sao,ao,pou,mou,fou,dou,tou,nou,lou,gou,kou,hou,zhou,chou,shou,rou,zou,cou,sou,ou,ban,pan,man,fan,dan,tan,nan,lan,gan,kan,han,zhan,chan,shan,ran,zan,can,san,an,ben,pen,men,fen,den,nen,gen,ken,hen,zhen,chen,shen,ren,zen,cen,sen,en,bang,pang,mang,fang,dang,tang,nang,lang,gang,kang,hang,zhang,chang,shang,rang,zang,cang,sang,ang,dong,tong,nong,long,gong,kong,hong,zhong,chong,rong,zong,cong,song,bi,pi,mi,di,ti,ni,li,ji,qi,xi,yi,dia,lia,jia,qia,xia,ya,bie,pie,mie,die,tie,nie,lie,jie,qie,xie,ye,biao,piao,miao,diao,tiao,niao,liao,jiao,qiao,xiao,yao,miu,diu,niu,liu,jiu,qiu,xiu,you,bian,pian,mian,dian,tian,nian,lian,jian,qian,xian,yan,bin,pin,min,nin,lin,jin,qin,xin,yin,niang,liang,jing,qiang,xiang,yang,bing,ping,ming,ding,ting,ning,ling,jing,qing,xing,ying,jiong,qiong,xiong,yong,bu,pu,mu,fu,du,tu,nu,lu,gu,ku,hu,zhu,chu,shu,ru,zu,cu,su,wu,gua,kua,hua,zhua,shua,wa,duo,tuo,nuo,luo,guo,kuo,huo,zhuo,chuo,shuo,ruo,zuo,cuo,suo,wo,guai,kuai,huai,zhuai,chuai,shuai,wai,dui,tui,gui,kui,hui,zhui,chui,shui,rui,zui,cui,sui,wei,duan,tuan,nuan,luan,guan,kuan,huan,zhuan,chuan,shuan,ruan,zuan,zuan,cuan,suan,wan,dun,tun,lun,gun,kun,hun,zhun,chun,shun,run,zun,cun,sun,wen,guang,kuang,huang,zhuang,chuang,shuang,wang,weng,nu,lu,ju,qu,xu,yu,nue,lue,jue,que,xue,yue,juan,quan,xuan,yuan,jun,qun,xun,yun'
    hl = [x.capitalize() for x in h.split(',')]
    hc = ','.join(hl)
    print(hc)

if __name__ == '__main__':
    main()
