# @Author: JogFeelingVi 
# @Date: 2021-09-03 22:53:25 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-09-03 22:53:25
from modex import rplan, fmu

def main():
    p = rplan.pathdat(__file__)
    fpm = fmu.fMoblieNumber(p)
    for p in range(1300000, 1599999):
        if (pfter:=fpm.filter(p, '442000')) == True:
            print(pfter)

if __name__ == '__main__':
    main()