# @Author: JogFeelingVi 
# @Date: 2021-08-31 00:18:17 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2021-08-31 00:18:17
import yaml, pathlib as plib

def pathx():
    p = plib.Path(__file__).parent.parent
    fp = plib.Path(p, './plan.yaml')
    return fp if fp.exists() else None

def readyaml(key:str = 's'):
    if (p:=pathx()) != None:
        with open(p) as plan:
            lis = yaml.full_load(plan).get('plans')
            if key in lis.keys():
                lis_v = lis[key]
                tmp = [list(lis_v), lis_v.split(',')][key in 'MDh']
                return tmp
    else:
        print(f'plan.yaml Not Found')
