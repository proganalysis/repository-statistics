## Tools Overview

#### `compare.py`

This tool will compare two files (one is handwritten types & the other is generated) and produce statistics on how many types are correct

Usage: `python3 compare.py <file1> <file2>`


#### `copy-typed.py`

This tool will read in from `data/typed-repos-org` and copy all of the repos with types in it from one folder to a new one

Usage: `python3 ./copy-typed <all-repos> <new-folder>`


#### `gentypes.py`

This tool will generate the typed files using pytype and retype and put them in `typed-src` in the folder associated

Usage: `Usage: python3 ./gentypes <repo-folder>`


#### `repo-generator.py`

This tool will generate a list of typed repos in the specified folder

Usage: `python3 ./repo-generator <repo-folder>`


#### `strip-types.py`

This tool will strip out types in each python file and write the new untyped file

Usage: `python3 ./strip-types <repo-folder>`