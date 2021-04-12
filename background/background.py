_err_incorrect_length = 'Source file does not have the correct number of lines: {}'
import datetime as dt

class background:
    """Interpreter for the background files from the Sequoia LISST-200x.

    Files are in an ASCII format, each line representing one value (scientific notation).
    Each line ends with with 'comma\r\n':
        01-36 Raw ring values [counts],
        37 Laser transmission Sensor [counts],
        38 Supply voltage in cal. units [V*100],
        39 External Analog input 1 in cal. units [V*10000],
        40 Laser Reference sensor in cal. units [counts],
        41 Depth in cal. units [counts],
        42 Temperature in cal. units [counts],
        43-49 Y/M/D/H/M/S,
        49 External Analog input 2 in cal. units [V*10000],
        50 [NOT USED]Sauter Mean Diameter [uncal. units],
        51 Total Volume Concentration [uncal. units],
        52 Relative Humidity [%],
        53-56 Accelerometer X/Y/Z [counts],
        56-58 Raw pressure MSB/LSB,
        58 Ambient light [counts],
        59 [NOT USED]: 0.000000e+000,
        60 [NOT USED]: empty line
    Newer versions of the software use a comma instead of a point in the decimal notation (5,400000e+004 instead of 5.400000e+004)
    """
    
    def __init__(self, source):
        self.counts = []
        self.laser_trans_sens_counts = None
        self.laser_ref_sens_counts = None
        self.volt_supply_volt = None
        self.depth_counts = None
        self.temperature_degc = None
        self.datetime = dt.datetime(1900,1,1)
        self.total_vol_conc_uncal_counts = None
        self.rh_pct = None
        self.acc_xyz_counts = [None] * 3
        self.raw_press_noidea = None
        self.ambient_light_counts = None
        self._parse_source(source)

    def _parse_source(self, source):
        """Get data from the file"""
        self._tmp = []
        with open(source) as src:
            for line in src:
                line = line.strip()[:-1]  # get rid of EOL and last comma
                line = line.replace(',', '.')  # if there still is a comma, it is used as decimal point
                self._tmp.append(float(line))

        if len(self._tmp) != 59:
            raise TypeError(_err_incorrect_length.format(len(self._tmp)))

        self._get_rings()
        self._get_aux_data()
        
    def _get_rings(self):
        """First 36 values are ring counts"""
        self.counts = self._tmp[0:35]
        # TODO: convert to float

    def _get_aux_data(self):
        """Other values are auxillary data"""
        self.laser_trans_sens_counts = self._tmp[36]
        self.laser_ref_sens_counts = self._tmp[39]
        self.volt_supply_volt = self._tmp[37] / 100
        self.depth_counts = self._tmp[40]
        self.temperature_degc = self._tmp[41] / 1000
        self._get_datetime()
        self.total_vol_conc_uncal_counts = self._tmp[50]
        self.rh_pct = self._tmp[51]
        self.acc_xyz_counts = [i for i in self._tmp[52:55]]
        self._get_raw_pressure()
        self.ambient_light_counts = self._tmp[57]

    def _get_datetime(self):
        """Get date/time from 6 split lines/elements"""
        dt_temp = [int(i) for i in self._tmp[42:48]]
        self.datetime = dt.datetime(*dt_temp)

    def _get_raw_pressure(self):
        """ 
        According to datasheet: 56-58 Raw pressure MSB/LSB.
        No idea how to interpret this if values are floats.
        """
        pass






