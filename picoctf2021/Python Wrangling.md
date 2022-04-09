#general-skills
<hr>

#### Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/ende.py) using [this password](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/pw.txt) to get [the flag](https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/flag.txt.en)?

#### Solve
1. wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/ende.py
2. wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/pw.txt
3. wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/flag.txt.en
4. `python3 ende.py -d flag.txt.en` and input password from pw.txt or `cat pw.txt | python3 ende.py -d flag.txt.en`
5. picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}