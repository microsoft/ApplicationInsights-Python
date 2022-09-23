#!/bin/sh

# This script builds wheels for the API, SDK, and extension packages in the
# dist/ dir, to be uploaded to PyPI.

set -ev

# Get the latest versions of packaging tools
python -m pip install --upgrade pip build setuptools wheel

BASEDIR=$(dirname $(readlink -f $(dirname $0)))
DISTDIR=dist

(
  cd $BASEDIR
  mkdir -p $DISTDIR
  rm -rf $DISTDIR/*

 for d in azure-monitor-opentelemetry-distro; do
   (
     echo "building $d"
     cd "$d"
     # Package distribution in dist folder
    python setup.py sdist --dist-dir "$BASEDIR/dist/" clean --all
   )
 done
 # Build a wheel for each source distribution
 (
   cd $DISTDIR
   for x in *.tar.gz ; do
     pip wheel --no-deps $x
   done
 )
)
