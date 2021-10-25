SELECT
CASE
    WHEN (select count(*) from Employee) = 1 THEN null
    ELSE (select salary from employee
          group by salary
          order by salary desc
          limit 1 offset 1
         )
END as SecondHighestSalary

