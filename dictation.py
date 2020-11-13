#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 13:52
# @Author  : JerryFu
# @project : math_test.py
# @File    : dictation.py
# @Software: PyCharm

import pyttsx3

f = open('text.txt', 'r', encoding='UTF-8')
line = True
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
while line:
    line = f.readline()
    # print(line)
    engine.say(line)
engine.runAndWait()
