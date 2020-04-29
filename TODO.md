## Implementation notes
We will represent streams of records using [Python interators](https://docs.python.org/3/library/stdtypes.html#iterator-types) that produce dictionaries. 

Use [StringIO](https://docs.python.org/3/library/io.html#io.StringIO) to produce timestamped CSV data for testing



## TODO
Write some tests for BufferedIterator



## Modules
### dmerge module
Exposes functions for merging primary and secondary records

`dmerge(primary, auxiliares)` <br/>
Merges data from auxiliary records into the primary record. <br/>
Adds only properties that are not present in the primary record.
Interpolates values for additional numeric properties based on high-precision timestamp 


### timestamped-dstream module
Exposes functions that handle timestamped data streams. <br/>

`getAuxiliaries(primary)`
Returns a set of auxiliary records that correspond to given primary record. That set may be empty. <br/>
Auxiliaries also get "high-precision" timestamp, used for data interpolation by `dmerge` module

`getPrimaryStream`
Returns the stream of primary records, augmented with high-precision timestamp. <br/>
The ability to skip N initial lines in the actual source file also go here, probably.
