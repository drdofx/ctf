#web-exploitation
<hr>

#### Description

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:34561/](http://mercury.picoctf.net:34561/)

#### Solve
1. Open postman or other similar tools
2. Send request to http://mercury.picoctf.net:34561/index.php with HTTP HEAD method
3. in Headers, get "flag" key with value of picoCTF{r3j3ct_th3_du4l1ty_8f878508}