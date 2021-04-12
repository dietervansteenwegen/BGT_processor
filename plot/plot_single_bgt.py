from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

datetime_format = '%d/%b/%Y, %H:%M:%S'
date_format = '%d/%b/%Y'
filename_format = '%Y%m%d_%H%M%S'

# class PLOT_SINGLE_BGT:
#     def __init__(self, bgd, show = True):
#         self.bgt = bgd
#         self.plot = plt.figure(figsize=(9,7), dpi=100)
#         print(type(self.plot))

#         self.plot.plot([x for x in range(35)], self.bgt.counts, label = 'Raw counts')
#         self.plot.legend()
#         created = self.bgd.datetime.strftime(time_format)
#         self.plot.title('Background created {}'.format(created))

#     def show(self):
#         self.plot.show()
def plot_single_bgt_func(bgt):
    created_dt = bgt.datetime.strftime(datetime_format)
    created_date = bgt.datetime.strftime(date_format)
    # plt.figure(figsize=(10,10), dpi=150)
    _,ax = plt.subplots()
    plt.plot([x for x in range(1,36)], bgt.counts, label = created_date)
    grd = plticker.MultipleLocator(base = 1)
    ax.yaxis.set_major_locator(grd)
    ax.xaxis.set_major_locator(grd)
    ax.set_xlim(0,36)
    ax.set_ylim(0,35)
    plt.title('Background created {}'.format(created_dt))
    plt.legend()
    plt.grid(True)
    filename = bgt.datetime.strftime(filename_format)
    plt.savefig(fname = filename)
    plt.close()
    # plt.show()