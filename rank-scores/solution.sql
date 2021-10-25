# Write your MySQL query statement below




Select s.score as Score, rankings.rowid DIV 1 as Rank from scores s,
(SELECT score, @rowid:=@rowid+1 as rowid
FROM (select * from scores group by score order by score desc) as grouped, (SELECT @rowid:=0) as init) as rankings
where s.score = rankings.score
order by rankings.rowid
