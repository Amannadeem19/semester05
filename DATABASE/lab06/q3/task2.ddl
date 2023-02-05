-- Generated by Oracle SQL Developer Data Modeler 4.1.1.888
--   at:        2022-10-12 10:51:10 PDT
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g




CREATE
  TABLE Employees
  (
    emp_id  VARCHAR2 (10 CHAR) NOT NULL ,
    f_name  VARCHAR2 (10 CHAR) NOT NULL ,
    l_name  VARCHAR2 (10 CHAR) NOT NULL ,
    address VARCHAR2 (20 CHAR) NOT NULL
  ) ;
ALTER TABLE Employees ADD CONSTRAINT Employees_PK PRIMARY KEY ( emp_id ) ;


CREATE
  TABLE customers
  (
    cus_id           VARCHAR2 (10 CHAR) NOT NULL ,
    name             VARCHAR2 (10 CHAR) NOT NULL ,
    pro_name         VARCHAR2 (10 CHAR) NOT NULL ,
    Quantity         INTEGER NOT NULL ,
    address          VARCHAR2 (20 CHAR) NOT NULL ,
    Employees_emp_id VARCHAR2 (10 CHAR) NOT NULL
  ) ;
ALTER TABLE customers ADD CONSTRAINT customers_PK PRIMARY KEY ( cus_id ) ;


CREATE
  TABLE orders
  (
    order_name       VARCHAR2 (20 CHAR) NOT NULL ,
    Quantity         INTEGER NOT NULL ,
    Shipped_data     VARCHAR2 (10 CHAR) NOT NULL ,
    Received_data    VARCHAR2 (20 CHAR) NOT NULL ,
    customers_cus_id VARCHAR2 (10 CHAR) NOT NULL
  ) ;
ALTER TABLE orders ADD CONSTRAINT orders_PK PRIMARY KEY ( customers_cus_id ) ;


CREATE
  TABLE produccts
  (
    name VARCHAR2 (10 CHAR) NOT NULL ,
    price FLOAT (10000) NOT NULL ,
    stock            INTEGER NOT NULL ,
    product_id       VARCHAR2 (10 CHAR) NOT NULL ,
    Employees_emp_id VARCHAR2 (10 CHAR) NOT NULL
  ) ;
ALTER TABLE produccts ADD CONSTRAINT produccts_PK PRIMARY KEY ( product_id,
Employees_emp_id ) ;


ALTER TABLE customers ADD CONSTRAINT customers_Employees_FK FOREIGN KEY (
Employees_emp_id ) REFERENCES Employees ( emp_id ) ;

ALTER TABLE orders ADD CONSTRAINT orders_customers_FK FOREIGN KEY (
customers_cus_id ) REFERENCES customers ( cus_id ) ;

ALTER TABLE produccts ADD CONSTRAINT produccts_Employees_FK FOREIGN KEY (
Employees_emp_id ) REFERENCES Employees ( emp_id ) ;


-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             4
-- CREATE INDEX                             0
-- ALTER TABLE                              7
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0