Reference Data
==============

The Solar Forecast Arbiter includes a set of reference irradiance and PV power data that all users may access. The image below shows a the status of the reference data set as of June 2019. Click [here](https://solarforecastarbiter.org/referencedata/) to access a zoomable map.

![reference data map](reference_data_map.png?raw=true =400x)

The data set includes the following networks:

* [NOAA SURFRAD](https://www.esrl.noaa.gov/gmd/grad/surfrad/)
* [NOAA SOLRAD](https://www.esrl.noaa.gov/gmd/grad/solrad/index.html)
* [NOAA CRN](https://www.ncdc.noaa.gov/crn/qcdatasets.html)
* [NREL MIDC](https://midcdmz.nrel.gov/)
* [U. Oregon SRML](http://solardat.uoregon.edu/)
* [DOE ARM](https://www.arm.gov/data)
* [Sandia RTC](https://pv-dashboard.sandia.gov/)

Parsers for most of these networks are available in [pvlib-python](https://pvlib-python.readthedocs.io/en/stable/api.html#io-tools).

The Solar Forecast Arbiter imports new reference data from each of these networks each night.

Recommended steps to explore the reference data:

1. Click [here](https://solarforecastarbiter.org/referencedata/) to access a zoomable map.
2. Visit [dev-dashboard.solarforecastarbiter.org/sites](https://dev-dashboard.solarforecastarbiter.org/sites/).
3. Type *reference* in the search bar to restrict the listed sites to the reference data set.
4. Click through sites from a few different providers. Hint: use the search bar to filter sites by name e.g. *surfrad* or *srml*. Be sure to visit the Observation page for each site to see the data available from that site. Note that all sites have GHI, but only some have DNI and DHI.
5. Select a *Sandia* site to view reference PV power data.
