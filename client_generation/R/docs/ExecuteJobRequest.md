# openlattice-rundeck::ExecuteJobRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argString** | **character** | Argument string to pass to the job, of the form &#x60;-opt value -opt2 value ...&#x60; | [optional] 
**loglevel** | **character** | Loglevel to use | [optional] 
**asUser** | **character** | A username identifying the user who ran the job. Requires &#x60;runAs&#x60; permission. | [optional] 
**filter** | **character** | A node filter string. | [optional] 
**runAtTime** | **character** | Specify a time to run the job (*API v18* or later). &#x60;ISO-8601&#x60; format with optional milliseconds. | [optional] 
**options** | **object** | Option value for option named &#x60;OPTNAME&#x60;. If specified the &#x60;argString&#x60; value is ignored (*API v18* or later). | [optional] 


