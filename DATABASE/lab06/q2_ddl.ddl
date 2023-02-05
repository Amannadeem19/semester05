-- Generated by Oracle SQL Developer Data Modeler 4.1.1.888
--   at:        2022-10-12 23:56:07 PKT
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g




CREATE
  TABLE College
  (
    COffice    VARCHAR2 (20 CHAR) NOT NULL ,
    CName      VARCHAR2 (20 CHAR) NOT NULL ,
    CPhone     NUMBER (11) NOT NULL ,
    College_ID NUMBER NOT NULL
  ) ;
ALTER TABLE College ADD CONSTRAINT College_PK PRIMARY KEY ( College_ID ) ;


CREATE
  TABLE Course
  (
    CourseDesc VARCHAR2 (30 CHAR) NOT NULL ,
    "level"    INTEGER NOT NULL ,
    CoName     VARCHAR2 (20 CHAR) NOT NULL ,
    credits    INTEGER NOT NULL ,
    Ccode      INTEGER NOT NULL ,
    Dept_Dcode VARCHAR2 (10 CHAR) NOT NULL
  ) ;
ALTER TABLE Course ADD CONSTRAINT Course_PK PRIMARY KEY ( Ccode, Dept_Dcode ) ;


CREATE
  TABLE Dept
  (
    DName              VARCHAR2 (20 CHAR) NOT NULL ,
    Dcode              VARCHAR2 (10 CHAR) NOT NULL ,
    DOffice            VARCHAR2 (20 CHAR) NOT NULL ,
    DPhone             NUMBER (11) NOT NULL ,
    College_College_ID NUMBER NOT NULL
  ) ;
ALTER TABLE Dept ADD CONSTRAINT Dept_PK PRIMARY KEY ( Dcode ) ;


CREATE
  TABLE Instructor
  (
    id                 INTEGER NOT NULL ,
    IName              VARCHAR2 (20 CHAR) NOT NULL ,
    IOffice            VARCHAR2 (20 CHAR) NOT NULL ,
    IPhone             NUMBER (11) NOT NULL ,
    Rank               INTEGER NOT NULL ,
    Dept_Dcode2        VARCHAR2 (10 CHAR) NOT NULL ,
    Dept_Dcode         VARCHAR2 (10 CHAR) NOT NULL ,
    CStartDate         DATE NOT NULL ,
    College_College_ID NUMBER NOT NULL ,
    Dept_Dcode1        VARCHAR2 (10 CHAR) NOT NULL ,
    CStartDate1        DATE NOT NULL
  ) ;
CREATE UNIQUE INDEX Instructor__IDX ON Instructor
  (
    Dept_Dcode ASC
  )
  ;
CREATE UNIQUE INDEX Instructor__IDXv1 ON Instructor
  (
    College_College_ID ASC
  )
  ;
CREATE UNIQUE INDEX Instructor__IDXv2 ON Instructor
  (
    Dept_Dcode1 ASC
  )
  ;
ALTER TABLE Instructor ADD CONSTRAINT Instructor_PK PRIMARY KEY ( id,
Dept_Dcode2 ) ;


CREATE
  TABLE Section
  (
    YEAR  INTEGER NOT NULL ,
    CRoom VARCHAR2 (5 CHAR) NOT NULL ,
    Attribute_3 UNKNOWN
    --  ERROR: Datatype UNKNOWN is not allowed
    ,
    secNo                  INTEGER NOT NULL ,
    sem                    INTEGER NOT NULL ,
    DaysTime               DATE NOT NULL ,
    SecId                  INTEGER NOT NULL ,
    Course_Ccode           INTEGER NOT NULL ,
    Course_Dept_Dcode      VARCHAR2 (10 CHAR) NOT NULL ,
    Instructor_id          INTEGER NOT NULL ,
    Instructor_Dept_Dcode1 VARCHAR2 (10 CHAR) NOT NULL
  ) ;
ALTER TABLE Section ADD CONSTRAINT Section_PK PRIMARY KEY ( SecId, Course_Ccode
, Course_Dept_Dcode, Instructor_id, Instructor_Dept_Dcode1 ) ;


