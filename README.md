# CrackDict
## hashCat -- CrackDict 中文拼音wifi密码字典生成工具 Python3 以上适用
### 基本功能,根据设定规则,生成字典文件适用与数字密码、英文密码、汉语拼音密码等，是hashcat的掩码功能拓展


     ↪ python3 ~/Downloads/CrackDict/CusList.py -c1 zhaoyanhua,zhangjie -c2 0123456789x -l 1MD                             06:48:26
    [A]cus_1............: zhaoyanhua,zhangjie
    [A]cus_2............: 0123456789x
    [A]plan_list........: 1MD
    [A]outfile..........: cuslist.lst
    [A]password_min.....: 8
    [A]add_zero.........: False
    Password length.....: [ 10 ~ 14 ]
    Total number........: 744
    Page size...........: 99,999
    Cpu Core............: 4
    Progress rate.......: 100.00% / zhangjie1231
    Time consuming......: 0.00s

    hashcat -m 2500 -a 0 ./xxx.hccapx cuslist.lst`


`CrackDict Wiki`