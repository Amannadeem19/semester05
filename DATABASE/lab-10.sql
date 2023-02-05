-- TASK-01 --

CREATE TABLE Persons (
    PersonID int PRIMARY KEY,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    Age int
);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (1,'John','Smith','South Street', 'Karachi', 23);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (2,'King','Smile','North Street', 'Karachi', 21);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (3,'Robb','Gold','East Street', 'Karachi', 27);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (4,'Josh','Lui','West Street', 'Karachi', 24);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (5,'Jack','Brand','Central Street', 'Karachi', 28);
savepoint savepoint1;
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (6,'Osama','Aslam','Silver Street', 'Karachi', 23);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (7,'Erum','Shaheen','Gold Street', 'Karachi', 25);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (8,'Faraz','Naeem','White Street', 'Karachi', 28);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (9,'Konain','Ahmed','Green Street', 'Karachi', 34);
insert into PERSONS (PersonID, FirstName, LastName, Address, City, Age) VALUES (10,'Abdullah','Aftab','Red Street', 'Karachi', 29);
savepoint savepoint2;

update PERSONS set FIRSTNAME='Rida' where PersonID=7;
select * from PERSONS;

rollback to savepoint savepoint1;
select * from PERSONS;


update PERSONS set Age=30 where PersonID=8;
-- commit;



-- TASK-02 --
-- We observe the phenomenon of Strict Scheduling here. 
-- In order to avoid write, write loss update problem the session 2 is unable to update the age of PersonId=8 until it's commited here in this session 1.