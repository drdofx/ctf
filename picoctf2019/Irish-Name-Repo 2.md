#web-exploitation
<hr>

#### Description

There is a website running at `https://jupiter.challenges.picoctf.org/problem/53751/` ([link](https://jupiter.challenges.picoctf.org/problem/53751/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:53751

#### Solve
1.  First, send POST request to https://jupiter.challenges.picoctf.org/problem/53751/login.php with request key of debug=1
2. The SQL query: SELECT * FROM users WHERE name=' '  AND password=' ' (**Same as before**)
3. Do SQL Injection by sending POST request with username=`' or ''='` and password=`' or ''='`  --> Failed
4. Some research on https://portswigger.net/web-security/sql-injection: Subverting application logic. send POST with username=`admin'--`
5. The SQL query: SELECT * FROM users WHERE name='admin'--' AND password='admin'
> The key thing here is that the double-dash sequence `--` is a comment indicator in SQL, and means that the rest of the query is interpreted as a comment. This effectively removes the remainder of the query... (portswigger)
6. Your flag is: picoCTF{m0R3_SQL_plz_c34df170}