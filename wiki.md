Welcome to the CrackDict wiki!
------- 
**1.什么是 CrackDict**

> CrackDict旨在解决hashcat在猜解中文wifi密码时遇到的各种问题
> @lifelse -> 不会开枪的特工 lifelse$outlook^com -_*||

**2.如何安装**

> ?可以选择安装，也可以不安装直接使用,
```
chmod +x ./cdlis.command
ln -s ./cdlis.command /usr/local/bin/cdlis
```

**3.软件如何运行**

> 软件时Python程序,启动代码为 `cdlis` or `cdlis.command`

**4.软件有哪些内建列表**

* M = 1-12 # 月份
* D = 1-31 # 日期
* d = 0-9 # 数字
* s = q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m # 26个键盘字母
* S = s 的大写形式
* f = `,~,!,@,#,$,%,^,&,*,(,),_,-,+,=,[,],{,},\,|,;,:,,,<,.,>,/,?,空格
* p = b,p,m,f,d,t,n,l,g,k,h,j,q,x,r,z,c,s # 汉语拼音中的声母
* P = p 的大写形式
* h = 388个汉语发音 例如 zhanghaoran|张浩然
* T = 3,4,5,6,7,8,9 中国手机号码第二位数字

**5.运行参数** 

* -c  自定义数据段 -c zhang Zhang Zhao zhao
* -p 密码生成规则 -p [...]TMDdSspPfhc
* -o 密码输出文件 默认为./cuslist.lst

> `注意 -p 中允许的数值为 c.M.D.d.S.s.P.p.h.f,-c xxx yyy cc. 结果为 ['xxx', 'yyy', 'zzz']. -p cddddddd xxx12345 yyy23456 zzz34567

**6.如何生成+86手机号码**

* `↪ cdlis -p [1][3456789]ddddddddd`
> 解析 +86 手机第一位数字都是 1，第二位数字 3-9，第三位数字为0-9 所以是d 后面八位等同，其中前四位为区域码，后面四位为随机数字  [1]  [34567] 列表 13，14，15.... [...]内的字符将被解析为列表

**7.如何生成—张XX-的汉语拼音**

* `↪ cdlis -c zhang Zhang -p c[0][90]ddddd` Zhang0093216 -> Zhang0099999
* ↪ hashcat -m 2500 -a0 capture.hccapx Zhang091231.lst --session zhao -o ./passdw

> `解析 -c Zhang zhang 设定姓名拼音，之后用hh补充两个汉字拼音，在-p中 c代表自定义数据段 -c h为内置数据列表，密码总数为2*388*388 = 1,400,000`

**8.如何生成 中文手写字母的密码**

* ·cdlis -p [zZ]ssddddd· zqq00000-Zmm99999 合计135,200,000组密码

> 解析 [zZ]汉字张、郑等汉字首字母,ss 英语26个字母的小写形式，d为数字

**9.如何生成YYYYMMDD格式密码**

* ·cdlis -c 19 20 -p c[0126789]d[01]d[0123]d·

> 解析 YYYYMMDD 年四位数字 -c 19 20 只显示19xx年至20xx年.[0126789]可以组合出190x,209x年年份,[01]月份第一位数字,月份最大01-12,所以[01]d,[0123]d,指日期,日期第一位数字最小0,最大3,所以输入[0123]d
