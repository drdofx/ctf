#web-exploitation
<hr>
#### Description

Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/44924/` ([link](https://jupiter.challenges.picoctf.org/problem/44924/)) or http://jupiter.challenges.picoctf.org:44924

#### Solve
1. Open /robots.txt
2. User-agent: *
Disallow: /8028f.html
3. go to /8028f.html
4. picoCTF{ca1cu1at1ng_Mach1n3s_8028f}