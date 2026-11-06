# Week 1 Results

Source: the uploaded `Week_1_Lab_Report.docx` (11 pages), particularly the Linux command output on pages 2–3 and HDFS/MapReduce output on pages 4–11.

## 1. Linux filesystem

The report records these commands and observations:

| Command | Purpose / recorded result |
|---|---|
| `ls` | Lists entries in the current directory. Sample entries: `bin`, `lib64`, `sbin`, `lib`, `tmp`. |
| `ls -l` | Displays detailed file metadata. Example: `dr-xr-xr-x. 2 root root 6 Nov 3 2024 afs`. |
| `mkdir myfile` | Creates a directory named `myfile`. |
| `nano myfile.txt` | Opens a terminal text editor to create/edit a file. |
| `cd ..` | Moves to the parent directory. |
| `ls` | Lists directories in the parent directory; the report notes that names such as `up2545416` refer to user accounts. |

The report explains the `afs` listing as a directory owned by `root`, with read/execute permissions for owner, group, and others. Its displayed link count is 2 and displayed size is 6.

## 2. HDFS and MapReduce WordCount

The report documents this workflow:

1. `hdfs dfs -ls /user` — list HDFS user directories.
2. `hdfs dfs -copyFromLocal Ubuntu-dialogue-corpus` — upload the local corpus to HDFS.
3. `hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.2.jar wordcount Ubuntu-dialogue-corpus out` — run the Hadoop example WordCount job.
4. `hdfs dfs -ls out` — inspect output files.
5. `hdfs dfs -cat out/part-r-0000` — display the reducer output.

### Job completion

The report records:

```text
map 100% reduce 100%
Job job_1769600642415_0055 completed successfully
```

The output directory contained:

```text
out/_SUCCESS
out/part-r-0000
```

The report identifies `_SUCCESS` as the job completion marker and `part-r-0000` as the result file.

### Sample word counts

These are the three sample rows transcribed in the report (page 7):

| Word | Count |
|---|---:|
| `ctionParsni` | 1 |
| `radley` | 2 |
| `onkeyHote` | 4 |

The report also includes terminal screenshots of the full output (Figures 7–10, pages 8–11). The complete reducer output is not available as selectable text in the report, so only the three explicitly transcribed sample rows are reproduced here.

## 3. Important reproducibility note

These are results captured in the submitted lab report, not a new execution in this environment. The original corpus is not included in this repository, and the scripts require a configured Hadoop cluster. The original report includes screenshots of the terminal outputs and should be retained alongside this summary if the source document is added separately.
