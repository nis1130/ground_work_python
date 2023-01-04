# 내장모듈
# : 파이썬 설치 시 자동으로 설치되는 모듈

import math
print(math.pi)
print(math.ceil(2.9))

from math import pi as a, ceil as c
print(a)
print(c(2.9))

# 외부모듈
# : 다른 사람이 만든 파이썬 파일 pip로 설치해서 사용
# pyautogui

import pyautogui as pg
pg.moveTo(500,500, duration=2)
