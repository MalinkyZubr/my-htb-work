# Web Requests
### HTTP
* applicaiton level protocol
* hypertext contains link to other resources
* client and server
* client requests server for resources
* server processes requests and returns resource
* URL contains a FQDN, fully qualified domain name

#### URL
1. scheme: http/s://
2. username:password@host:port
3. /path.html: path
4. ?login=true: query
5. #status: fragment
   1. locat sections within the primary resource

####
* cURL
* client URL
* http request client side
* `curl (url)`
* `-0` to write to file with website path name
* `-o` to speicfy file name

### HTTPS
* no more MITM
* wpa encryption
* after standard DNS exchange with client and DNS server.

1. client hello packet, client information
2. server hello, server information
3. key exchange, and ssl certificate excahnge
4. client verify certificate and sends its own
5. server verifies certificate
6. encrypted handshake to check that everythign is working

#### curl HTTPS
* curl works with HTTPs. will not work with expired server certs
* `-k` flag skips certificate check for testing purposes

### HTTP Request
#### core headers
1. Method: what action is performed?
2. path: path to accessed resource
3. version: what http version

#### optional headers
* host
* user agent
* redirect
* cookie

### HTTP response
* responds with response code
* can respond with HTML, JSON, XML, many others

### curl responses and requests
* `-v` flag for verbose to see full http responses
* `-vvv` is super verbose output
* this will also show good server information, like if apache or something


### Browser Dev Tools
* `ctrl shift i` to open dev tools on browser
* network tab for requests
* list requests sent by the page
* use filter URLs to search for specific request
* 

### HTTP HEaders in detail
* general headers
  * describe message, not contents
  * metadata
    * Date
    * Connection close:
      * should the connection be kept alive after request finishes?
        * keep-alive or close
* entity headers
  * describe the content of the message
  * post or put
    * content-type
      * resource type in transfer
      * text/html
    * media-type
      * similar to content type. Help server interpret our data
      * application/pdf
    * Boundary
      * separation marker when several parts of one message
      * b4e4fbd93540
    * content-length
      * how long is the data being sent
    * content-encoding
      * how is the data encoded so the server can decode it
      * compression, encoding schemes
      * gzip for instance
* request headers
  * unrelated to content
  * host
    * target host
  * user-agent
    * descirbe client requesting resource
    * curl, wget
    * reveals client, browser, OS
  * referer
    * where is the request coming from?
    * where is the client being redirected from
  * Accept
    * describes what media client understands
    * */* means all media accepted
  * Cookie
    * PHPSESSID=b4e4fbd93540
    * key value pair
    * data stored by client and server
    * identifier
    * passed to server on request to make sure the session maintains access
  * Authorization
    * cleint identification
    * token for lcient
    * only client side storage
  * https://tools.ietf.org/html/rfc7231#section-5
* response headers
  * HTTP response
  * server:
    * server which is handling client request
    * apache/2.2.14
  * set-cookie: cookie list for client ID.
    * same format as cookie request header
  * www-authenticate
    * notify client as to what kind of authentication required
* security headers
  * response headers to define the policies to be followed by client for security
  * content-security policy
    * dictate policy to injected resources
    * javascript or php
    * instructs browser to accept resources only from certain places
    * prevent XSS
    * script-src 'self'
  * strict transport security
    * prevent from accessing with http
    * prevent sniffing and https downgrading
  * referrer-policy
    * dictates if browser should include referer in header
    * prevent disclosing sensitive URLs

#### CURL headers
* `-l` response header
* `-I` send head request and only display response headers
* `-i` display headers and response body
* `-H` set request headers
* `-A` to set user agent

#### DevTools headers
* click on a request, then access different parts using the tabs
* 

### Methods
* define actions taken by server and client
* get
  * request specific resource
* post
  * sends data to server from client
  * handle data input
* head
  * rwquests headers from website
  * check response time
* put
  * create new resource
  * can allow uploading of malicious resource if not controlled
* delete
  * delete existing resource on webserver
  * lead to DOS if allowed to delete critical documents
* options
  * return information about the server
* patch
  * modifications to server resource

### Get
#### HTTP basic auth
* when the little popup comes asking for username and password
* handled directly by webserver to protect directories without directly interacting with the webapp
* to do this in curl:
  * `curl -u username:password (url)`

#### Authorization header
* after using http basic auth, authorization header is set to base64 of username:password
* in the case of JWT, authorization would be the bearer, carrying the token
* we can set the authorization with the -H flag
  * `curl -H 'Autorization: Basic username:passwordb64`

#### Get parameters
* using the network tab of the devtools, we can also see how the webpage communicates with backend resources, like with scripts and databases
* for instance, we might see that a call is made to search.php, we could just send a request directly to that after we see it in network tab
* devtools provides a neat trick
  * right click on request, then 'copy as cURL'
* we could also repeat the request in devtools by selecting copy as fetch. This copies it using javascript fetch. Then we paste this to devtools javascript console

#### Post
* to specify post request using curl:
  * `curl -X POST`
* when we need to transfer files we use post
* post places user parameters in http request body
  * this means:
    * no logging 
      * a full file doesnt get logged
    * less encoding
      * binary, characters, etc. Doesnt need to conform with URL formatting
    * larger data throughput

#### Login forms
* a php login form integrated with the webpage woudl use post requests, instead of basic http auth which used get
* some login forms just return the page logged into with the post request
* others will redirect. to accept redirects, specify the `-L` flag
* after successful auth, cookies will allow persistent auth
* to set cookie, use `-b` flag
  * `curl -b 'SILLY=SILLYSILLYFELLOWHEHEHE`
* the storage tab of the devtools will show us the cookies
* we can also add or remove cookies here
  * this can be used to replace cookies with authenticated ones

#### JSon
* format of post data

#### APIs
* APIs operate much the same as regular HTTP, just standardized
* read, write, update delete
* use paths to access specific resources, then run operations on them
* https://hehe/funny/silly
  * /funny/silly is a resource I can do things to, it is like an object for the API.