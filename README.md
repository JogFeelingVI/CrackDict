# CrackDict
## hashCat -- CrackDict 中文拼音wifi密码字典生成工具 Python3 以上适用
### 基本功能,根据设定规则,生成字典文件适用与数字密码、英文密码、汉语拼音密码等，是hashcat的掩码功能拓展

## Install

```
chmod +x cdlis.command
ln -s ~/Downloads/cdlis.command /usr/local/bin/cdlis
```

## Running effect
```
↪ cdlis -p Ppdddddd
  Archives: {'var': 1.02, 'cust': None, 'plan': 'Ppdddddd', 'out': None, 'list': False}
  Number of password digits {8}
  Scope: Bb000000-Ss999999
  Count: 324,000,000 Done!
  OutFile: /Users/feeling/Downloads/crack_wifi/Zhao/Ss999999.lst
  Progress: 445.52s [100.00%]
  Write completion Use time 445.54 seconds File size 2847656.25kb
    
  hashcat -m 2500 -a 0 ./xxx.hccapx cuslist.lst`
```

## plan key

```
  M - 1,2,3,4,5,6,7,8,9,10,11,12
  D - 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
  d - 0,1,2,3,4,5,6,7,8,9
  s - q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m
  S - Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M
  f - `,~,!,@,#,$,%,^,&,*,(,),_,-,+,=,[,],{,},\,|,;,:,,,<,.,>,/,?
  p - b,p,m,f,d,t,n,l,g,k,h,j,q,x,r,z,c,s
  P - B,P,M,F,D,T,N,L,G,K,H,J,Q,X,R,Z,C,S
  h - ba,pa,ma,fa,da,tu,na,la,ga,ka,ha,zha,cha,sha,za,ca,sa,a,bo,po,mo,fo,o,me,de,te,ne,le,ge,ke,he,zhe,che,she,re,ze,ce,se,e,zhi,chi,shi,ri,zi,ci,si,er,bai,pai,mai,dai,tai,nai,lai,gai,kai,hai,zhai,chai,shai,zai,cai,sai,ai,bei,pei,mei,fei,dei,tei,nei,lei,gei,hei,zhei,shei,zei,ei,bao,pao,mao,dao,tao,nao,lao,gao,kao,hao,zhao,chao,shao,rao,zao,cao,sao,ao,pou,mou,fou,dou,tou,nou,lou,gou,kou,hou,zhou,chou,shou,rou,zou,cou,sou,ou,ban,pan,man,fan,dan,tan,nan,lan,gan,kan,han,zhan,chan,shan,ran,zan,can,san,an,ben,pen,men,fen,den,nen,gen,ken,hen,zhen,chen,shen,ren,zen,cen,sen,en,bang,pang,mang,fang,dang,tang,nang,lang,gang,kang,hang,zhang,chang,shang,rang,zang,cang,sang,ang,dong,tong,nong,long,gong,kong,hong,zhong,chong,rong,zong,cong,song,bi,pi,mi,di,ti,ni,li,ji,qi,xi,yi,dia,lia,jia,qia,xia,ya,bie,pie,mie,die,tie,nie,lie,jie,qie,xie,ye,biao,piao,miao,diao,tiao,niao,liao,jiao,qiao,xiao,yao,miu,diu,niu,liu,jiu,qiu,xiu,you,bian,pian,mian,dian,tian,nian,lian,jian,qian,xian,yan,bin,pin,min,nin,lin,jin,qin,xin,yin,niang,liang,jing,qiang,xiang,yang,bing,ping,ming,ding,ting,ning,ling,jing,qing,xing,ying,jiong,qiong,xiong,yong,bu,pu,mu,fu,du,tu,nu,lu,gu,ku,hu,zhu,chu,shu,ru,zu,cu,su,wu,gua,kua,hua,zhua,shua,wa,duo,tuo,nuo,luo,guo,kuo,huo,zhuo,chuo,shuo,ruo,zuo,cuo,suo,wo,guai,kuai,huai,zhuai,chuai,shuai,wai,dui,tui,gui,kui,hui,zhui,chui,shui,rui,zui,cui,sui,wei,duan,tuan,nuan,luan,guan,kuan,huan,zhuan,chuan,shuan,ruan,zuan,zuan,cuan,suan,wan,dun,tun,lun,gun,kun,hun,zhun,chun,shun,run,zun,cun,sun,wen,guang,kuang,huang,zhuang,chuang,shuang,wang,weng,nu,lu,ju,qu,xu,yu,nue,lue,jue,que,xue,yue,juan,quan,xuan,yuan,jun,qun,xun,yun
```

## wiki

`CrackDict Wiki` [Click Me](https://github.com/JogFeelingVI/CrackDict/wiki)