# Write your MySQL query statement below




SELECT actor_id as ACTOR_ID, director_id as DIRECTOR_ID FROM ActorDirector
group by actor_id, director_id
having count(*) >=3
