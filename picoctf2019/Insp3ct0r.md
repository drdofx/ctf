#web-exploitation
<hr>

#### Description

Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/44924/` ([link](https://jupiter.challenges.picoctf.org/problem/44924/)) or http://jupiter.challenges.picoctf.org:44924

#### Solve
1. Open inspect on browser
2. in index.html (found the first part):
``` html
<div id="tababout" class="tabcontent" style="display: none;">
	<h3>How</h3>
	<p>I used these to make this site: <br>
	  HTML <br>
	  CSS <br>
	  JS (JavaScript)
	</p>
	<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
</div>
```

3. in mycss.css (found the second part)
``` css
#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }

/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

4. in myjs.js (found the last part)
``` js
window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?f10be399} */
```

5. combine them: picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}