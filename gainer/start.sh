#!/bin/bash
pkill gunicorn
echo 3 > /proc/sys/vm/drop_caches
rm -rf log/*.log
rm -rf img/*.png
rm -rf mp3/*.mp3
rm -rf pcm/*.pcm
rm -rf occupy.log
gunicorn -c gun.py occupy_receiver:app > /dev/null 2>&1 &
