CREATE TABLE Person (
ID int NOT NULL,
Name varchar (50) NOT NULL,
PreviousName varchar (50) NULL,
SameNameCount int NULL,
CONSTRAINT pk_Person PRIMARY KEY (ID));

---------------------------------
Trigger#01:
---------------------------------
CREATE OR REPLACE TRIGGER update_previous_name
BEFORE UPDATE ON Person
FOR EACH ROW
BEGIN
	:new.PreviousName := :old.Name;
	dbms_output.put_line('');
	dbms_output.put_line('Old Name' || :old.PreviousName);
	dbms_output.put_line('New Name' || :new.Name);
	dbms_output.put_line('');
END;

INSERT INTO Person (ID, Name) values (1, 'Ashmal');
INSERT INTO Person (ID, Name) values (2, 'Hasnain');
INSERT INTO Person (ID, Name) values (3, 'Samad');
INSERT INTO Person (ID, Name) values (4, 'Ashmal');

UPDATE Person SET Name = 'Ali' WHERE ID = 3;
SELECT * FROM Person;

---------------------------------
Trigger#02:
---------------------------------
CREATE OR REPLACE TRIGGER set_same_name_count
AFTER INSERT OR DELETE OR UPDATE OF Name
ON Person
BEGIN
	UPDATE Person A SET SameNameCount = (SELECT COUNT(*) FROM Person WHERE NAME = A.Name);
END;

INSERT INTO Person (ID, Name) values (5, 'Ashmal');
INSERT INTO Person (ID, Name) values (6, 'Hasnain');
INSERT INTO Person (ID, Name) values (7, 'Samad');
INSERT INTO Person (ID, Name) values (8, 'Ashmal');
SELECT * FROM Person;