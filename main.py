import argparse
from background import background as bg
import os

file = r'E:\Projects\BGT_processor\background_files\Background 2028 05okt2017.bgt'

backg = bg(file)
for i in dir(backg):
    print('{}: {}'.format(i,getattr(backg,i).strip()))
