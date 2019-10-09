# DC data sharing

## Creating Sites, Observations, Forecasts

* Create a Site (weather station)
  * Boulder: 40 N, -105 E, 1650 m
* Create a Site (power plant)
  * Boulder Power Plant: 10 MW AC, 14 MW DC, tracking, .4 gcr
* Create an Observation.
  * AC power, hourly average, beginning
* View sample data, upload boulder_cloudy_aug_sept.csv
  * Note: procedure must be repeated for each variable. Tedious, but avoids need to agree upon and parse column names
* Create a Forecast
  * AC power, hourly average, beginning
* upload boulder_fx_demo_aug_sept.csv

## Data sharing

For this exercise you need two accounts. Here we use demo and holmgren.
For now we must use uuids to share data, but email support will come soon.

* demo: 4f738239-e632-11e9-ab45-52540015d5ce
* holmgren: 26653f79-e62d-11e9-ab45-52540015d5ce

* Goal: demo@solarforecastarbiter.org wants to share its AC power data with a forecast provider (holmgren@email.arizona.edu), receive a forecast from the forecast provider, and generate a report comparing to its own forecast (created previously).
* Show roles page
* In a second incognito window, log in as holmgren@email.arizona.edu, show available sites -- cannot see demo’s
* From demo window, create role for sharing sites, obs metadata, values
* Use “all *” permissions for simplicity, but note this can be made much more fine grained
* Assign role to forecast provider account
* From holmgren window, create forecast, upload forecast
  * AC power, hourly average, beginning
  * upload boulder_fx_holmgren_aug_sept.csv
* Note that demo could have created a forecast metadata object
* Share new holmgren forecast metadata and data with the demo account
* From demo account, see that there is now a new forecast
* From demo create report comparing demo forecast and holmgren forecast to demo obs

## Data sharing on MIDC Arizona OASIS

* From holmgren window, create OASIS forecast, upload forecast
  * issue time of day 7Z, run length 1 day, lead time 1 day
* Premade uploaded forecast is a bias corrected version of GFS forecast
* Note that demo could have created a forecast metadata object
* If not already done, share new holmgren forecast metadata and data with the demo account
* From demo account, see that there is now a new forecast
* Create report comparing reference forecast and holmgren forecast to reference obs
