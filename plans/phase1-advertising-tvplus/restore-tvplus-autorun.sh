#!/bin/sh
set -eu
grep -Fq 'BUILD_ID=T-KSU2EDEUC-REL-202607211851' /etc/os-release
vconftool set -t bool -f db/menu/autorun_tv_plus 1
