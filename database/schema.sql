CREATE DATABASE VetClinic;
GO

USE VetClinic;
GO

CREATE TABLE Pets (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100),
    species VARCHAR(50),
    age INT
);

CREATE TABLE Owners (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100),
    phone VARCHAR(50)
);

ALTER TABLE Pets
ADD owner_id INT
FOREIGN KEY REFERENCES Owners(id);

ALTER TABLE Pets
ADD CONSTRAINT FK_Pets_Owners
FOREIGN KEY (owner_id)
REFERENCES Owners(id);

SELECT * FROM Pets;

INSERT INTO Owners (name, phone)
VALUES ('Juan', '8888-9999');
INSERT INTO Owners (name, phone)
VALUES ('Carlos', '7777-5555');

SELECT * FROM Owners;

INSERT INTO Pets (name, species, age, owner_id)
VALUES ('Max', 'Dog', 5, 1);

INSERT INTO Pets (name, species, age, owner_id)
VALUES ('Luna', 'Cat', 3, 1);

INSERT INTO Pets (name, species, age, owner_id)
VALUES ('Charlie', 'Dog', 2, 2);

SELECT
    Pets.name AS Pet,
    Owners.name AS Owner
FROM Pets
JOIN Owners
ON Pets.owner_id = Owners.id;