#!/bin/bash

for f in $(find * -name '*.py-stripped.py');
	do pytype $f; merge-pyi $f ".pytype/pyi/${f}i" > "${f%.py-stripped.py}-gen.py"
done

