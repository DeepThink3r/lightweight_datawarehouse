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
	EmployeeIDI VARCHAR,
	LastNameI VARCHAR,
	FirstNameI VARCHAR,
	TitleI VARCHAR,
	TitleOfCourtesyI VARCHAR,
	BirthDateI VARCHAR,
	HireDateI VARCHAR,
	AddressI VARCHAR,
	CityI VARCHAR,
	RegionI VARCHAR,
	PostalCodeI VARCHAR,
	CountryI VARCHAR,
	HomePhoneI VARCHAR,
	ExtensionI VARCHAR,
	PhotoI VARCHAR,
	NotesI VARCHAR,
	ReportsToI VARCHAR,
	PhotoPathI VARCHAR,
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
	Picture VARCHAR,
	origem VARCHAR,
	ext_timestmp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) USING columnar
WITH (columnar.compression = zstd)