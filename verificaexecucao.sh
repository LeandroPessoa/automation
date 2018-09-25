#!/bin/sh
p=$(ps -A X | grep light | grep php | awk '{print $1}')
if [ -z $p ]
 then
     	cd  automation
    nohup python3 light.py > /home/.outlight &
fi
