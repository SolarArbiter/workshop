import numpy as np
import pandas as pd

from solarforecastarbiter import datamodel
from solarforecastarbiter import pvmodel

from pvlib.location import Location


# define metadata
modeling_params = datamodel.SingleAxisModelingParameters(
    ac_capacity=10, dc_capacity=14, temperature_coefficient=-0.004,
    dc_loss_factor=0, ac_loss_factor=0,
    axis_tilt=0, axis_azimuth=0, ground_coverage_ratio=.4,
    backtrack=True, max_rotation_angle=45)

metadata = datamodel.SolarPowerPlant(
    name='Boulder Power Plant', latitude=40., longitude=-105.,
    elevation=1650., timezone='America/Denver', provider='Sandia',
    modeling_parameters=modeling_params)

times = pd.date_range(
    start='20190801', end='20191001', freq='5min', closed='left')

solpos = pvmodel.calculate_solar_position(
    metadata.latitude, metadata.longitude, metadata.elevation, times)
cs = pvmodel.calculate_clearsky(
    metadata.latitude, metadata.longitude, metadata.elevation,
    solpos['apparent_zenith'])
ac_clear = pvmodel.irradiance_to_power(
    modeling_params, solpos['apparent_zenith'], solpos['azimuth'],
    cs['ghi'], cs['dni'], cs['dhi'])

ac_clear_1h = ac_clear.resample('1h').mean()
ac_clear_1h = pd.DataFrame({'value': ac_clear_1h, 'quality_flag': 0})
ac_clear_1h.to_csv('boulder_clear_aug_sept.csv', index_label='timestamp')

# make it cloudy, but apply clipping
random = np.random.random(size=len(times)) + 0.5
random = random.clip(max=1)
ac = ac_clear * random

ac_1h = ac.resample('1h').mean()
ac_1h = pd.DataFrame({'value': ac_1h, 'quality_flag': 0})
ac_1h.to_csv('boulder_cloudy_aug_sept.csv', index_label='timestamp')

fx_demo = ac_1h['value'].shift(1)
fx_demo.to_csv('boulder_fx_demo_aug_sept.csv',
               header=['value'], index_label='timestamp')

csi = ac / ac_clear
csi = csi.fillna(0)  # account for divide by 0
ac_csi = csi.shift(12) * ac_clear
holmgren_demo = ac_csi.resample('1h').mean()
holmgren_demo.to_csv('boulder_fx_holmgren_aug_sept.csv',
                     header=['value'], index_label='timestamp')
