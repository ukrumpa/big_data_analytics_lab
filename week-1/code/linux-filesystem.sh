#!/usr/bin/env bash
# Week 1: Exploring Linux filesystem commands.
# Run in a Linux terminal. Some listings depend on the current directory
# and your account permissions.

set -e

echo "Current directory:"
pwd

echo
echo "List files in the current directory:"
ls

echo
echo "Detailed listing:"
ls -l

echo
echo "Create a directory named myfile:"
mkdir -p myfile

echo
echo "Create/edit a text file (interactive editor):"
echo "Run this manually when you want to edit the file:"
echo "  nano myfile.txt"

echo
echo "Move one directory up:"
cd ..

echo
echo "List entries in the parent directory:"
ls
