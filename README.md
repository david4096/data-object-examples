# Data Object Examples

This repository implements a minimalistic static Data Object service by hosting JSON that can be accessed by URL.

## Creating demo JSON

The repository is organized to mimic a the Data Object Service schemas by offering 
Data Object JSON at the path `repobase/ga4gh/dos/v1/dataobjects/{data_object_id}`.

First, install requirements using `pip install -r requirements.txt` to download 
the DOS client.

To recreate these files, edit the `make_files.py` script to point at a Data Object 
Service you would like to query. Running the script will attempt to create
files for the Data Objects in the directory `ga4gh/dos/v1/dataobjects`.

## Making Requests against the Examples

Note that responses from github raw will not have their mime-type set correctly. 
However, a simple HTTP request should return a document that appears the same 
as the service used to originally generate it above:

```
curl https://raw.githubusercontent.com/david4096/data-object-examples/master/ga4gh/dos/v1/dataobjects/7a683716-cf63-4e9e-abb6-9d18853dc165
```

## Maintaining

To update this repository, delete the contents of `ga4gh/dos/v1/dataobjects` and 
modify `make_files` to point at a new service.

