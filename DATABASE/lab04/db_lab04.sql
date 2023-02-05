--1. For each department, retrieve the department no, the number of employees in
--the department and their average salary.
SELECT DEPARTMENT_ID, COUNT(DEPARTMENT_ID) AS NO_OF_EMPLOYEES,
ROUND(AVG(SALARY)) AS AVG_SALARY
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;

--2. Write a Query to display the number of employees with the same job.

SELECT JOB_ID, COUNT(JOB_ID) AS NO_OF_EMPLOYEES
FROM EMPLOYEES
GROUP BY JOB_ID;

--3. Write a Query to select Firstname and Hiredate of Employees Hired right after
--the joining of employee_ID no 110.
SELECT FIRST_NAME, HIRE_DATE
FROM EMPLOYEES
WHERE EMPLOYEE_ID IN (Select EMPLOYEE_ID FROM EMPLOYEES WHERE EMPLOYEE_ID > 110);

--4. Write a SQL query to select those departments where maximum salary is at
--least 15000.
SELECT DEPARTMENT_ID, MAX(SALARY)
from Employees 
group by DEPARTMENT_ID
having MAX(Salary) >= 15000;

--5. Write a query to display the employee number, name (first name and last
--name) and job title for all employees whose salary is smaller than any salary
--of those employees whose job title is IT_PROG.
SELECT EMPLOYEE_ID, FIRST_NAME || ' ' || LAST_NAME AS NAME, JOB_ID
FROM EMPLOYEES 
WHERE SALARY < ANY(SELECT SALARY FROM EMPLOYEES
    WHERE JOB_ID = 'IT_PROG');


--6. Write a query in SQL to display all the information of those employees who
--did not have any job in the past.
Select * from employees
where employee_id NOT IN (Select employee_id from job_history);

--Display the manager number and the salary of the lowest paid employee of
--that manager. Exclude anyone whose manager is not known. Exclude any groups where the minimum salary is 2000. Sort the output is descending order
--of the salary.

select * from employees;

Select MANAGER_ID, MIN(SALARY)
FROM EMPLOYEES
WHERE MANAGER_ID IS NOT NULL 
GROUP BY MANAGER_ID
HAVING  MIN(SALARY) != 2000
ORDER BY MIN(SALARY) DESC;

--8. Insert into employees_BKP as it should copy the record of the employee
--whose start date is ’13-JAN-01’ from job_History table.
 
 create table employees_BKP
 as select * from employees
 where 1=2;
 
 insert INTO employees_BKP
 select * from employees
 where employee_id IN(select employee_id from job_history
 where start_date = '13-Jan-01');

select * from EMPLOYEES_BKP;
--9. Update salary of employees by 20% increment having minimum salary of
--6000.
update employees
set SALARY = SALARY + (SALARY*0.20)
WHERE JOB_ID IN (select job_id from JOBS where min_salary >= 6000);
--//42  rows updated 



--10.Delete the record of employees from employees_BKP who are manager and
--belongs to the department ‘Finance’.

delete from EMPLOYEES_BKP
where job_id IN (Select j.job_id
    from jobs j, EMPLOYEES e
    
    where j.JOB_TITLE = 'finance' AND e.manager_id is not null);



--11.For each department that has more than five employees, retrieve the
--department number and the number of its employees who are making more
--than $20,000.

select department_id, count(department_id), salary
from employees
where SALARY > 20000
group by department_id, SALARY
having count(DEPARTMENT_ID) > 5;

select


