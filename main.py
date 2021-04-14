from plot.plot_single_bgt import PLOT_SINGLE_BGT
from background import background as bg
from plot import PLOT_SINGLE_BGT
import os
file = r'E:\Projects\BGT_processor\background_files\Background 2028 05okt2017.bgt'
directory = r'E:\Projects\BGT_processor\background_files'

for file in os.listdir(directory):
    print(file)
    backg = bg(r'{}\{}'.format(directory, file))
    p = PLOT_SINGLE_BGT(backg)
    _ = input('press enter')
    p.show()
