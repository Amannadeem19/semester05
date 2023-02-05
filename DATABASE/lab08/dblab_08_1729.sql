--1) Create a PL/SQL block that computes and prints the bonus amount for a given Employee based on the employee s salary.
DECLARE
e_id employees.employee_id%type := &EMP_ID;
e_sal employees.salary%type;
bonus number;
BEGIN
    select employees.salary into e_sal from employees where employees.employee_id=e_id;
    IF (e_sal IS NULL) THEN
        bonus := 0;
    ELSIF (e_sal<1000) THEN
        bonus := e_sal*0.1;
    ELSIF (e_sal>=1000 AND e_sal<1500) THEN
        bonus := e_sal*0.15;
    ELSE
        bonus := e_sal*0.2;
        
    update employees set employees.salary = e_sal+bonus where employee_id=e_id;
    dbms_output.put_line ('Bonus given: ' || bonus);
    END IF;
END;

-- 2) Write a pl/sql block in sql that ask a user for employee id than it checks its commission if commission is null than it updates salary of that employee by adding commission into salary.
DECLARE
    emp_id EMPLOYEES.employee_id%type := &EMP_ID;
    emp_sal EMPLOYEES.salary%type;
    emp_com EMPLOYEES.commission_pct%type;
BEGIN
    SELECT salary, commission_pct INTO emp_sal, emp_com FROM Employees WHERE employee_id = emp_id;
    IF (emp_com IS NOT NULL) THEN
        DECLARE new_sal EMPLOYEES.salary%type := emp_sal + emp_com;
        BEGIN
            UPDATE Employees SET salary=emp_sal+emp_com WHERE employee_id = emp_id;
            dbms_output.put_line('Updated salary to ' || new_sal);
        END;
    END IF;
END;

-- 3) Write a PL/SQL block to obtain the department name of the employee who works for deptno 30
DECLARE
    deptno Employees.department_id%type := 30;
BEGIN
    DECLARE
        dep_name Departments.department_name%type;
    BEGIN
        SELECT department_name INTO dep_name FROM Departments WHERE department_id = deptno;
        dbms_output.put_line('Department Name: ' || dep_name);
    END;
END;

-- 4) Write a PL /SQL block to find the nature of job of the employee whose deptno is 20(to be passed as an argument)
CREATE OR REPLACE FUNCTION JobNature(DEPT_ID in Departments.department_id%type)
RETURN Jobs.job_title%type
IS
    job_nature Jobs.job_title%type;
BEGIN 
    DECLARE 
        job_id Employees.job_id%type;
        job_title Jobs.job_title%type;
    BEGIN
        SELECT job_id INTO job_id FROM Employees WHERE department_id = DEPT_ID AND ROWNUM = 1;
        SELECT job_title INTO job_title FROM Jobs WHERE job_id = job_id AND ROWNUM = 1;
        RETURN job_title;
    END;
END;

SELECT JobNature(100) FROM DUAL;


-- 5) Write a PL /SQL block to find the salary of the employee who is working in the deptno 20(to be passed as an argument).
CREATE OR REPLACE FUNCTION EmpSal(DEPT_ID in Departments.department_id%type)
RETURN Employees.salary%type
IS
BEGIN 
    DECLARE 
        e_sal Employees.salary%type;
    BEGIN
        SELECT salary INTO e_sal FROM Employees WHERE department_id = DEPT_ID AND ROWNUM = 1;
        RETURN e_sal;
    END;
END;

SELECT EmpSal(80) FROM DUAL;

-- 6) Write a PL/SQL block to update the salary of the employee with a 10% increase whose empno is to be passed as an argument for the procedure
CREATE OR REPLACE PROCEDURE IncSal(e_no in Employees.employee_id%type)
IS
BEGIN 
    UPDATE Employees SET salary=salary*1.1 WHERE employee_id = e_no;
END;

EXEC IncSal(100);

-- 7) Write a procedure to add an amount of Rs.1000 for the employees whose salaries is greater than 5000 and who belongs to the deptno passed as an argument.
CREATE OR REPLACE PROCEDURE AddSal(d_no in Employees.department_id%type)
IS
BEGIN 
    UPDATE Employees SET salary=salary+1000 WHERE department_id = d_no AND salary > 5000;
END;

EXEC AddSal(80);

-- 8) Create views for following purposes:-
    -- a) Display each designation and number of employees with that particular designation.
    
CREATE OR REPLACE VIEW EMP_DESG AS
    SELECT job_title DESIGNATION, count(*) EMPLOYEES
    FROM Jobs
    INNER JOIN Employees USING (job_id)
    GROUP BY job_title;

SElECT * FROM EMP_DESG;

    -- b) The organization wants to display only the details like empno, empname , deptno , deptname of all the employee except king.
CREATE OR REPLACE VIEW EMP_NO_KING AS
    SELECT employee_id, first_name, last_name, department_id, department_name
    FROM Employees
    INNER JOIN Departments USING(department_id)
    WHERE last_name != 'King';
    
