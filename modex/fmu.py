# @Author: JogFeelingVi
# @Date: 2021-09-03 22:45:08
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-09-03 22:45:08
import re
from typing import List, Union


class fMoblieNumber:
    lsof_P = None

    def __init__(self, lsofp) -> None:
        self.lsof_P = lsofp
        self.find = self.lsof_P.find

    def filter(self,
               pNum: Union[int, str] = 1597257,
               fter: List[str] = ['442500']) -> bool:
        matc = re.match(r'[1][3456789][\d]{5}', f'{pNum}')
        if matc is None:
            return False
        pNum = int(f'{pNum}'[0:7])
        if (resour := self.find(pNum)) is None:
            return False
        flag = [x for x in fter if x in resour.values()]
        if flag != []:
            return True
        else:
            return False