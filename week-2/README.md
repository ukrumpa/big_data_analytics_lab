# Week 2 — MapReduce with `mrjob`

This lab report demonstrates two MapReduce programs using Python's `mrjob` package: a Unix-style character/word/line counter and a word-frequency counter. It then runs the word-frequency job locally and on a Hadoop cluster.

## Repository contents

- `scripts/mr_unix_wc.py` — counts characters, words, and lines.
- `scripts/mr_word_count.py` — counts occurrences of alphabetic words.
- `screenshots/` — the 14 original report figures, in report order.

## 1. Environment setup

The report activates the `jhub-ml` Conda environment and creates `mr_unix_wc.py` with `nano`. See [Figure 1](screenshots/environment-setup.png).

```bash
conda activate jhub-ml
nano mr_unix_wc.py
```

## 2. Unix `wc`-style MapReduce job

The mapper emits three key-value pairs for each input line: character count, word count, and line count. The reducer sums values for each key.

See [Figure 2](screenshots/mr-unix-word-count-code.png) for the code in the report. The report uses *The Owl and the Pussy-Cat* by Edward Lear as `poem.txt` input ([Figure 3](screenshots/poem-input-owl-and-pussycat.png)).

Run locally:

```bash
python mr_unix_wc.py poem.txt
```

Recorded output:

| Measure | Result |
|---|---:|
| Characters | 1267 |
| Lines | 42 |
| Words | 242 |

The recorded terminal output is in [Figure 4](screenshots/unix-wc-count-results.png).

## 3. Word-frequency MapReduce job

The second program uses the regular expression `r"[a-zA-Z]+"` to extract alphabetic words. The mapper emits `(word, 1)` and the reducer sums each word's occurrences.

See [Figure 5](screenshots/word-frequency-count-code.png). The report runs:

```bash
python mr_word_count.py poem.txt
```

The local word-frequency output is captured across [Figures 6–8](screenshots/local-word-count-output-a.png), [Figure 7](screenshots/local-word-count-output-b.png), and [Figure 8](screenshots/local-word-count-output-c.png).

## 4. Run the word-count job on Hadoop

The report copies the `Ubuntu-dialogue-corpus` dataset into HDFS, then submits the `mrjob` word-count job to Hadoop:

```bash
hdfs dfs -copyFromLocal Ubuntu-dialogue-corpus

python mr_word_count.py -r hadoop \
  -o hdfs:///user/up2542055/out \
  hdfs:///user/up2542055/Ubuntu-dialogue-corpus
```

The report describes the input being split into 12 chunks and processed in parallel. The job progress and completion output are shown in [Figures 9–11](screenshots/hadoop-wordcount-progress.png), [Figure 10](screenshots/hadoop-wordcount-job-summary.png), and [Figure 11](screenshots/hadoop-wordcount-framework-details.png).

## 5. Run with five reducers

The report removes the existing output directory before rerunning the job, because Hadoop does not overwrite an existing output directory:

```bash
hdfs dfs -rm -r out

python mr_word_count.py -r hadoop \
  -o hdfs:///user/up2542055/out \
  hdfs:///user/up2542055/Ubuntu-dialogue-corpus \
  -D mapred.reduce.tasks=5
```

The `-D mapred.reduce.tasks=5` option configures five reducer tasks. The report's second Hadoop run is documented in [Figures 12–14](screenshots/hadoop-five-reducers-progress.png), [Figure 13](screenshots/hadoop-five-reducers-summary.png), and [Figure 14](screenshots/hadoop-five-reducers-final-output.png).

## Reproducing the lab

The screenshots are evidence from the submitted report, not a fresh execution here. To reproduce the work, use an environment with Python, `mrjob`, Conda environment `jhub-ml`, and access to a configured Hadoop/HDFS cluster. The report does not include the full `poem.txt` or `Ubuntu-dialogue-corpus` source datasets; supply those inputs separately. Update the HDFS username/path if your cluster account differs from `up2542055`.
