# 1. Create Stored Procedure

###    -               Stored Procedure to filter transaction based on year


```python
Create procedure filter_year @year int
as 
Begin
SELECT TOP (10) * FROM [SalesLT].[SalesOrderHeader] where year(OrderDate) = @year
End
```

![result](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/sql/stored_proc/cret_stored_proc_Screenshot%202023-08-19%20131225.png?raw=true)

# 2. Execute Stored Procedure

![result](https://github.com/Piyush16-98/raw_files/blob/main/screenshots/sql/stored_proc/exec_proc_Screenshot%202023-08-19%20131848.png?raw=true)

# 3. Multiple parameters


```python
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
GO;
```


```python
EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';
```
