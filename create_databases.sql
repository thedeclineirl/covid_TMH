CREATE DATABASE COVID_Figures
GO
USE COVID_Figures;
GO
CREATE TABLE Daily_Cases
( CasesID INT NOT NULL IDENTITY,
Country VARCHAR(20),
County VARCHAR(10),
FullDate DATE,
New_Cases INT,
DeNotified_Cases INT,
PRIMARY KEY (CasesID));

CREATE TABLE Daily_Deaths
( DeathsID INT NOT NULL IDENTITY,
Country VARCHAR(20),
County VARCHAR(10),
FullDate DATE,
New_Deaths INT,
DeNotified_Deaths INT,
PRIMARY KEY (DeathsID));

