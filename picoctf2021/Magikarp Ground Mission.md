#general-skills
<hr>

#### Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `a13b7f9d`

#### Solve
1. Launch instance and ssh to the challenge endpoint
2. cat 1of3.flag.txt -> picoCTF{xxsh_
3. cat instructions-to-2of3.txt **AND** cd /
4. cat 2of3.flag.txt -> 0ut_0f_\/\/4t3r_
5. cat instructions-to-3of3.txt **AND** cd ~
6. cat 3of3.flag.txt -> 71be5264}
7. Combine it: `picoCTF{xxsh_0ut_0f_\/\/4t3r_71be5264}`