_err_incorrect_length = 'Source file does not have the correct number of lines: {}'
import datetime as dt

class background:

    def __init__(self, source):
        self.counts = []
        self.laser_trans_sens = None
        self.laser_ref_sens = None
        self.volt_supply = None
        self.depth = None
        self.temperature = None
        self.date = dt.datetime(1900,1,1)
        self.total_vol_conc = None
        self.rh = None
        self.acc_xyz = [None] * 3
        self.raw_press = None
        self.ambient_light = None

        self._parse_source(source)

    def _parse_source(self, source):
        self._tmp = []
        with open(source) as src:
            for line in src:
                self._tmp.append(line.strip())

        if len(self._tmp) != 59:
            raise TypeError(_err_incorrect_length.format(len(self._tmp)))

        self._get_rings()
        self._get_aux_data()
        
    def _get_rings(self):
        self.counts = self._tmp[0:35]
        # TODO: convert to float

    def _get_aux_data(self):
        self.laser_trans_sens = self._tmp[36]
        self.laser_ref_sens = self._tmp[39]
        self.volt_supply = self._tmp[37]  # should divide by 100
        self.depth = self._tmp[40]
        self.temperature = self._tmp[41]
        self._get_datetime()
        self.total_vol_conc = self._tmp[50]
        self.rh = self._tmp[51]
        self.acc_xyz = self._tmp[52:55]
        self._get_pressure()
        self.ambient_light = self._tmp[57]

    def _get_datetime(self):
        pass

    def _get_pressure(self):
        pass






