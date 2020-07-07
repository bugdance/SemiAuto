#!/bin/bash
pkill gunicorn
echo 3 > /proc/sys/vm/drop_caches