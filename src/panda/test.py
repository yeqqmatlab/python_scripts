import pandas as pd
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("test").getOrCreate()
# 读取数据，数据位置‘hdfs://bd01:8020/a/b/part*.parquet’
df = spark.read.format('parquet').load('hdfs://ip243:8020/test/student_score_weekly')

df.printSchema()

df.createOrReplaceTempView("student_score_weekly")
df2 = spark.sql("select * from student_score_weekly where province_id = 14 and school_id = 1080 and class_id = '17536408539761141459' and exam_group_id = '594770208413478912' ")
df2.show()

# pandas_pd = df2.toPandas()

# print(pandas_pd.dtypes)

# print(pandas_pd['school_id'])

spark.stop()
