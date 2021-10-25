# Write your MySQL query statement below



select d2.name as Department, e1.name as Employee, e1.salary
from employee e1, department d2 where (e1.departmentId, e1.salary) in
(select d.id, max(e.salary)
from employee e, department d
where e.DepartmentId = d.Id
group by e.DepartmentId)
and e1.departmentId = d2.id
