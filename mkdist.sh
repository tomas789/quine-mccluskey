#!/bin/sh
set -e

name=`python setup.py --name`
version=`python setup.py --version`
archive="$name-v$version"

git archive --format=tar --prefix="$archive/" HEAD | tar x
rm -f "$archive/$0"

tar cvzf "$archive.tar.gz" "$archive"
zip "$archive.zip" `find "$archive"`
rm -rf "$archive"