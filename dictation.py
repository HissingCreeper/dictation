#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 13:52
# @Author  : JerryFu
# @project : math_test.py
# @File    : dictation.py
# @Software: PyCharm

import pyttsx3

f = open('dictation_text.txt', 'r')
line = f.readline()
engine = pyttsx3.init()
while line: 
    line = f.readline() 
    print(line, end='')
    engine.say(line)
engine.runAndWait()
