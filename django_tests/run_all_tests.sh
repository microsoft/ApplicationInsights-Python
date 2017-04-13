#!/bin/bash

if [ -z $PYTHON ]; then
	PYTHON=$(which python)
fi

cd $(dirname $0)
BASEDIR=$(pwd)

# Django/python compatibility matrix...
if $PYTHON -c "import sys; sys.exit(0 if sys.version_info < (3, 0) else 1)"; then
	# Django2.0 won't support Python2
	DJANGO_VERSIONS='1.7.11 1.8.18 1.9.13 1.10.7 1.11'
elif $PYTHON -c "import sys; sys.exit(0 if sys.version_info < (3, 5) else 1)"; then
	DJANGO_VERSIONS='1.7.11 1.8.18 1.9.13 1.10.7 1.11'
else
	# python3.5 dropped html.parser.HtmlParserError versions older than Django1.8 won't work
	DJANGO_VERSIONS='1.8.18 1.9.13 1.10.7 1.11'
fi

# For each Django version...
for v in $DJANGO_VERSIONS
do
	echo ""
	echo "***"
	echo "*** Running tests for Django $v"
	echo "***"
	echo ""

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
