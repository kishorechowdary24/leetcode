# Write your MySQL query statement below
SElECT m.employee_id, m.name, COUNT(*) AS reports_count, ROUND(avg(e.age), 0) AS average_age
FROM Employees m
JOIN Employees e ON m.employee_id = e.reports_to 
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id

