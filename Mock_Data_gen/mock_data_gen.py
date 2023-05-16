import pyspark,random
from pyspark.sql import *
from pyspark.sql.functions import *
from faker import Faker


spark = SparkSession.builder.master("local") \
                    .appName('session_test') \
                    .getOrCreate()

fake = Faker(['en_IN'])

def get_gender():
    return random.choice(['Male','Female'])
get_gender = udf(get_gender,StringType())

def gen_first_name(gender):
    if gender == 'Male':
        return fake.first_name_male()
    else:
        return fake.first_name_female()
gen_first_name = udf(gen_first_name,StringType())

def gen_last_name():
    return fake.last_name()
gen_last_name = udf(gen_last_name,StringType())


def gen_phone(id):
    return str(random.randint(70000,99000)) + str(int(id) + 500000)
gen_phone = udf(gen_phone,StringType())

def gen_email(first_name,last_name):
    op = f'{first_name}.{last_name}{random.randint(4000,9000)}@gmail.com'
    return op.lower()
gen_email = udf(gen_email,StringType())

df = spark.range(101).toDF("customer_id")
df = df.withColumn('gender',get_gender())
df = df.withColumn('first_name',gen_first_name(col('gender')))
df = df.withColumn('last_name',gen_last_name())
df = df.withColumn('phone',gen_phone('customer_id'))
df = df.withColumn('email',gen_email('first_name','last_name'))
df.show()

