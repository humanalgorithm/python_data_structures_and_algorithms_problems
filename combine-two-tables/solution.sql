# Write your MySQL query statement below


select p.Firstname, p.LastName, a.City, a.State from Person p LEFT OUTER JOIN Address a
ON p.PersonId = a.PersonId
