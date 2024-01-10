--Problems URL(https://leetcode.com/problems/bank-account-summary-ii/description/)
SELECT Users.name , SUM(Transactions.amount) AS balance
FROM Users
LEFT JOIN Transactions 
ON Users.account=Transactions.account
GROUP BY Users.name,transactions.account
HAVING SUM(Transactions.amount)>10000