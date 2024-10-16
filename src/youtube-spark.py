##work in progress code for docker execution connecting AWS S3 

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Read JSON from S3") \
    .config("spark.hadoop.fs.s3a.access.key", "YOUR_ACCESS_KEY") \
    .config("spark.hadoop.fs.s3a.secret.key", "YOUR_SECRET_KEY") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:4566") \
    .getOrCreate()

# Replace with your S3 bucket and file path
s3_path = "s3a://youtube-data-bucket/video_comments/Q4nbwea22jo.json"

# Read JSON file
df = spark.read.json(s3_path)

# Display the schema
df.printSchema()

# Show the first few rows
df.show()

# Perform transformations
transformed_df = df.select("column1", "column2").filter(df.column3 > 100)