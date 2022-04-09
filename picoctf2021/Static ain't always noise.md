#general-skills
<hr>

#### Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/static)? This [BASH script](https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/ltdis.sh) might help!

#### Solve
1. wget https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/static
2. wget https://mercury.picoctf.net/static/0f6ea599582dcce7b4f1ba94e3617baf/ltdis.sh
3. chmod +x ltdis.sh
4. ./ltdis.sh static
5. cat static.ltdis.strings.txt | grep pico 
6. picoCTF{d15a5m_t34s3r_6f8c8200}