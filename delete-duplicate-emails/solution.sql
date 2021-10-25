# Write your MySQL query statement below
delete from Person
where id not in (
    select id from(
        select min(p.id) as id
        from Person p
        group by p.email) as derived)

