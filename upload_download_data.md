Upload and Download Data
========================

The Solar Forecast Arbiter allows users to upload and download data in JSON and CSV formats. Data may be uploaded manually using the dashboard (the focus of this exercise) or programmatically using the [API](https://dev-api.solarforecastarbiter.org/).

The upload data process is outlined in this [documentation](https://solarforecastarbiter.org/dashboarddoc/#upload-data). For this exercise, we recommend creating a new Site with new a 60-minute interval GHI Observation and Forecast. View these sample [observation](observation_1h.csv?raw=true) and [forecast](forecast_1h.csv?raw=true) csv files, copy them into a plain text file or an Excel workbook, save the file in csv format, and then upload them to the dashboard. A data validation job will run after the observation data is uploaded. Reload the page after a few seconds to see the validation results.

The download data process is also outlined in the [documentation](https://solarforecastarbiter.org/dashboarddoc/#download-data). Choose any observation or forecast from which to download data.
