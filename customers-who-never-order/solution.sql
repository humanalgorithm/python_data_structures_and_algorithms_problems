# Write your MySQL query statement belo



select c.name as Customers from customers c where c.id not in (select distinct(customerId) from orders)
