Create DATABASE vic_cities;
use vic_cities;
create table cities(
city varchar(20),
lat decimal(8,6),
lng decimal(9,6));

Select * from cities

ALTER TABLE cities
ADD PRIMARY KEY(city);