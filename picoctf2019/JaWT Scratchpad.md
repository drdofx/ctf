#web-exploitation
<hr>
#### Description

Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/58210/` or http://jupiter.challenges.picoctf.org:58210

#### Solve
1.  Access the url and type any name (except admin)
2. Copy jwt from cookies
3. Open linux to use John the Ripper
4. Get rockyou.txt from Github (simple google search)
5. Copy jwt to a new txt file called jwt.txt
6. Run `john jwt.txt --wordlist=rockyou.txt --format=HMAC-SHA256`
7. Get `ilovepico` as the secret key for the jwt
8. Go to `jwt.io`  and paste the jwt, change payload of `user` to `admin` and then put the `ilovepico` as the secret key
9. Copy the jwt result and replace the jwt in cookies with that
10. Refresh the page and get picoCTF{jawt_was_just_what_you_thought_44c752f5}