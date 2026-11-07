---Extensões---
CREATE EXTENSION IF NOT EXISTS citus;

CREATE EXTENSION IF NOT EXISTS citus_columnar;

---Schemas---
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS transformed;
CREATE SCHEMA IF NOT EXISTS mart;

---STAGING--
CREATE TABLE IF NOT EXISTS staging.customers (
	CustomerID VARCHAR,
	CompanyName VARCHAR,
	ContactName VARCHAR,
	ContactTitle VARCHAR,
	Address VARCHAR,
	City VARCHAR,
	Region VARCHAR,
	PostalCode VARCHAR,
	Country VARCHAR,
	Phone VARCHAR,
	Fax VARCHAR,
	origem varchar,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)


CREATE TABLE IF NOT EXISTS staging.employees (
	EmployeeID VARCHAR,
	LastName VARCHAR,
	FirstName VARCHAR,
	Title VARCHAR,
	TitleOfCourtesy VARCHAR,
	BirthDate VARCHAR,
	HireDate VARCHAR,
	Address VARCHAR,
	City VARCHAR,
	Region VARCHAR,
	PostalCode VARCHAR,
	Country VARCHAR,
	HomePhone VARCHAR,
	Extension VARCHAR,
	Notes VARCHAR,
	ReportsTo VARCHAR,
	PhotoPath VARCHAR,
	origem varchar,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)


CREATE TABLE IF NOT EXISTS staging.products (
ProductID VARCHAR,
ProductName VARCHAR,
SupplierID VARCHAR,
CategoryID VARCHAR,
QuantityPerUnit VARCHAR,
UnitPrice VARCHAR,
UnitsInStock VARCHAR,
UnitsOnOrder VARCHAR,
ReorderLevel VARCHAR,
Discontinued VARCHAR,
origem VARCHAR,
ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)


CREATE TABLE IF NOT EXISTS staging.region (
	RegionID VARCHAR,
	RegionDescription VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)


CREATE TABLE IF NOT EXISTS staging.territories (
	TerritoryID VARCHAR,
	TerritoryDescription VARCHAR,
	RegionID VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)


CREATE TABLE IF NOT EXISTS staging.employeeterritories (
	EmployeeID VARCHAR,
	TerritoryID VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)

CREATE TABLE IF NOT EXISTS staging.shippers (
	ShipperID VARCHAR,
	CompanyName VARCHAR,
	Phone VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)

CREATE TABLE IF NOT EXISTS staging.categories (
	CategoryID VARCHAR,
	CategoryName VARCHAR,
	Description VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)

CREATE TABLE IF NOT EXISTS staging.orders (
	OrderID VARCHAR,
	CustomerID VARCHAR,
	EmployeeID VARCHAR,
	OrderDate VARCHAR,
	RequiredDate VARCHAR,
	ShippedDate VARCHAR,
	ShipVia VARCHAR,
	Freight VARCHAR,
	ShipName VARCHAR,
	ShipAddress VARCHAR,
	ShipCity VARCHAR,
	ShipRegion VARCHAR,
	ShipPostalCode VARCHAR,
	ShipCountry VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)


CREATE TABLE IF NOT EXISTS staging.order_details (
	OrderID VARCHAR,
	ProductID VARCHAR,
	UnitPrice VARCHAR,
	Quantity VARCHAR,
	Discount VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)


select * from staging.territories