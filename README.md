# CrackDict
## CrackDict hashCat 中文字典的扩展
### 基本功能,更具设定规则,生成字典文件
#### 参数介绍
* -c1 -c1 abc
* -c2 -c2 xyz
* -c3 -c3 ...
* -c4 -c4 ...
> 对字典设置自定义数据,以供生产字典文件
* -l 生成字典文件的规则 默认值 Sssddddd, -c1 abc 在-l 规则中对应 1.2.3.4
* -o 字典文件文件名, 默认值 cuslist.lst

#### 内置列表
* d = list('0123456789')
* s = list('qwertyuiopasdfghjklzxcvbnm')
* S = list('QWERTYUIOPASDFGHJKLZXCVBNM')
* f = list('`~!@#$%^&*()_-+=[]{}\|;:'",<.>/?")
* p = list('bpmfdtnlgkhjqxrzcs')
* y = 共计388个汉语拼音
  
  > 这些列表 可以出现在-l 参数中,包括四个自定义栏位所代表的 1,2,3,4
  p 为所有中文发音的声母首字母，所以 zh ch sh 不包含在内,用到的时候可以自定义 -c1 zh,ch,sh
  y 为所有简体中文的388个发音, 在-l yyy 即可生成所有简体中文中的三个字的名称！ -l yy 即可生成两个字的名字，也可以结合 -c[1-4]使用，来减少，hashcatd的运行压力，制造更加精准的字典文件。例如 -c1 zhang,zhao,zhou -l 1yy 就只生成-c1 中定义的姓名
  
 #### 汉语拼音
 > pinyin = 'ba,pa,ma,fa,da,tu,na,la,ga,ka,ha,zha,cha,sha,za,ca,sa,a,bo,po,mo,fo,o,me,de,te,' \
           'ne,le,ge,ke,he,zhe,che,she,re,ze,ce,se,e,zhi,chi,shi,ri,zi,ci,si,er,bai,pai,mai,' \
           'dai,tai,nai,lai,gai,kai,hai,zhai,chai,shai,zai,cai,sai,ai,bei,pei,mei,fei,dei,tei,' \
           'nei,lei,gei,hei,zhei,shei,zei,ei,bao,pao,mao,dao,tao,nao,lao,gao,kao,hao,zhao,chao,' \
           'shao,rao,zao,cao,sao,ao,pou,mou,fou,dou,tou,nou,lou,gou,kou,hou,zhou,chou,shou,rou,' \
           'zou,cou,sou,ou,ban,pan,man,fan,dan,tan,nan,lan,gan,kan,han,zhan,chan,shan,ran,zan,can,' \
           'san,an,ben,pen,men,fen,den,nen,gen,ken,hen,zhen,chen,shen,ren,zen,cen,sen,en,bang,pang,' \
           'mang,fang,dang,tang,nang,lang,gang,kang,hang,zhang,chang,shang,rang,zang,cang,sang,ang,' \
           'dong,tong,nong,long,gong,kong,hong,zhong,chong,rong,zong,cong,song,bi,pi,mi,di,ti,ni,li,ji,' \
           'qi,xi,yi,dia,lia,jia,qia,xia,ya,bie,pie,mie,die,tie,nie,lie,jie,qie,xie,ye,biao,piao,miao,' \
           'diao,tiao,niao,liao,jiao,qiao,xiao,yao,miu,diu,niu,liu,jiu,qiu,xiu,you,bian,pian,mian,dian,' \
           'tian,nian,lian,jian,qian,xian,yan,bin,pin,min,nin,lin,jin,qin,xin,yin,niang,liang,jing,qiang,' \
           'xiang,yang,bing,ping,ming,ding,ting,ning,ling,jing,qing,xing,ying,jiong,qiong,xiong,yong,bu,' \
           'pu,mu,fu,du,tu,nu,lu,gu,ku,hu,zhu,chu,shu,ru,zu,cu,su,wu,gua,kua,hua,zhua,shua,wa,duo,tuo,' \
           'nuo,luo,guo,kuo,huo,zhuo,chuo,shuo,ruo,zuo,cuo,suo,wo,guai,kuai,huai,zhuai,chuai,shuai,wai,' \
           'dui,tui,gui,kui,hui,zhui,chui,shui,rui,zui,cui,sui,wei,duan,tuan,nuan,luan,guan,kuan,huan,zhuan,' \
           'chuan,shuan,ruan,zuan,zuan,cuan,suan,wan,dun,tun,lun,gun,kun,hun,zhun,chun,shun,run,zun,cun,sun,' \
           'wen,guang,kuang,huang,zhuang,chuang,shuang,wang,weng,nu,lu,ju,qu,xu,yu,nue,lue,jue,que,xue,yue,' \
           'juan,quan,xuan,yuan,jun,qun,xun,yun'

#### Exp
> _> python3 ~/Downloads/CrackDict/CusList.py  -c1 abc -l 111ddd
设定了自定义-c1 为 abc 在-l 中前三位密码使用了 -c1 abc,后三位密码为数字【0-9】生成的密码为 aaa000 -> ccc999

> _> python3 ~/Downloads/CrackDict/CusList.py  -c1 abc, -l 1ddd
以上面命令基本相似，但是abc后面多了一个‘，’逗号,使得abc被识别为一个词，而不是一个列表，生成的密码为abc000 -> abc999
