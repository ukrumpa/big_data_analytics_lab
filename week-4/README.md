# Week 4 — Apache Spark, DataFrames, SQL, Word Count and MLlib

This lab explores PySpark: loading and inspecting CSV data, DataFrame selection and aggregation, Spark SQL, word-frequency counting, and Random Forest regression on Melbourne housing data.

## Contents

- `scripts/week4_spark_exercises.py` — consolidated editable examples reconstructed from the report.
- `screenshots/` — 25 original PNG figures extracted from the DOCX report. Figure numbering is described in the report; image files retain their source media numbering.

## 1. Flight data and DataFrame operations

The report loads a flight CSV with `header=true` and `inferSchema=true`, inspects rows with `.show()`, and sets `spark.sql.shuffle.partitions` to 5. It selects `DEST_COUNTRY_NAME` and `count`, groups by destination, and sums counts.

## 2. Spark SQL and top destinations

A temporary view named `flight_data_2015` is created. SQL queries repeat the grouped aggregation, find the maximum count, and select the top five destination countries. The same top-five aggregation is also performed with the DataFrame API.

## 3. Word count

The report reads a text file, splits lines on whitespace, expands the words into rows using `explode`, groups by `word`, and counts occurrences.

## 4. Melbourne housing regression

The report loads `melb_data.csv` and records 13,580 rows before cleaning. It removes null rows with `dropna`, assembles Rooms, Bathroom, Landsize, Latitude and Longitude into a feature vector, and splits the data 70/30. A `RandomForestRegressor` predicts `Price`.

Reported example: prediction 473,328.34 versus actual 470,000; reported test MAE 284,496.13. These are results stated in the report, not a fresh execution.

## Run

Install/configure Spark and PySpark, update the placeholder dataset paths in `scripts/week4_spark_exercises.py`, then run:

```bash
spark-submit scripts/week4_spark_exercises.py
```

The source datasets are not included. The script consolidates the report's examples into one sequence; run sections independently if input schemas or paths differ. The 70/30 split uses a fixed seed for reproducibility, so results may differ from the report.
