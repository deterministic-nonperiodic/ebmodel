from numpy import pi

# extracted from climlab:
cp = 1004.       # specific heat at constant pressure for dry air (J / kg / K)
Rd = 287.        # gas constant for dry air (J / kg / K)
kappa = Rd / cp
Rv = 461.5       # gas constant for water vapor (J / kg / K)
cpv = 1875.      # specific heat at constant pressure for water vapor (J / kg / K)
eps = Rd / Rv
kBoltzmann = 1.3806488E-23  # the Boltzmann constant (J / K)
c_light = 2.99792458E8      # speed of light (m/s)
hPlanck = 6.62606957E-34    # Planck's constant (J s)

#  Stefan-Boltzmann constant (W / m**2 / K**4)
sigma = (2*pi**5 * kBoltzmann**4) / (15 * c_light**2 * hPlanck**3)

# default parameters:
kratio = 3.81    # (W m-2 C**(-1))
S0 = 1365.2      # solar constant (W / m**2)
emss = 0.6       # atmosphere emissivity

# effective emiss. * Stefan-Boltzmann constant
olr_cns = (1.0 - 0.5*emss) * sigma 

rho_w = 1028.   # density of water (kg / m**3)
cw = 4181.3     # specific heat of liquid water (J / kg / K)
hl = 10.0       # characteristic depth for Ts

CtoK = 273.1592 # 0degC in Kelvin
KtoC = -CtoK    # 0 K in degC

tau = hl * rho_w * cw # time scale

#  Some useful time conversion factors
seconds_per_minute = 60.
minutes_per_hour = 60.
hours_per_day = 24.
days_per_year = 365.2422
seconds_per_hour = minutes_per_hour * seconds_per_minute
minutes_per_day = hours_per_day * minutes_per_hour
seconds_per_day = hours_per_day * seconds_per_hour
seconds_per_year = seconds_per_day * days_per_year