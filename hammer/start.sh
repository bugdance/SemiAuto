#!/bin/bash
pkill python3
echo 3 > /proc/sys/vm/drop_caches
rm -rf test.log
python3 login_xw.py > /dev/null 2>&1 &
