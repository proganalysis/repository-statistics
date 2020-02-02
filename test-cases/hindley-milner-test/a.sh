#!/bin/bash

for f in $(find . -name '*.py');
	do cat $f | grep TypeVar;
done

