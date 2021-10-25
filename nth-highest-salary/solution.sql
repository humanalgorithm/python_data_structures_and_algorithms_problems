CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
IF (select count(distinct(salary)) from employee) < N THEN
    return null;
END IF;

return (SELECT DISTINCT(salary) AS salary FROM Employee
         ORDER BY salary DESC
         LIMIT N, 1
        );
END
