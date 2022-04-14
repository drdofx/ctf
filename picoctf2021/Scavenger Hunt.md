#web-exploitation
<hr>

#### Description

There is some interesting information hidden around this site [http://mercury.picoctf.net:39698/](http://mercury.picoctf.net:39698/). Can you find it?

#### Solve
1. In index.html --> `<!-- Here's the first part of the flag: picoCTF{t -->`
2. In mycss.css --> `/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */`
3. In myjs.js --> `/* How can I keep Google from indexing my website? */`
4. Go to /robots.txt --> `# Part 3: t_0f_pl4c`, `# I think this is an apache server... can you Access the next flag?
5. Go to /.htaccess --> `# Part 4: 3s_2_lO0k`, `# I love making websites on my Mac, I can Store a lot of information there.`
6. Go to /.DS_Store --> `Congrats! You completed the scavenger hunt. Part 5: _fa04427c}`
7. Construct flag => `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_fa04427c}`
