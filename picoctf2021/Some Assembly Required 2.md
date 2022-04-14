#web-exploitation
<hr>

#### Description

[http://mercury.picoctf.net:7319/index.html](http://mercury.picoctf.net:7319/index.html)

#### Solve
1. Open Inspect -> Source tab 
2. in wasm/3e1a8b4a, on the second last line there is a data `xakgK\5cNs9=8:9l1?im8i<89?00>88k09=nj9kimnu\00\00`
3. XOR it with number 8  and get `picoCTF{15021d97ae0a401788600c815fb1caef}`
