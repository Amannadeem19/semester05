set serveroutput  on

DECLARE

    Sec_name varchar2(20) := 'bs se';
BEGIN   
 
    dbms_output.put_line('This is : '|| Sec_Name );
    
END;

DECLARE

    Sec_name varchar2(20) := 'bs se';
BEGIN   

    dbms_output.put_line('This is : '|| Sec_Name );

END;

--variables
Declare 
--   global variables 
    a integer :=10;
    b integer := 20;
    c integer;

BEGIN
    declare
--    local variables
    name varchar2(20) := 'aman nadeem';
    begin
    
    c:=a+b;
    dbms_output.put_line('name is : ' || name);
    dbms_output.put_line('the sum is : ' || c);
    
    
    end;
END;select * from employees;



--getting data from tables


DECLARE 

E_ID hr.EMPLOYEES.EMPLOYEE_ID%type;
e_name hr.EMPLOYEES.FIRST_NAME%type;

BEGIN
    
    select EMPLOYEE_ID, FIRST_NAME 
    into E_ID, e_name from hr.employees
    where employee_id = 169;
    
    dbms_output.put_line('Employees id' || E_ID);
    dbms_output.put_line('Employees name ' || e_name);

END;


DECLARE
e_id hr.employees.EMPLOYEE_ID%type;
e_name hr.employees.FIRST_NAME%type;
e_lname hr.employees.LAST_NAME%type;
d_name hr.DEPARTMENTS.DEPARTMENT_NAME%type;
BEGIN
    SELECT EMPLOYEE_ID,FIRST_NAME,LAST_NAME,DEPARTMENT_NAME
    INTO e_id, e_name, e_lname, d_name
    FROM hr.employees inner join hr.DEPARTMENTS
    on hr.employees.DEPARTMENT_ID = hr.DEPARTMENTS.DEPARTMENT_ID and
    EMPLOYEE_ID =100 ;
    DBMS_OUTPUT.PUT_LINE('hello world');
    dbms_output.put_line('EMPLOYEE ID: ' ||e_id);
    dbms_output.put_line('EMPLOYEE First Name: ' ||e_name);
    dbms_output.put_line('EMPLOYEE Last Name: ' ||e_lname);
    dbms_output.put_line('DEPARTMENT Name: ' ||d_name);
END;


--conditional logic

DECLARE 
E_ID hr.EMPLOYEES.EMPLOYEE_ID%type := 169;
e_sal hr.EMPLOYEES.SALARY%type;
BEGIN
    SELECT SALARY INTO e_sal FROM hr.EMPLOYEES WHERE EMPLOYEE_ID = E_ID;
    IF(e_sal > 15000)
    THEN 
    UPDATE hr.EMPLOYEES
    SET SALARY = e_sal+1000
    where employee_id = E_ID;
    DBMS_OUTPUT.PUT_LINE('record updated');
    ELSIF (e_sal = 14000)
    then
    update employees
    set salary = e_sal + 500
    where Employee_id = E_ID;
    DBMS_OUTPUT.put_line('record updated2');
    
    end if;
END;
    
--  select EMPLOYEE_ID, FIRST_NAME, SALARY from employees WHERE EMPLOYEE_ID=169;
  
  --loops
set serveroutput  on
DECLARE 

BEGIN
    
    FOR c IN (SELECT EMPLOYEE_ID, SALARY, FIRST_NAME , LAST_NAME FROM hr.EMPLOYEES
             WHERE DEPARTMENT_ID = 90)
    
    loop
    dbms_output.put_line('e_id : ' || c.EMPLOYEE_ID || ' SALARY ' || c.SALARY);
    
    end loop;

end;

--creating views

--read-only view

create or replace view Emp_temp as
select employee_id, salary from employees
with read only;

--// gives error
update Emp_temp
set salary = salary + 100 where employee_id = 102; 

select * from Emp_temp;


--read and updatable view 
create or replace view Emp_info as
select employee_id, job_id, department_id, salary from employees;

--can we update? yes
update EMP_INFO set 
salary = salary + 500
where EMPLOYEE_ID  > 200;
select * from EMP_INFO;


--materialized views -- hold data physically

create materialized view Emp_data as
select salary from employees where employee_id = 169;

select * from Emp_data;


update EMPLOYEES
set salary = salary + 2000
where employee_id = 169;

select salary from employees where EMPLOYEE_ID  = 169; 



--FUNCTIONS

create or replace function findSalary(emp_id in number)
return number
is 
salary number;
begin 
select salary into salary from employees where employee_id = emp_id;
return (salary);
end;
select findSalary(100) from dual;

create table employeesSalary as
select employee_id, salary from employees where 1=2;

--stored procedures 

create or replace procedure insertdata(salary in number)
is
total_record INT;
emp_id number;
begin

select count(employee_id) into emp_id from employees;
emp_id := emp_id +1;
total_record := emp_id;
insert into EMPLOYEESSALARY(employee_id, salary) values (emp_id, salary);

DBMS_OUTPUT.PUT_LINE('new record inserted with id '|| emp_id);
DBMS_OUTPUT.PUT_LINE('Total records are ' || total_record);

end;
exec insertdata(2000);
select * from EMPLOYEESSALARY;


--q1
create or replace procedure myproc1(emp_id in number)
is
salary number;
bonus real;
begin
        select salary into salary from employees where employee_id = emp_id;
        if(salary < 1000)
        then
        bonus :=salary*0.1;
        elsif (salary > 1000 and salary < 1500)then
        bonus := salary*0.15;
        elsif(salary > 1500)then
        bonus := salary*0.2;
        elsif(salary =0)then
        bonus := 0;
        end if;
        
        update EMPLOYEES set salary =  salary + bonus
        where employee_id = emp_id;
end;

exec myproc1(169);
select EMPLOYEE_ID, FIRST_NAME, SALARY from employees WHERE EMPLOYEE_ID=169;

--q8a

create or replace view EmpDesg as
select j.job_title DESIGNATION , count(*)as employees from employees e, jobs j
where e.job_id = j.job_id
group by j.job_title;
select * from EmpDesg;


--& is used for taking user input
declare 

emp_id employees.employee_id%type := &employee_no;
begin
DBMS_OUTPUT.PUT_LINE(emp_id);
end;

