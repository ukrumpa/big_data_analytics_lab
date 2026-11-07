# Week 4 — Apache Spark, DataFrames, SQL, Word Count and MLlib

This lab explores PySpark: loading and inspecting CSV data, DataFrame selection and aggregation, Spark SQL, word-frequency counting, and Random Forest regression on Melbourne housing data.

## Contents

- `scripts/week4_spark_exercises.py` — consolidated editable examples reconstructed from the report.
- `screenshots/` — 24 uploaded PNG figures, named `figure-02.png` through `figure-25.png`.

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

## Screenshots

![Figure 2](screenshots/figure-02.png)

![Figure 3](screenshots/figure-03.png)

![Figure 4](screenshots/figure-04.png)

![Figure 5](screenshots/figure-05.png)

![Figure 6](screenshots/figure-06.png)

![Figure 7](screenshots/figure-07.png)

![Figure 8](screenshots/figure-08.png)

![Figure 9](screenshots/figure-09.png)

![Figure 10](screenshots/figure-10.png)

![Figure 11](screenshots/figure-11.png)

![Figure 12](screenshots/figure-12.png)

![Figure 13](screenshots/figure-13.png)

![Figure 14](screenshots/figure-14.png)

![Figure 15](screenshots/figure-15.png)

![Figure 16](screenshots/figure-16.png)

![Figure 17](screenshots/figure-17.png)

![Figure 18](screenshots/figure-18.png)

![Figure 19](screenshots/figure-19.png)

![Figure 20](screenshots/figure-20.png)

![Figure 21](screenshots/figure-21.png)

![Figure 22](screenshots/figure-22.png)

![Figure 23](screenshots/figure-23.png)

![Figure 24](screenshots/figure-24.png)

![Figure 25](screenshots/figure-25.png)

