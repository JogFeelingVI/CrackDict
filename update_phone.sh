#!/bin/bash
# @Author: JogFeelingVi
# @Date: 2021-09-01 10:07:27
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-09-01 10:07:27

PDIR="./phonedat"

if [ ! -d "$PDIR" ]
then
    echo "mkdir $PDIR ..."
    mkdir "$PDIR"
fi
echo 'Download phone dat/py'
curl -Ls  -o "$PDIR/phone.dat" "https://github.com/xluohome/phonedata/raw/master/phone.dat"
#curl -Ls -o "$PDIR/phone.py" "https://github.com/ls0f/phone/raw/master/phone/phone.py"
echo "Update completed"
