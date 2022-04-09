#web-exploitation
<hr>

#### Description

There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/40742/` ([link](https://jupiter.challenges.picoctf.org/problem/40742/)) or http://jupiter.challenges.picoctf.org:40742. Try to see if you can login as admin!

#### Solve
1.  First, send POST request to https://jupiter.challenges.picoctf.org/problem/40742/login.php with request key of debug=1
2. The SQL query: SQL query: SELECT * FROM admin where password = ' '
3.  After sending request with password key set to anyhing, I found that every password is encrypted before being given to SQL query and it's using `ROT13`
4. Encrypt `' or ''='` with any ROT13 tools and get `' be ''='`
5. Send it in password key POST request
6. Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}