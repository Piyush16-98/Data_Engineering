# 1. Read csv from datalake


```python
SELECT top 10 * from 
OPENROWSET(
    bulk 'https://storage_name.dfs.core.windows.net/input/a.csv',
    format = 'csv',
    HEADER_ROW = TRUE,
    PARSER_VERSION = '2.0') 
as r1
```

# 2. Read parquet from datalake


```python
SELECT top 10 * from 
OPENROWSET(
    bulk 'https://storage_name.dfs.core.windows.net/input/a_parquet',
    format = 'PARQUET'
    ) 
as r1
```

![result](https://raw.githubusercontent.com/Piyush16-98/raw_files/main/screenshots/synapse/serverless_sql_pool/read_Datalake_csv_Screenshot%202023-08-16%20191926.png)

# 3. Read json from datalake


```python
SELECT * from 
OPENROWSET(
    bulk 'https://storage_name.dfs.core.windows.net/input/json_test.json',
    format = 'csv',
    FIELDTERMINATOR ='0x0b',
    FIELDQUOTE = '0x0b'
    ) 
with (
    doc NVARCHAR(max)
)
as r1
```

![result](https://raw.githubusercontent.com/Piyush16-98/raw_files/main/screenshots/synapse/serverless_sql_pool/read_json_Screenshot%202023-08-17%20114612.png)


```python
SELECT JSON_VALUE(doc, '$.product_name') AS product,
           JSON_VALUE(doc, '$.list_price') AS price FROM
OPENROWSET(
    bulk 'https://storage_name.dfs.core.windows.net/input/json_test.json',
    format = 'csv',
    FIELDTERMINATOR ='0x0b',
    FIELDQUOTE = '0x0b'
    ) 
with (
    doc NVARCHAR(max)
)
as r1
```

![result](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/synapse/serverless_sql_pool/json_value_Screenshot%202023-08-17%20114814.png?raw=true)

# 4. Read partitioned folders- using filepath


```python
SELECT *
FROM OPENROWSET(
    BULK 'https://storage_name.blob.core.windows.net/data/orders/year=*/month=*/*.*',
    FORMAT = 'parquet') AS orders
WHERE orders.filepath(1) = '2020'
    AND orders.filepath(2) IN ('1','2');
```
