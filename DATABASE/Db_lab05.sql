---1. Write a query to list the name, job name, department name, salary of the
--employees according to the department in ascending order.
SELECT E.FIRST_NAME, J.JOB_TITLE, D.DEPARTMENT_NAME,D.DEPARTMENT_ID, E.SALARY 
FROM EMPLOYEES E, JOBS J, DEPARTMENTS D
WHERE E.JOB_ID = J.JOB_ID AND  E.DEPARTMENT_ID = D.DEPARTMENT_ID
ORDER BY E.DEPARTMENT_ID ASC;



--2. Write a query to list the department where at least two employees are working.

SELECT D.DEPARTMENT_ID, COUNT(*)
FROM DEPARTMENTS D, EMPLOYEES E
WHERE D.DEPARTMENT_ID = E.DEPARTMENT_ID
GROUP BY D.DEPARTMENT_ID
HAVING COUNT(*) >= 2;
--3. Fetch all the records where salary of employee is less than the lower salary.
SELECT E.*
FROM   EMPLOYEES E, JOBS J
WHERE E.JOB_ID = J.JOB_ID AND E.SALARY < J.MIN_SALARY;

--4. Write a query to list the name, job name, annual salary, department id,
--department name and city who earn 60000 in a year or not working as an
--ANALYST.
SELECT E.FIRST_NAME, J.JOB_TITLE, (E.SALARY*12) AS ANNUAL_SALARY , D.DEPARTMENT_ID, D.DEPARTMENT_NAME, L.CITY
FROM EMPLOYEES E, JOBS J, DEPARTMENTS D, LOCATIONS L
WHERE E.JOB_ID = J.JOB_ID AND D.DEPARTMENT_ID = E.DEPARTMENT_ID AND D.LOCATION_ID = L.LOCATION_ID AND ((E.SALARY*12)= 60000 OR J.JOB_TITLE != 'ANALYST');

--5. Write a query to print details of the employees who are also Managers.
SELECT  DISTINCT E.*
FROM EMPLOYEES E, EMPLOYEES M
WHERE E.EMPLOYEE_ID = M.MANAGER_ID ;

-- Task 6
SELECT b.DEPARTMENT_ID,
       count(a.DEPARTMENT_ID)
FROM departments b
LEFT OUTER JOIN employees a ON a.DEPARTMENT_ID=b.DEPARTMENT_ID
GROUP BY b.DEPARTMENT_ID
HAVING count(a.DEPARTMENT_ID) = 0;


-- Task 7
SELECT  first_name, last_name, employee_id, job_id  
FROM employees  
WHERE department_id = 
    (SELECT department_id  
    FROM departments 
    WHERE location_id = 
        (SELECT location_id 
        FROM locations  
        WHERE city ='Toronto'));


-- Task 8
SELECT  first_name, last_name, employee_id, job_id  
FROM employees  
WHERE department_id = 
(SELECT department_id  
FROM departments 
WHERE location_id = 
(SELECT location_id 
FROM locations  
WHERE city ='Toronto'));


-- Task 9
SELECT t1.first_name
FROM table1 t1
LEFT JOIN table2 t2 ON t2.name = t1.name
WHERE t2.name IS NULL

-- Task 10
SELECT country_name,city, COUNT(department_id)
    FROM countries 
        JOIN locations USING (country_id) 
        JOIN departments USING (location_id) 
WHERE department_id IN 
    (SELECT department_id 
        FROM employees 
     GROUP BY department_id 
     HAVING COUNT(department_id)>=2)
GROUP BY country_name,city);