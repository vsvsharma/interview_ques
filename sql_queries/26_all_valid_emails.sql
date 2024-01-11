--Problems URL(https://leetcode.com/problems/find-users-with-valid-e-mails/description/)
SELECT *
FROM users
WHERE REGEXP_LIKE(mail,'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$')