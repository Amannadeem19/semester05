Select *
FROM EMPLOYEES;




SELECT EMPLOYEE_ID, JOB_ID
FROM EMPLOYEES;


--USE ALIAS 

SELECT HIRE_DATE AS JOINING_DATE
FROM EMPLOYEES;

--USE OF CONCATENATION OPERATOR ||

SELECT FIRST_NAME || LAST_NAME AS "FULL NAME"


FROM EMPLOYEES;


--USE DISTINCT KEYWORD

SELECT DISTINCT (DEPARTMENT_ID)
FROM EMPLOYEES;

--USE ALL KEYWORD REVER5E OF 
SELECT ALL(SALARY)
FROM EMPLOYEES;

--USE *

SELECT *
FROM DEPARTMENTS;

--SEARCH CONDITIONS
--1)
SELECT *
FROM EMPLOYEES
WHERE SALARY BETWEEN 20000 and 30000;
--2)
SELECT EMPLOYEE_ID,FIRST_NAME, DEPARTMENT_ID
FROM EMPLOYEES
WHERE DEPARTMENT_ID BETWEEN 59 and 101;

--3)
SELECT *
FROM EMPLOYEES,LOCATIONS
WHERE city = 'Toronto' OR city = 'Hiroshima' OR city =  'Sydney';
--4)
SELECT *
FROM EMPLOYEES
WHERE FIRST_NAME LIKE '%ll%';
--5)
SELECT *
FROM EMPLOYEES
WHERE COMMISSION_PCT IS NULL;

--sorting rows

SELECT * 
FROM EMPLOYEES
ORDER BY SALARY asc;

--task
SELECT * 
FROM EMPLOYEES
ORDER BY SALARY desc;

--//Print an employee name (first letter capital) and job title (lower Case)
SELECT FIRST_NAME , SUBSTR(FIRST_NAME,1,1) as first_letter, LOWER(JOB_ID) AS JOB_ID   
From EMPLOYEES;
--
--Display employee name and job title together, length of employee name and the
--numeric position of letter A in employee name, for all employees who are in sales.
SELECT FIRST_NAME , LENGTH(FIRST_NAME) AS LENGTH, INSTR(FIRST_NAME, 'a') AS POSITION
FROM EMPLOYEES;
--
--Comparing the hire dates for all employees who started in 2003, display the employee
--number, hire date, and month started using the conversion and date functions.

SELECT EMPLOYEE_ID, HIRE_DATE, EXTRACT(Month FROM HIRE_DATE) AS STARTING_MONTH
FROM EMPLOYEES;

--
--To display the employee number, the month number and year of hiring.
SELECT EMPLOYEE_ID, EXTRACT(MONTH FROM HIRE_DATE) AS MONTH_HIRE, EXTRACT(YEAR FROM HIRE_DATE) AS YEAR_HIRE
FROM EMPLOYEES;

--To display the employee’s name and hire date for all employees. The hire date
--appears as 16 September, 2021.

SELECT CONCAT(FIRST_NAME, LAST_NAME) AS NAME, TO_CHAR(HIRE_DATE, 'DD Month,yyyy')
FROM  EMPLOYEES;

--Display the salary of employee Neena with $ sign preceded.

SELECT CONCAT(FIRST_NAME , LAST_NAME) AS NAME, TO_CHAR(SALARY,'$99999999999') AS SALARY_DOLLARS
FROM EMPLOYEES;

--Find the next ‘Monday’ considering today’s date as date.

SELECT DATE_ADD(SYSDATE, INTERVAL 7 DAY) as NEXT_MONDAY;

--FROM EMPLOYEES;

--List all Employees who have an ‘A’ in their last names.

SELECT * FROM EMPLOYEES WHERE LAST_NAME LIKE '%a%';

--Show all employees’ last three letters of first name.
Select FIRST_NAME , SUBSTR(FIRST_NAME, -3) AS THREE_LETTERS
from employees ;
--
--For all employees employed for more than 100 months, display the employee
--number, hire date, number of months employed, first Friday after hire date andlast
--day of the month hired.

SELECT ROUND(MONTHS_BETWEEN (SYSDATE, HIRE_DATE), 0) AS EMPLOYED_Months,
        NEXT_DAY(HIRE_DATE, 'Friday') as NEXT_FRIDAY,
        LAST_DAY(HIRE_DATE) AS LAST_DAY
        
FROM EMPLOYEES

WHERE ROUND(MONTHS_BETWEEN (SYSDATE, HIRE_DATE), 0) > 100;


--CALCULATIONS TASK

--To display the employee number, name, salary of employee before and after 15%
--increment in the yearly salary. Name the calculated new salary as “Incremented
--Salary”. Do calculate the difference between before and after salaries & name this
--amount as “Incremented Amount”.

SELECT EMPLOYEE_ID, CONCAT(FIRST_NAME , LAST_NAME) AS NAME, SALARY, (SALARY * 0.15) AS INCREMENTED_AMOUNT , (SALARY+ (SALARY*0.15)) AS INCREMENTED_SALARY
FROM EMPLOYEES;
--
--List the name, hire date, and day of the week (labeled DAY) on which job was
--started. Order the result by day of week starting with Monday.
SELECT  CONCAT(FIRST_NAME , LAST_NAME) AS NAME, TO_CHAR(HIRE_DATE,'DD MONTH,YYYY') AS HIRE_DATE, DAYOFWEEK(HIRE_DATE) AS DAY
FROM EMPLOYEES;

--Display the department and manager id for all employees and round the commission
--up to 1 decimal.

SELECT DEPARTMENT_ID, MANAGER_ID, ROUND(COMMISSION_PCT, 1) 
FROM EMPLOYEES;

--Write a query to find the list of employees whose COMMISSION_PCT>0 and they do
--not belong to DEPARTMENT_ID 90 or 100 from Employees table

SELECT *
FROM EMPLOYEES
WHERE (COMMISSION_PCT > 0 ) AND (DEPARTMENT_ID != 90 OR DEPARtMENT_ID != 100);

--Write a query to find the employees who are hired in year 2010 from Employees table.
SELECT  EXTRACT(YEAR FROM HIRE_DATE) AS HIRE_YEAR
FROM EMPLOYEES;
WHERE EXTRACT(YEAR FROM HIRE_DATE) = '2010';

--Write a query to find the list of jobs whose min salary is greater than 8000 and less than
--15,000 and commission = 0 from job table.

SELECT *
FROM JOBS, EMPLOYEES
WHERE MIN_SALARY > 8000 AND MIN_SALARY < 15000 AND COMMISSION_PCT IS NULL;

--Write a query to find employee whose ID are greater than 100 and less than 150 and
--their department_id is greater than 90 and less than 100 along with their first_name,
--Last_name & Job ID.
SELECT FIRST_NAME, LAST_NAME, EMPLOYEE_ID, DEPARTMENT_ID, JOBS.JOB_ID
FROM EMPLOYEES, JOBS
WHERE (EMPLOYEES.EMPLOYEE_ID >= 100 AND EMPLOYEES.EMPLOYEE_ID <= 150) AND (EMPLOYEES.DEPARTMENT_ID >= 90 AND EMPLOYEES.DEPARTMENT_ID <= 100);

--Write a query to find total salary (Total salary formula = salary + (commission_pct*
--salary)) as “Total Salary”, commission_pct where commission_pct is not equal to null.


SELECT EMPLOYEE_ID, (SALARY+(COMMISSION_PCT*SALARY)) AS TOTAL_SALARY
FROM EMPLOYEES
WHERE COMMISSION_PCT IS NOT NULL;