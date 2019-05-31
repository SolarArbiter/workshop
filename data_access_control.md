# View Data Access Controls

The Solar Forecast Arbiter uses roles and permissions to control access to data and resources within the system.
At this time users are only allowed to view roles and permissions but not edit or create them. In this excersise
you will inspect three users' access controls and how it affects the data available to them.


A permission defines an action that can be made on an resource or group of resources, e.g. 'create a site' or
'read forecast forecast A'. A role is a collection of permissions that can be assigned to a user. A user can
be assigned multiple roles.

Here we use the following scenario to demonstrate how data access controls function in the Solar Forecast Arbiter.

A utility company, _Utility X_ has a power plant, Plant X with some irradiance and power measurements. They want
to share Site information and measurements with _Forecaster A_ and _Forecaster B_.
Forecasters A and B want to provide power forecasts for Power Plant X that are only visible to their own users
and to users in Utility X. The forecasters have also made forecasts for a site, 'Ashland OR', which is not visible
to Utility X or to the other forecaster.

You may log in to the [Solar Forecast Arbiter Dashboard](https://dev-dashboard.solarforecastarbiter.org) as any of these users
to view the data they have access to and the roles and permissions on their account. Credentials for each user are found in the 
table below.

|Email                                 | Password          |
|--------------------------------------|-------------------|
|utilityx@solarforecastarbiter.org     |Utilitypassword!   |
|forecastera@solarforecastarbiter.org  |Forecasterpassword!|
|forecasterb@solarforecastarbiter.org  |Forecasterpassword!|


These excersizes will walk you through accessing the set of permissions necessary to accomplish the interaction between
Utility X and Forecasters A and B described above.


## View the data available to Utility X
Log into the dashboard as Utility X and follow the _Sites_ link to view the list of Sites available to you. Here, you 
should see a site 'Power Plant X' provided by 'Utility X'.

Click on the site and view its observations and forecasts. You will notice that all observations are provided by
Utility X, but there are two hour ahead AC power forecasts one provided by each forecaster.

## View the roles and permissions of Utility X 
The following steps guide you in how to view the roles of the 'Utility X' user.

1. Click on the "Account" button in the top right corner and select "User Administration" 
2. Click on the "Users" link in at the top of the page.
3. Click on the User ID field in the table, there should only be one user in the table.

### The User Page
This page shows some information about the user, `utilityx@solarforecastarbiter.org`, as well as
listing the roles they are assigned. Notice the 'Read Forecaster A Plant X Forecast' role and its
organization. 
This is a role granted by Forecaster A to read the values and metadata of the forecast they have provided
for the site 'Power Plant X'. There is also a similar role granted to the user from Forecaster B. The
'Utility X' role grants the user access to all of the resources in this organization.

### The Role Page
Click on the 'Read Forecaster A Plant X Forecast' role. The role page will display information about the role
and a list of permissions it grants. Notice that this particular role contains only read permissions. These read
permissions allow the user at Utility X to access the Single forecast made by Forecaster A at Power Plant X.

  - The 'Read Forecaster A plant x forecast metadata' permission allows read access to the metadata of the forecast
provided by Forecaster A. The metadata of a forecast is defined in the Forecasts section of the
[Data Model](https://solarforecastarbiter.org/datamodel/#forecasts) document.


  - The 'Read Forecaster A plant x forecast values' allows reading the values of the forecast made by Forecaster A
at Power Plant X.

  - The permissions 'Read Forecaster A plant role' and 'Read Forecaster A Plant permissions' make the role and
its permissions visible to the user it is assigned to. Usually only administrators may view or edit roles, but for
the purposes of this demonstration, each role contains permissions to view the role itself, and the permissions
it allows.
