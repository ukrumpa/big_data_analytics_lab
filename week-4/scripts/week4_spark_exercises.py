"""Consolidated PySpark exercises reconstructed from the Week 4 lab report.

Update all placeholder input paths before running with spark-submit.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc, explode, split
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder.appName("Week4-Spark-Lab").getOrCreate()

# Flight dataset: replace with the actual CSV path.
flightData2015 = (spark.read.option("inferSchema", "true")
                  .option("header", "true")
                  .csv("file:/path/to/flight-data.csv"))
flightData2015.show(20)

spark.conf.set("spark.sql.shuffle.partitions", "5")
flightData2015.select("DEST_COUNTRY_NAME", "count").show(50)
flightData2015.select(flightData2015.DEST_COUNTRY_NAME,
                      flightData2015["count"]).show(50)
(flightData2015.select("DEST_COUNTRY_NAME", "count")
 .groupBy("DEST_COUNTRY_NAME").sum("count").show(50))

flightData2015.createOrReplaceTempView("flight_data_2015")
spark.sql("""SELECT DEST_COUNTRY_NAME, sum(count)
             FROM flight_data_2015 GROUP BY DEST_COUNTRY_NAME""").show(50)
spark.sql("SELECT max(count) FROM flight_data_2015").show()
spark.sql("""SELECT DEST_COUNTRY_NAME, sum(count) AS destination_total
             FROM flight_data_2015 GROUP BY DEST_COUNTRY_NAME
             ORDER BY sum(count) DESC LIMIT 5""").show()
(flightData2015.select("DEST_COUNTRY_NAME", "count")
 .groupBy("DEST_COUNTRY_NAME").sum("count")
 .sort(desc("sum(count)")).limit(5).show())

# Word count: one text record per line.
textFile = spark.read.text("/path/to/input.txt")
wordCounts = (textFile.select(explode(split(textFile.value, r"\s+")).alias("word"))
              .groupBy("word").count())
wordCounts.show(50)

# Melbourne housing regression.
melbourne_data = (spark.read.option("inferSchema", "true")
                  .option("header", "true")
                  .csv("file:/path/to/melb_data.csv"))
print("Rows:", melbourne_data.count())  # report: 13,580
melbourne_data_clean = melbourne_data.dropna()
print("Rows after dropna:", melbourne_data_clean.count())

assembler = (VectorAssembler()
             .setInputCols(["Rooms", "Bathroom", "Landsize", "Latitude", "Longitude"])
             .setOutputCol("features"))
assembled = assembler.transform(melbourne_data_clean)
trainingData, testData = assembled.randomSplit([0.7, 0.3], seed=42)

rf = RandomForestRegressor(labelCol="Price", featuresCol="features")
model = rf.fit(trainingData)
predictions = model.transform(testData)
predictions.select("prediction", "Price").show()

evaluator = RegressionEvaluator(labelCol="Price",
                                predictionCol="prediction",
                                metricName="mae")
print("MAE:", evaluator.evaluate(predictions))
spark.stop()
