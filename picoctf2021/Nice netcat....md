#general-skills
<hr>

#### Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 21135`, but it doesn't speak English...

#### Solve
1. nc mercury.picoctf.net 21135 | tee ascii.txt 
2. cat ascii.txt (and copy all ascii text to decode in some online tools or own scripts)
3. picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}