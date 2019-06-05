# View Data Access Controls

The Solar Forecast Arbiter uses roles and permissions to control access to data and metadata within the system.
At this time users are allowed to view roles and permissions but not edit or create them. In this exercise
you will inspect three users' access controls and how they affect the data available to them.

A _permission_ defines an action that can be made on an resource or group of resources, e.g. 'create a site' or
'read forecast A'. A _role_ is a collection of permissions that can be assigned to a user. A user can
be assigned multiple roles.

Here we use the following scenario to demonstrate how permissions and roles enable data access control in the
Solar Forecast Arbiter.

A utility company, _Utility X_, has a power plant, _Power Plant X_, with some irradiance and power observations. They want
to share site metadata and observations with _Forecaster A_ and _Forecaster B_.
Forecasters A and B want to provide power forecasts for Power Plant X that are only visible to their own users
and to users in Utility X. Both forecasters have also created a forecast at the site 'Weather Station'. These forecasts
are only visible to the Forecaster that created them.

You may log in to the [Solar Forecast Arbiter Dashboard](https://dashboard.solarforecastarbiter.org) as any of these users
to view the data they have access to and the roles and permissions on their account. Credentials for each user are found in the
table below. If you are currently logged in as another user, click **Account** in the upper right corner of the page and then
select **Log out**.

|Email                                 | Password          |
|--------------------------------------|-------------------|
|utilityx@solarforecastarbiter.org     |Utilitypassword!   |
|forecastera@solarforecastarbiter.org  |Forecasterpassword!|
|forecasterb@solarforecastarbiter.org  |Forecasterpassword!|


These exercises will walk you through accessing the set of permissions necessary to accomplish the interaction between
Utility X and Forecasters A and B described above.

## View the data available to Utility X

Log in to the dashboard as Utility X and follow the _Sites_ link to view the list of sites available to you. Filter
out reference data by clicking on the Provider header of the table and unchecking the Reference box. You should
see the sites Power Plant X provided by Utility X and Weather Station provided by Organization 1.

Click on Power Plant X and view its observations and forecasts (click the Observations and Forecasts links above the
metadata table). You will notice that all observations are provided by
Utility X. There should be one hour ahead AC Power forecast provided by each forecaster. Utility X can see these forecasts
because Forecaster A and Forecaster B each assigned a role to Utility X that grants the user permission to view these forecasts.
The forecasters could revoke the roles and Utility X would no longer be able to view the data.

Return to the sites page and click on Weather Station (filter the Provider list or use the search bar). You should only
see observations and no forecasts at this site. As we'll see below, both Forecasters have created forecasts at this site,
but have not given Utility X access to view them.

## View the roles and permissions of Utility X
Follow these steps to view the roles of the Utility X user:

1. Click on the "Account" button in the top right corner and select "User Administration"
2. Click on the "Users" link in at the top of the page.
3. Click on the User ID field in the table.

### The User Page
This page shows information about the user Utility X and lists the roles they are assigned. Notice
the _Read Forecaster A Plant X Forecast_ role and its organization.
This is a role granted by Forecaster A to read the values and metadata of the forecast they have provided
for the site Power Plant X. There is also a similar role granted to the user from Forecaster B. The
Utility X role grants the user access to all of the resources in the Utility X organization.

### The Role Page
Click on the _Read Forecaster A Plant X Forecast_ role. The role page displays information about the role
and a list of permissions it grants. Notice that this particular role contains only read permissions. These read
permissions allow the user at Utility X to access the single forecast made by Forecaster A at Power Plant X:

  - The _Read Forecaster A plant x forecast metadata_ permission allows read access to the metadata of the forecast
provided by Forecaster A.
  - The _Read Forecaster A plant x forecast values_ allows reading the values of the forecast made by Forecaster A
at Power Plant X.
  - The permissions _Read Forecaster A plant role_ and _Read Forecaster A Plant permissions_ make the role and
its permissions visible to the user it is assigned to. Usually only administrators may view or edit roles, but for
the purposes of this demonstration, each role contains permissions to view the role itself, and the permissions
it allows.

## View the data available to Forecaster A or B
Log in to the dashboard as Forecaster A and follow the Sites link to view the list of sites available to you. Filter
out reference data by clicking on the Provider header of the table and unchecking the Reference box.
You should see the sites Power Plant X provided by Utility X and Weather Station provided by Organization 1.

Click on Power Plant X. Here you'll find the irradiance and power observations provided by Utility X. Notice
that the only visible forecast objects are provided by Forecast Provider A. Unlike Utility X, you will not be
able to see the forecast provided by Forecaster B because Forecaster A has not been assigned a role with
permission to read that data.

Return to the site listing and click on Weather Station. You will find irradiance observations provided by
Organization 1 and a day ahead GHI forecast from Forecast Provider A.

Logging in as Forecaster B will yield all of the same observation and site information, but only forecasts from
Forecast Provider B will be visible. The two Forecasters have not granted any read permissions to one another
and cannot view each other's data. Creating new Sites, Forecasts, and Observations will result in a resource
only visible to the user that created it.

## View the roles and permissions of Forecaster A or B
Access the User Administration page through the Account menu as in the Utility X permission section above. The
following instructions are the same for Forecaster A or B, save for roles allowing each Forecaster to access their
own data.

### The User Page
Click on the User ID field of the users table to view Forecaster A's user information. Notice the Read Plant X role from
organization Utility X. This role grants the forecaster access to Power Plant X and the observation data associated
with it. There is also a 'Forecaster A' role that allows the user access to data in its own organization.

### The Role Page
Click on the Read Plant X role. On this role page you can see the permissions granted to Forecaster A by Utility X. In this
case the utility has created a single role to apply to both forecasters. Notice the following read permissions:

  - The _Read Plant X observation metadata_ permission grants the forecaster permission to access metadata about an
observation. The metadata of an observation is defined in the
[Observations section of the Data Model](https://solarforecastarbiter.org/datamodel/#observations) document.
  - The _Read Plant X observation values_ permission allows reading values of the observations made by Utility X at Power
Plant X.
  - The _Read Plant X site metadata_ permission allows the forecaster to read the site's metadata. Site metadata is defined
in the [Site section of the Data Model](https://solarforecastarbiter.org/datamodel/#site) document.
  - Again, the other permissions allow the Forecast user to view the role and permissions, as these permissions are usually
reserved for administrators.

### The Permission Page
Click on the 'Read Plant X observation values' permission. The permission page shows some information about the permission
as well as listing the objects that it allows its action on. In this case, all of the observations made by Utility X at Power
Plant X are listed. If Utility X no longer wanted to share data from a portion of these observations, they would simply need
to remove those observations from the permissions. Support for editing roles and permissions through the dashboard will be
implemented soon.
