import argparse
from background import background as bg
import os

file = r'E:\Projects\BGT_processor\backgrounds\Background 2028 01jun2018.bgt'

backg = bg(file)
for i in dir(backg):
    print('{}: {}'.format(i,getattr(backg,i).strip()))
