from matplotlib import pyplot as plt
# from matplotlib import ticker as plticker

datetime_format = '%d/%b/%Y, %H:%M:%S'
date_format = '%d/%b/%Y'
filename_format = '%Y%m%d_%H%M%S'

class PLOT_SINGLE_BGT:
    def __init__(self, bgd, show = True):
        self.bgt = bgd
        _, self.ax = plt.subplots()
        created_date = self.bgt.datetime.strftime(date_format)
        self.ax.plot([x for x in range(1,36)], self.bgt.counts, label = created_date)
        self.ax.set_title('Background created {}'.format(created_date))
        self.ax.set_xlim(0,36)
        self.ax.set_ylim(0,35)
        self.ax.fill()


    def show(self):
        plt.show()


# def plot_single_bgt_func(bgt):
#     created_dt = bgt.datetime.strftime(datetime_format)
#     created_date = bgt.datetime.strftime(date_format)
#     # plt.figure(figsize=(10,10), dpi=150)
#     _,ax = plt.subplots()
#     plt.plot([x for x in range(1,36)], bgt.counts, label = created_date)
#     grd = plticker.MultipleLocator(base = 1)
#     ax.yaxis.set_major_locator(grd)
#     ax.xaxis.set_major_locator(grd)
#     ax.set_xlim(0,36)
#     ax.set_ylim(0,35)
#     plt.title('Background created {}'.format(created_dt))
#     plt.legend()
#     plt.grid(True)
#     filename = bgt.datetime.strftime(filename_format)
#     plt.savefig(fname = filename)
#     plt.close()
#     # plt.show()