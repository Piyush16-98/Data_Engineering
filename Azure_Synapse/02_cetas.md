# 1. Create database with utf8 collation


```python
CREATE DATABASE adv_data
    COLLATE Latin1_General_100_BIN2_UTF8;
GO;
```

# 2. Create External Data Source


```python
CREATE EXTERNAL DATA SOURCE cnt_adv_data
WITH (
    LOCATION = 'https://storagedev1112.dfs.core.windows.net'
)
GO;
```

# 3. Create External File Format


```python
CREATE EXTERNAL FILE FORMAT pq_format
    WITH (
            FORMAT_TYPE = PARQUET,
        );
GO;
```

# 4. Read source file / explore


```python
SELECT *
 FROM
     OPENROWSET(
         BULK 'adv-data-source/AdventureWorks_Sales_2017.csv',
         DATA_SOURCE = 'cnt_adv_data',
         FORMAT = 'CSV',
         PARSER_VERSION = '2.0',
         HEADER_ROW = TRUE
     ) AS od
```

![result](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/synapse/cetas/read_source_Screenshot%202023-08-19%20214714.png?raw=true)

# 5. Create external table as select


```python
CREATE EXTERNAL TABLE [dbo].[product_dim]
WITH (
    LOCATION = 'adv-data-source/ext_tables/product_dim',
    DATA_SOURCE = cnt_adv_data,
    FILE_FORMAT = pq_format
)
AS
SELECT *
 FROM
     OPENROWSET(
         BULK 'adv-data-source/AdventureWorks_Sales_2017.csv',
         DATA_SOURCE = 'cnt_adv_data',
         FORMAT = 'CSV',
         PARSER_VERSION = '2.0',
         HEADER_ROW = TRUE
     ) AS od

```

# 6. Read external table / external location

![result](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/synapse/cetas/read_external_tb_Screenshot%202023-08-19%20220537.png?raw=true)

![result](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/synapse/cetas/ext_table_location_Screenshot%202023-08-19%20220622.png?raw=true)
