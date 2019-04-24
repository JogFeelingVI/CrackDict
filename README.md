# CrackDict
## hashCat -- CrackDict 中文拼音wifi密码字典 Python3 以上适用
### 基本功能,根据设定规则,生成字典文件

> ↪ python3 ~/Downloads/CrackDict/CusList.py  -c1 zhang,zhao -l 1yyd
> [A]cus_1............: zhang,zhao
> [A]plan_list........: 1yyd
> [A]outfile..........: cuslist.lst
> Password length.....: [ 4 ]
> Total number........: 3,010,880
> Page size...........: 99,999
> Cpu Core............: 8
> Progress rate.......: 100.00% / zhaoyunyun9
> Time consuming......: 24.58s

#### 参数介绍
* -c1 -c1 abc
* -c2 -c2 xyz
* -c3 -c3 ...
* -c4 -c4 ...
> 对字典设置自定义数据,以供生产字典文件
* -l 生成字典文件的规则 默认值 Sssddddd, -c1 abc 在-l 规则中对应 1.2.3.4 注意 大小写敏感
* -o 字典文件文件名, 默认值 ./cuslist.lst

#### 内置列表
* d = list('0123456789')
* s = list('qwertyuiopasdfghjklzxcvbnm') # 按照键盘排列 更容易猜解出密码
* S = list('QWERTYUIOPASDFGHJKLZXCVBNM')
* f = list('`~!@#$%^&*()_-+=[]{}\|;:'",<.>/?") # 包含 空格键
* p = list('bpmfdtnlgkhjqxrzcs') # 汉语拼音中的声母 国人wifi常用内容,
* y = 共计388个汉语拼音
  
  > 这些列表 可以出现在-l 参数中,包括四个自定义栏位所代表的 1,2,3,4
  p 为所有中文发音的声母首字母，所以 zh ch sh 不包含在内,用到的时候可以自定义 -c1 zh,ch,sh
  y 为所有简体中文的388个发音, 在-l yyy 即可生成所有简体中文中的三个字的名称！ -l yy 即可生成两个字的名字，也可以结合 -c[1-4]使用，来减少hashcatd的运行压力，制造更加精准的字典文件。例如 -c1 zhang,zhao,zhou -l 1yy 就只生成 zhangxxx zhaoxxx zhouxxx的字典
  
 #### 汉语拼音
 > ![汉语拼音总表的圖片搜尋結果](https://github.com/JogFeelingVI/CrackDict/blob/master/view.jpeg)

#### Exp
> _> python3 ~/Downloads/CrackDict/CusList.py  -c1 abc -l 111ddd
设定了自定义-c1 为 abc 在-l 中前三位密码使用了 -c1 abc,后三位密码为数字【0-9】生成的密码为 aaa000 -> ccc999

> _> python3 ~/Downloads/CrackDict/CusList.py  -c1 abc, -l 1ddd
以上面命令基本相似，但是abc后面多了一个‘，’逗号,使得abc被识别为一个词，而不是一个列表，生成的密码为abc000 -> abc999

> 使用方法类似于 hashcat 的掩码,区别在于掩码不同,但使用方法一样！
