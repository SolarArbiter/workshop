# Upload and Download Data

The Solar Forecast Arbiter allows users to upload and download data in JSON and CSV formats. Data may be uploaded manually using the dashboard (the focus of this exercise) or programmatically using the [API](https://api.solarforecastarbiter.org/).

## Upload

The upload data process is outlined in this [documentation](https://solarforecastarbiter.org/dashboarddoc/#upload-data). For this exercise, we recommend creating a new Site with new a 60-minute interval GHI Observation and Forecast so that you can use the data files linked to below.

View these sample [observation](observation_1h.csv?raw=true) and [forecast](forecast_1h.csv?raw=true) csv files, copy them into a plain text file or an Excel workbook, save the file in csv format, and then upload them to the dashboard. For observation data, a validation job will run after the observation data is uploaded. Reload the page after a few seconds to see the validation results. Compare the validation results to the raw data that you uploaded. Note that the  data is in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and the `Z` specifies UTC time zone. The data may be specified in time zone other than UTC, so long as it conforms to ISO 8601. See [this file](observation_1h_with_timezone.csv?raw=true) for an example.

The Solar Forecast Arbiter requires that points in the data files are consistent with the interval length of the observation or forecast metadata. Missing data may be specified with an empty value field, `NaN`, or `NULL`. View and upload this [example file](observation_1h_missing.csv?raw=true) to confirm that missing data is supported. Next, delete one row of the file so that there is a 2 hour interval between labels. The dashboard should reject the upload.

## Download

The download data process is also outlined in the [documentation](https://solarforecastarbiter.org/dashboarddoc/#download-data). Choose any observation or forecast that has data (as shown by the presence of a graph on its page). Click the *Download data* button. For example, here's a [link](https://dashboard.solarforecastarbiter.org/observations/9f657636-7e49-11e9-b77f-0a580a8003e9/download) to the download data page for the NREL MIDC OASIS GHI observation. Input the *start* and *end* date and time fields. For most observations, data is currently available from mid-May 2019 onward.

## Quality flags

The Solar Forecast Arbiter uses *quality flags* to keep track issues with data. Users may indicate that data is ok (`quality_flag=0`) or questionable (`quality_flag=1`) when uploading data. The Solar Forecast Arbiter validates the uploaded data and stores the results in the `quality_flag` field. We will provide mechanisms for users to convert the flags into human-readable format.
