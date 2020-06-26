# openlattice_rundeck::LogStorage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **character** | True if plugin is configured | [optional] 
**pluginName** | **character** | Name of the configured plugin | [optional] 
**succeededCount** | **numeric** | Number of successful storage requests | [optional] 
**failedCount** | **numeric** | Number of failed storage requests | [optional] 
**queuedCount** | **numeric** | Number of queued storage requests | [optional] 
**totalCount** | **numeric** | Total number of storage requests (currently queued plus previously processed) | [optional] 
**incompleteCount** | **numeric** | Number of storage requests which have not completed successfully | [optional] 
**missingCount** | **numeric** | Number of executions for this cluster node which have no associated storage requests | [optional] 


