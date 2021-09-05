# @Author: JogFeelingVi 
# @Date: 2021-09-03 22:45:08 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-09-03 22:45:08
import re
class fMoblieNumber:
    lsof_P = None
    def __init__(self, lsofp) -> None:
        self.lsof_P = lsofp

    def find(self, pNum:int=1597257):
        res = self.lsof_P.find(pNum)
        return res

    def filter(self, pNum:int=1597257, fter:list=['442500']):
        matc = re.match('[1][3456789][\d]{9}', pNum)
        if matc is None:
            return False
        if (resour:=self.find(pNum)) is None:
            return False
        flag = [x for x in fter if x in resour.values()]
        if flag != []:
            return True
        else:
            return False