CREATE
  TABLE Student
  (
    DOB        VARCHAR2 (4000) NOT NULL ,
    address    VARCHAR2 (20 CHAR) NOT NULL ,
    SName      VARCHAR2 (20 CHAR) NOT NULL ,
    Sid        INTEGER NOT NULL ,
    Phone      VARCHAR2 (20 CHAR) NOT NULL ,
    major      VARCHAR2 (10 CHAR) NOT NULL ,
    Dept_Dcode VARCHAR2 (10 CHAR) NOT NULL
  ) ;
ALTER TABLE Student ADD CONSTRAINT Student_PK PRIMARY KEY ( Sid, Dept_Dcode ) ;


CREATE
  TABLE Takes
  (
    Student_Sid               INTEGER NOT NULL ,
    Student_Dcode             VARCHAR2 (10 CHAR) NOT NULL ,
    Section_SecId             INTEGER NOT NULL ,
    Section_Course_Ccode      INTEGER NOT NULL ,
    Section_Course_Dept_Dcode VARCHAR2 (10 CHAR) NOT NULL ,
    Section_id                INTEGER NOT NULL ,
    Section_Dcode1            VARCHAR2 (10 CHAR) NOT NULL ,
    Grade                     VARCHAR2 (10 CHAR) NOT NULL
  ) ;
ALTER TABLE Takes ADD CONSTRAINT Takes_PK PRIMARY KEY ( Student_Sid,
Student_Dcode, Section_SecId, Section_Course_Ccode, Section_Course_Dept_Dcode,
Section_id, Section_Dcode1 ) ;


ALTER TABLE Course ADD CONSTRAINT Course_Dept_FK FOREIGN KEY ( Dept_Dcode )
REFERENCES Dept ( Dcode ) ;

ALTER TABLE Dept ADD CONSTRAINT Dept_College_FK FOREIGN KEY (
College_College_ID ) REFERENCES College ( College_ID ) ;

ALTER TABLE Takes ADD CONSTRAINT FK_ASS_7 FOREIGN KEY ( Student_Sid,
Student_Dcode ) REFERENCES Student ( Sid, Dept_Dcode ) ;

ALTER TABLE Takes ADD CONSTRAINT FK_ASS_8 FOREIGN KEY ( Section_SecId,
Section_Course_Ccode, Section_Course_Dept_Dcode, Section_id, Section_Dcode1 )
REFERENCES Section ( SecId, Course_Ccode, Course_Dept_Dcode, Instructor_id,
Instructor_Dept_Dcode1 ) ;

ALTER TABLE Instructor ADD CONSTRAINT Instructor_College_FK FOREIGN KEY (
College_College_ID ) REFERENCES College ( College_ID ) ;

ALTER TABLE Instructor ADD CONSTRAINT Instructor_Dept_FK FOREIGN KEY (
Dept_Dcode ) REFERENCES Dept ( Dcode ) ;

ALTER TABLE Instructor ADD CONSTRAINT Instructor_Dept_FKv2 FOREIGN KEY (
Dept_Dcode1 ) REFERENCES Dept ( Dcode ) ;

ALTER TABLE Instructor ADD CONSTRAINT Instructor_Dept_FKv3 FOREIGN KEY (
Dept_Dcode2 ) REFERENCES Dept ( Dcode ) ;

ALTER TABLE Section ADD CONSTRAINT Section_Course_FK FOREIGN KEY ( Course_Ccode
, Course_Dept_Dcode ) REFERENCES Course ( Ccode, Dept_Dcode ) ;

ALTER TABLE Section ADD CONSTRAINT Section_Instructor_FK FOREIGN KEY (
Instructor_id, Instructor_Dept_Dcode1 ) REFERENCES Instructor ( id, Dept_Dcode2
) ;

ALTER TABLE Student ADD CONSTRAINT Student_Dept_FK FOREIGN KEY ( Dept_Dcode )
REFERENCES Dept ( Dcode ) ;

CREATE SEQUENCE College_College_ID_SEQ START WITH 1 NOCACHE ORDER ;
CREATE OR REPLACE TRIGGER College_College_ID_TRG BEFORE
  INSERT
    ON College FOR EACH ROW WHEN
    (
      NEW.College_ID IS NULL
    )
    BEGIN :NEW.College_ID := College_College_ID_SEQ.NEXTVAL;
END;
/


-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             3
-- ALTER TABLE                             18
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           1
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
-- CREATE SEQUENCE                          1
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
-- ERRORS                                   1
-- WARNINGS                                 0
