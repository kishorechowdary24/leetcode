# Write your MySQL query statement below
select customer_id,
       COUNT(*) AS count_no_trans
from Visits v
LEFT JOIN Transactions t
    ON t.visit_id = v.visit_id
WHERE t.transaction_id is NULL
GROUP BY customer_id