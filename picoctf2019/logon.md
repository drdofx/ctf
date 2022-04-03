#web-exploitation
<hr>

#### Description

The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/15796/` ([link](https://jupiter.challenges.picoctf.org/problem/15796/)) or http://jupiter.challenges.picoctf.org:15796

#### Solve
1. login with any user and password except Joe (or just empty it) and login
2. Change cookies value with name admin to True
3. Refresh page
4. **Flag**: `picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}`