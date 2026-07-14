SELECT
    category,
    COUNT(account_id) AS accounts_count
FROM
(
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
) AS c
LEFT JOIN Accounts
ON (
    (category = 'Low Salary' AND income < 20000)
    OR
    (category = 'Average Salary' AND income BETWEEN 20000 AND 50000)
    OR
    (category = 'High Salary' AND income > 50000)
)
GROUP BY category;