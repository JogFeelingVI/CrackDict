# @Author: JogFeelingVi 
# @Date: 2021-09-03 22:45:08 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-09-03 22:45:08

class fMoblieNumber:
    lsof_P = None
    def __init__(self, lsofp) -> None:
        self.lsof_P = lsofp

    def find(self, pNum:int=1597257):
        res = self.lsof_P.find(pNum)
        return res

    def filter(self, pNum:int=1597257, fter:str='442500'):
        resour = self.find(pNum)
        if resour is None:
            return False
        if fter in resour.values():
            return True
        else:
            return False