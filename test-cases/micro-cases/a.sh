#!/bin/bash

for f in $(find . -name '*.py-stripped.py');
	do cat $f | grep TypeVar;
done

