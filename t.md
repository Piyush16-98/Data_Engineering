# 1. Read data from datalake
SELECT top 10 * from 
OPENROWSET(
    bulk 'https://storagedev1112.dfs.core.windows.net/input/a.csv',
    format = 'csv',
    HEADER_ROW = TRUE,
    PARSER_VERSION = '2.0') 
as r1
![image-2.png](attachment:image-2.png)

# 2. Create external table - CSV file
2.1 create a database master key.\
&nbsp;&nbsp;&nbsp;&nbsp; This key will be used to protect the Shared Access Signature which is specified in the next step

CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'P@ssw0rd@123';
2.2 using the Shared Access Signature to authorize the use of the Azure Data Lake Storage account
CREATE DATABASE SCOPED CREDENTIAL SasToken
WITH IDENTITY='SHARED ACCESS SIGNATURE'
, SECRET = 'sas_key';
2.3 Create external file format
CREATE EXTERNAL FILE FORMAT TextFileFormat WITH (  
      FORMAT_TYPE = DELIMITEDTEXT,  
    FORMAT_OPTIONS (  
        FIELD_TERMINATOR = ',',
        FIRST_ROW = 2))
2.4 Create External Table
CREATE EXTERNAL TABLE [logdata]
(
    [Correlation id] [varchar](200) NULL,
	[Operation name] [varchar](200) NULL,
	[Status] [varchar](100) NULL,
	[Event category] [varchar](100) NULL,
	[Level] [varchar](100) NULL,
	[Time] [datetime] NULL,
	[Subscription] [varchar](200) NULL,
	[Event initiated by] [varchar](1000) NULL,
	[Resource type] [varchar](1000) NULL,
	[Resource group] [varchar](1000) NULL,
    [Resource] [varchar](2000) NULL)
WITH (
 LOCATION = '/Log.csv',
    DATA_SOURCE = log_data,  
    FILE_FORMAT = TextFileFormat
)