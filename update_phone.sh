#!/bin/bash
# @Author: JogFeelingVi
# @Date: 2021-09-01 10:07:27
# @Last Modified by:   By JogFeelingVi
# @Last Modified time: 2021-09-01 10:07:27

PDIR="/tmp/phone"

if [ -d "$PDIR" ]
then
    echo "Clearance $PDIR ..."
    rm -rf "$PDIR"
fi
git clone 'https://github.com/ls0f/phone.git' $PDIR
cp -R "$PDIR/phone/phone.dat" ./phonedat/phone.dat
cp -R "$PDIR/phone/phone.py" ./phonedat/phone.py
cp -R "$PDIR/phone/test_phone.py" ./phonedat/test_phone.py
cp -R "$PDIR/README.md" ./phonedat/README.md
echo "Update completed"
