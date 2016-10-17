"""
'Earth is shaking'

Monty   >> "OMG AN EARTHQUAKE"
You     >> "Duck!!"

'House crashes down'

Monty   >> "Where on earth did that come from?"
You     >> "I don't know yet Monty, but we'd better find out."

'Synchronous evil laughter'

First, let's determine how far away the earthquake was.
    1. Obtain P- and S-wave arrival times from three locations.
    2. Calculate the difference between P- and S-wave arrival times at each location (seconds).
    3. Use the difference in arrival time to determine distance (in km) from the earthquake at each location.

Let's also determine the earthquake's magnitude (Richter scale):
    4. Determine the amplitude of the strongest wave (mm).
    5. Use the difference in arrival time and the amplitude to determine the magnitude of the earthquake.

Now, let's locate the epicenter:
    6. Draw radius around each location using the distance found in 3.
    7. Determine where the 3 circles intersect.

** reminder, GPS N and E are +, S and W are -
*** advanced option: write program that analyzes the seismograms for you, determines p- and s-wave arrival times and amplitude of strongest wave.

station_event = (p-wave, s-wave, max_amp, (latitude, longitude))

>>> station1 = ('08:00:00', '08:00:50', (eureka, ca))
>>> station2 = ('08:00:00', '08:01:12', (elko, nv))
>>> station3 = ('08:00:00', '08:01:04', (Vegas))

where
d = distance to earthquake
tS = S-wave arrival time
tP = P-wave ""
vS = velocity of S-wave
vP = velocity of p-wave

d = (tS-tP/(1/vS-1/vP)

"""

from datetime import datetime
from math import log, exp


class SeismicStation:
    def __init__(self, name, coords):
        self.name = name
        self.latitude = coords[0]
        self.longitude = coords[1]
        self.events = list()

    def add_event(self, event):
        self.events.append(event)
        return self

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class StationEvent:
    """
    An object pertaining to a single seismic event at a single seismic recording
    station.
    """
    VS = float(3.67) # avg velocity of s-waves in CA crustal rocks (km/sec)
    VP = float(6.34) # avg velocity of p-waves in CA crustal rocks (km/sec)
    Vsp = (VS * VP)/(VP - VS) # your conversion factor from arrival time difference (sec) to distance (km)

    def __init__(self, p_arrival_time, s_arrival_time, max_amplitude):
        p_time = datetime.strptime('%H:%M:%S', p_arrival_time)
        s_time = datetime.strptime('%H:%M:%S', s_arrival_time)
        delta = s_time - p_time

        self.p_arrival_time = p_time
        self.s_arrival_time = s_time
        self.delta_sec = delta.seconds
        self.max_amplitude = max_amplitude # in mm
        # Method resolution order below
        self.dist_to_eq = None
        self.magnitude = None
        self.seismic_moment = None
        self.energy = None

    def __str__(self):
        message = "{} | Tsp(s): {}, Amp(mm): {}"
        return message.format(self.p_time, self.delta_sec, self.max_amplitude)

    def __repr__(self):
        message = "{} | Tsp(s): {}, Amp(mm): {}"
        return message.format(self.p_time, self.delta_sec, self.max_amplitude)

    def calc_distance(self):
        """
        Calculates the distance from the epicenter of the earthquake from
        one seismic station. Using assumption of average velocity in California
        crustal rocks for Vsp. (adaptable for location of stations or earthquake)
        """
        self.dist_to_eq = self.delta_sec * Vsp # distance in km
        return self.dist_to_eq


    def calc_magnitude(self):
        """
        Calculates the magnitude of the Earthquake on the Richter Scale.
        source: http://crack.seismo.unr.edu/ftp/pub/louie/class/100/magnitude.html
        """
        result = log(self.max_amplitude) + (3*log(8*self.delta_sec)-2.92)
        self.magnitude = result
        return self.magnitude # richter scale 1 - 5

    def calc_seismic_moment(self):
        """
        Calculates the seismic moment (dyne-cm) of the earthquake based upon relationship
        with Magnitude. source: https://goo.gl/lLpS9x
        """
        result = 10 ** ((3/2)*(self.magnitude+16))
        self.seismic_moment = result
        return self.seismic_moment # in units of dyne-cm

    def calc_seismic_energy(self, method='moment'):
        """
        Calculates the amount of Energy (ergs) released by the earthquake, based on
        either the magnitude or the seismic moment.
        """
        if method == 'magnitude':
            """ E = 10 ^ (11.8 + (1.5 * Magnitude)) """
            result = 10 ** (11.8+(1.5*self.magnitude))

        elif method == 'moment':
            """ E = Moment / 20,000 """
            result = self.seismic_moment / 20000

        else:
            print("Error, available methods are 'moment' or 'magnitude'.")
            result = None

        self.energy = result
        return self.energy

    def print_report(self):
        """
        Prints out the results. :)
        """
        message = 'The difference between p- and s-wave arrival times was: {} seconds.\
                   \nThe distance to the earthquake is {} kilometers.'
        print(message.format(self.delta_sec, self.dist_to_eq)


class Earthquake:
    """
    Compiles data from at least three seismic station events to determine
    the epicenter of the earthquake!!!
    """

    def __init__(self, ): # takes other things...
    pass
