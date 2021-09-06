# CrackDict
###### hashcat dictionary generation tool,For MacOs and Linux
-----
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
  h - ba,pa,ma,jun,qun,xun,yun...
  H - h 首字母大写形式 Chuang Wang ...
```
-------
** 感谢phone数据提供者 **

* [lsof](https://github.com/ls0f/phone) phone.py
* [xluohome](https://github.com/xluohome/phonedata) phone.dat

## wiki

`CrackDict Wiki` [Click Me](https://github.com/JogFeelingVI/CrackDict/wiki)