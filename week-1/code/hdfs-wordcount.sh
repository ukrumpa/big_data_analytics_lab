#!/usr/bin/env bash
# Week 1: Upload Ubuntu-dialogue-corpus to HDFS and run Hadoop WordCount.
#
# Prerequisites:
# - Hadoop client configured and a reachable HDFS/YARN cluster
# - HADOOP_HOME set
# - Ubuntu-dialogue-corpus available in the current local directory
#
# Usage:
#   bash hdfs-wordcount.sh
#
# This follows the command sequence recorded in the Week 1 lab report.

set -euo pipefail

DATASET="${1:-Ubuntu-dialogue-corpus}"
OUTPUT_DIR="${2:-out}"
EXAMPLES_JAR="${HADOOP_HOME:?Set HADOOP_HOME}/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.2.jar"

if [[ ! -e "$DATASET" ]]; then
  echo "Dataset not found: $DATASET" >&2
  echo "Place Ubuntu-dialogue-corpus in this directory or pass its local path." >&2
  exit 1
fi

echo "HDFS users:"
hdfs dfs -ls /user

echo
echo "Upload dataset to HDFS:"
hdfs dfs -copyFromLocal "$DATASET"

echo
echo "Run Hadoop WordCount:"
hadoop jar "$EXAMPLES_JAR" wordcount "$DATASET" "$OUTPUT_DIR"

echo
echo "List output files:"
hdfs dfs -ls "$OUTPUT_DIR"

echo
echo "Display WordCount results:"
hdfs dfs -cat "$OUTPUT_DIR"/part-r-*

