CREATE DATABASE COVID_Figures
GO
USE COVID_Figures;
GO
CREATE TABLE Daily_Cases
CasesKey INT NOT NULL IDENTITY,
Country VARCHAR(2),
FullDate DATE,
New_Cases INT,
DeNotified_Cases INT,
PRIMARY KEY CasesKey;

CREATE TABLE Daily_Deaths
DeathsKey INT NOT NULL IDENTITY,
CountryID VARCHAR(2),
FullDate DATE,
New_Deaths INT,
DeNotified_Deaths INT,
PRIMARY KEY DeathsKey;

