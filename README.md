# csvdata-merge
`csvdata-merge` is tool to merge timestamped data in CSV format into one (CSV) data stream. It was written to merge data from EI CGR-30P and CGR-30C airplane engine monitors, but it can probably be easily modified to work with other data.

The tool is written in Python and requires Python 3 to run.

## Usage
    python3 csvdata_merge [--skip-lines n] [--verbose] primary-file auxiliary-file

where

| Parameter | Description |
| :--- | :--------- |
| `primary-file` | The primary data file |
| `auxiliary-file` | The auxiliary data file |
| `--skip-lines <n>` | (optional) Number of lines to skip (in both files) before attempting to read data. |
| `--verbose` | (optional) Emits verbose output with additional diagnostic information. |

Both files are assumed to contain CSV-formatted data with first line of data being the header. The program will attempt to merge data in the auxiliary file into the primary file. This is done by comparing columns present in primary and auxiliary files, and then adding columns missing in the primary file, but present in the auxiliary file, into the primary file records. The merged records are then written (in CSV format) to standard output.

## How the program works
The program is matching records in the primary and auxiliary files by timestamp. For each record in the master file the closest two records (time-wise) in the auxiliary file are found. The data from these auxiliary record is then interpolated and merged into the master file record and the record is written to the output. This continues until there are no more records in the master file.

The maximum permissible time difference between the master file record and the merge candidate record (from auxiliary file) is one second. If no good merge candidate records are found, the auxiliary data is left empty.

### Timestamp format
The data in both files is assumed to have a timestamp as the first column. Currently the only supported format for the timestamp is `hh:mm:ss` (hour, minute, and second--one second resolution).

### Duplicate timestamps
Several records might have the same timestamp. If that is the case, the program will assume the observations are distributed uniformly within the time period defined by the timestamp. For example, let's say there are 3 records with timestamp `00:00:23`. Internally the program will assign the records the following timestamps: `00:00:23.00`, `00:00:23.33`, and `00:00:23.66`. This insures that, internally, every record has a unique timestamp 

## Developing and testing the program
### Prepare the repo for development
Create new run-time environment for the project (one-time operation):

    cd <repo root>
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

After this one-time setup is is enough just to activate the environment whenever you start working with it:

    cd <repo root>
    source env/bin/activate

After you are done with development just do

    deactivate

To deactivate the environment

### Testing the program

    python3 -m unittest discover ./tests '*.py'

## References
CSV file format spec: https://tools.ietf.org/html/rfc4180