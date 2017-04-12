#!/bin/bash

if [ -z $PYTHON ]; then
	PYTHON=$(which python)
fi

cd $(dirname $0)
BASEDIR=$(pwd)

# For each Django version...
for v in 1.8.18 1.9.13 1.10.7 1.11
do
	echo "*** Running tests for Django $v"
	# Create new directory
	TMPDIR=$(mktemp -d)
	function cleanup
	{
		rm -rf $TMPDIR
		exit $1
	}
	
	trap cleanup EXIT SIGINT
	
	# Create virtual environment
	virtualenv -p $PYTHON $TMPDIR/env
	
	# Install Django version + application insights
	. $TMPDIR/env/bin/activate
	pip install Django==$v || exit $?
	cd $BASEDIR/..
	python setup.py install || exit $?
	
	# Run tests
	cd $BASEDIR
	bash ./run_test.sh || exit $?
	
	# Remove venv
	deactivate
	rm -rf $TMPDIR
done
