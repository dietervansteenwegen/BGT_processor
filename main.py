from background import background as bg
from plot import plot_single_bgt_func
import os
file = r'E:\Projects\BGT_processor\background_files\Background 2028 05okt2017.bgt'
directory = r'E:\Projects\BGT_processor\background_files'

for file in os.listdir(directory):
    print(file)
    backg = bg(r'{}\{}'.format(directory, file))
    plot_single_bgt_func(backg)
