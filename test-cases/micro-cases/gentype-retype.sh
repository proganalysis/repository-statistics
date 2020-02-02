#!/bin/bash

for f in $(find . -name '*.py-stripped.py');
	do pytype $f; retype -i -a -p .pytype/pyi $f;
done

