#!/bin/bash
# wget https://unicorn.drogon.net/wiringpi-2.46-1.deb
# sudo dpkg -i wiringpi-2.46-1.deb
# sudo apt-get install libc6-dbg
gcc -Wall libweight.c -fPIC -lwiringPi -shared -o libweight.so
