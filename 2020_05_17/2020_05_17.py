#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：5/17/2020  11:18 PM 
# 文件名称   ：2020_05_17.py


def decodeMorse(morse_code):
   return ' '.join(''.join(MORSE_CODE[word] for word in morse_word.split(' ')) for morse_word in morse_code.strip().split('   '))
