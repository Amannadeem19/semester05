--creating triggers

set serveroutput on;
create or replace trigger hr.salarychanges
before insert or update or delete on hr.emp_check
for each row
enable
declare
sal_diff number;
begin
DBMS_OUTPUT.put_line('old salary is : ' || :old.salary);

DBMS_OUTPUT.put_line('new salary is : ' || :new.salary);
end;
/
drop trigger salarychanges;
insert into hr.emp_check(employee_id, salary) values (100, 1000);
update hr.emp_check set salary = 2000 where employee_id = 100;
--select * from EMP_CHECK;

declare 
begin
dbms_output.put_line('done');
end;

--employeeshistory
create table employee_history as select employee_id , salary from employees where 1=2;
create or replace trigger hr.Employee_salary
before update of salary on hr.employees
for each row
begin
insert into employee_history(employee_id, salary) values(:old.employee_id, :old.salary);
DBMS_OUTPUT.put_line('history sucessfully entered' || sysdate());
end;
/
update hr.employees
set salary = 40000 where employee_id = 169;