SELECT * FROM EMP_NO_KING;

    -- c) The organization wants to display only the details empno, empname, deptno, deptname of the employees.
CREATE OR REPLACE VIEW EMP_BASIC AS
    SELECT employee_id, first_name, last_name, department_id, department_name
    FROM Employees
    INNER JOIN Departments USING(department_id);
    
SELECT * FROM EMP_BASIC;

-- 9) Write a PL/SQL code that takes two inputs from user, add them and store the sum in new variable and show the output.
DECLARE
a number := &a;
b number := &b;
c number;
BEGIN
    c := a+b;
    dbms_output.put_line(c);
END;


-- 10) Write a PL/SQL code that takes two inputs, lower boundary and upper boundary, then print the sum of all the numbers between the boundaries INCLUSIVE.
DECLARE
lower number := &lower;
higher number := &higher;
sum_t number := 0;
BEGIN
LOOP
    sum_t := sum_t+lower;
    IF lower = higher THEN
        EXIT;
    END IF;
    lower := lower+1;
END LOOP;
dbms_output.put_line(sum_t);
END;

-- 11) Write a PL/SQL code to retrieve the employee name, hiredate, and the department name in which he works, whose number is input by the user.
DECLARE
e_no Employees.employee_id%type := &EMP_NO;
BEGIN
    DECLARE
        e_name Employees.first_name%type;
        e_hire Employees.hire_date%type;
        e_dep Departments.department_name%type;
    BEGIN
        SELECT first_name, hire_date, department_name
        INTO e_name, e_hire, e_dep
        FROM Employees
        INNER JOIN Departments USING(department_id)
        WHERE employee_id = e_no;
        
        dbms_output.put_line('Name: ' || e_name);
        dbms_output.put_line('Hire Date: ' || e_hire);
        dbms_output.put_line('Department: ' || e_dep);
    END;
END;

-- 12) Write a PL/SQL code to check whether the given number is palindrome or not.
DECLARE
    n number := &NUMBER;
    m number;
    temp number:=0;
    rem number;
BEGIN
    m := n;

    WHILE n>0
    LOOP
        rem := mod(n,10);
        temp := (temp*10)+rem;
        n := trunc(n/10);
    END LOOP;
      
    IF m = temp THEN
        dbms_output.put_line('true');
    ELSE
        dbms_output.put_line('false');
    END IF;
END;

-- 13) Write a PL/SQL code that takes all the required inputs from the user for the Employee table and then insert it into the Employee and Department table in the database.
DECLARE
e_no Employees.employee_id%type:= &EMP_NO;
e_fname Employees.first_name%type := &FIRST_NAME;
e_lname Employees.last_name%type := &LAST_NAME;
e_email Employees.email%type := &EMAIL;
e_phone Employees.phone_number%type := &PHONE;
e_hire Employees.hire_date%type := &HIRE_DATE;
e_job Employees.job_id%type := &JOB_ID;
e_sal Employees.salary%type := &SALARY;
e_com Employees.commission_pct%type := &COMMISSION;
e_man Employees.manager_id%type := &MANANGER_ID;
e_dep Employees.Department_id%type := &DEPARTMENT_ID;
t_id int;
BEGIN
    SELECT employee_id INTO t_id FROM Employees WHERE manager_id = e_man;
    IF (t_id IS NULL) THEN
        dbms_output.put_line('Manager ID does not exist in employees table');
    SELECT department_id INTO t_id FROM Departments WHERE department_id = e_dep;
    ELSIF (t_id IS NULL) THEN
        dbms_output.put_line('Department ID does not exist in Departments table');
    ELSE
       INSERT INTO EMPLOYEES VALUES (e_no, e_fname, e_lname, e_email, e_phone, e_hire, e_job, e_sal, e_com, e_man, e_dep);
    END IF;
END;


-- 14) Write a PL/SQL code to find the first employee who has a salary over $2500 and is higher in the chain of command than employee 7499. Note: For chain, use of LOOP is necessary.
DECLARE
e_sal Employees.salary%type := 0;
e_mgr Employees.manager_id%type;
e_lname Employees.last_name%type;
e_no Employees.employee_id%type := 7499;
BEGIN
    SELECT manager_id into e_mgr from Employees
    WHERE employee_id = e_no;
    
    WHILE e_sal <= 2500 LOOP
        SELECT salary, manager_id, last_name into e_sal, e_mgr, e_lname
        FROM Employees WHERE employee_id = e_mgr;
    END LOOP;
    
    dbms_output.put_line('Employee: ' || e_lname);
END;

-- 15) Write a PL/SQL code to print the sum of first 100 numbers.
DECLARE
a number;
sum1 number :=0;
BEGIN
    a := 1;
    LOOP
        sum1 := sum1+a;
        IF (a=100) THEN
            EXIT;
        END IF;
        a:=a+1;
    END LOOP;
    dbms_output.put_line(sum1);
end;