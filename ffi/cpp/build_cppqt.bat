#!/usr/bin/env bash
### for linux ###
# export QTDIR=~/Qt5.7.0/5.7/gcc_64
### for macos ###
# export QTDIR=~/Qt/5.9.2/clang_64
export QT_SELECT=qt5
qmake jtd_cppqt.pro
make
