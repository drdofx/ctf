#cryptography
<hr>

#### Description

A musician left us a [message](https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt). What's it mean?

#### Solve
1. wget https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt
2. Take each coordinate and perform reverse geocoding with any tools. In this case, I wrote a simple python code by utilizing locationiq API.
3. From each location result, get its city. If it doesn't exist, get the province. Else, get the county
4. picoCTF{KODIAK_ALASKA}