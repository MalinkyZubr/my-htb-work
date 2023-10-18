# Web Applicaitons
* client server architecture
* front end, backend
* interconnected, realtime controllable applications

## WEbsite vs webapp
* website is a static webpage which requires manual reconfiguration
  * web 1.0
* webapp is dynamic, interactive, and supports communication between frontend and backend
  * web 2.0

## Webapp vs Native apps
* native apps run on the host OS
* webapps are platform indpednent
* webapps have version unity   
  * all users accessing the backend resources of a webapp are accessing the same version
* OS applications are faster
* greater capabilities
* hybrid applications are becoming more common

## Webapp distribution
* open source
  * wordpress
  * opencart
  * joomla
* closed source
  * wix
  * shopify
  * dotnetnuke
* open source can be customized to meet organizational needs, closed source frameworks are sold for specific purposes

## Risks
* verye accessible, vast attack surface
* automated tools scan for web apps with vulnerabilities
* greater complexity -> more vulnerability
* to find such risks, see the owasp web security testing guide
* most common procedures:
  * review HTML, CSS, JS. Find Sensitive data exposure and XSS. 
  * review backend from authenticated and unauthenticated perpective

## Webapp attacks
* vulnerable service
* windows remote code execution RCE
* file uploads allowing for code execution
* sql injection
  * active directory authentication
  * gain access to emails, usernames
* file inclusion
  * read source code of a page you shouldnt be looking at to find vulnerabilities
* insecure direct object referencing IDOR
  * access other users data because of poor access control (like on a linux system)
* broken access control
  * for instance, you are creating account. The request when creating specifies "roleid". If we set this to 1 in our own custom request, we could just make an admin account

## Web application Layout
* 3 primary layers
* web application infrastructure
  * structure of components, liek databases
* webapp components
  * the actual components, like UI/UX, Server
* Arhcitecture 
  * how are the parts connected?

### Infrastructure
* infrastructure setups -- models
  * client-server
  * one server
  * many servers - one database
  * many servers - many databases

#### Client server
* server hosts the app, and distributes it to all the clients
* app has frontend and backend, executed by clients and servers respectively

#### One server
* one or many applications + database are on a single server. Straightforward and easy, risky since everything is in the same place
* if any component compromised, all is compromised 
* if the server goes down, all services do to

#### Many servers one database
* database exists on an independent server to which all the other server compoennts connect from thir own server machines
* several web apps have a single database
* separation of concerns

#### Many servers many databases
* mesh where there are many servers and many databases
* each web app has separate data storage
* redundancy
* highly secure with proper configuration
* load balancers
  * nginx
  * apache
  * https://en.wikipedia.org/wiki/Load_balancing_(computing)

#### others
* serverless
* microservices

### Overview
1. client
2. server
   1. webserver
   2. web app logic
   3. database
3. services (microservice architecture)
   1. 3rd party integration
   2. web app integrations
4. functions (serverless)

### Architecture
* presentation
  * UI processes, DOM based, JS, CSS, HTML
  * DOM is document object model
* Application Layer
  * runs checks against user requests, permissions, request content
* Data layer
  * identify where data is stored, retrieve the data

#### Microservices
* independent components in a web application architecutre, usually running in separate containers, managed by a container orchestrator like kubernetes
* decompose the monolith of classic architectures to separate tasks
* intercommunication is stateless, request and response are independent
* data stored separately for each service
* service oriented
* different microservices can be written in different languages and still communicate. Allows flexibility, scalability, ease of deployment, and resilience
* https://d1.awsstatic.com/whitepapers/microservices-on-aws.pdf

#### Serverless
* cloud providers, AWS, GCP, Azure offer cloud hosting of webapps
* good idea to get some sort of cloud cert for career flexibility!

### Security
* vulnerabilities might be caused by architecture, rather than individual code

## Front end vs Back End
* front end
  * what the user sees and interacts with
  * visual concept web design
  * user interface design
  * user experience design
  * https://html-css-js.com/ is good for learning about this

* back end
  * drives the frontend
  * supplies the data which the frontend uses
  * stores persistent data
  * servers
    * hardware, containers, vms
  * web servers
    * apache, nginx
  * databases
  * development frameworks
  * different components can be divided into separate machines, or separate containers
  * main tasks
    * develop logic and services for back end
    * main code and functions of webapp
    * database management
    * implement libraries for web application
    * implement technical needs
    * APIs for communicaiton with frontend
    * integrate remote servers and cloud services to webapp

### SEcurity for front and backend
* input scrubbing to avoid injection
* whitebox pentesting:
  * pentest with access to source code
  * essential for application pentesting on frontend, since we can access frontent code
* blackbox pentesting:
  * pentesting without knowing source code
  * backend pentesting
  * doesnt apply if the webapp is open source and displayed on github

### 20 critical vulnerability
1. permitting invalid data into database
2. focusing on system as a whole
3. establishing personally developed security methods
4. treating security as last step
5. plain text password storage
6. weak passwords
7. unencrypted data in database
8. depending excessively on client side
9. optimism
10. permitting variables via URL path queries
11. trusting 3rd party code
12. hard coding backdoors
13. unverified sql injections
14. remote file inclusions
15. insecure data handling
16. unencrypted data
17. insecure cryptography
18. ignoring layer 8
19. review user actions
20. firewall misconfiguration

### OWASP top 10
1. broken access control
2. crypto failure
3. injection
4. insecure design
5. security misconfig
6. vulnerable outdated components
7. identification and authentication failures
8. software and data integrity failures
9. logging and monitoring failures
10. server side request forgery

## HTML
* HTML is the foundation for frontend
* web browser interprets html to display
* each html element contains other html elements
* every html element is enclosed in <> </>, a tag
  * tags can also have parameters 
  * <p id='para1'> 
  * these can be used for CSS to identify and format the element

### URL Encoding
* Percent encoding
* display page contents using ASCII.
* Replace unsafe ASCII characters with $code
* `'` encodes to %27. 
* ` ` encodes as + or %20
* https://www.w3schools.com/tags/ref_urlencode.ASP
* burp suite can encode and decode from URL format

### Elements
* <head>
  * contains elements that are not printed on page content section
  * page title, etc
* <body> 
  * contains page content
* <style>
  * hold CSS code
* <script>
  * hold JS code

* each of these is a document object model DOM
  * platform and langauge neutral interface allowing programs

* dom standard
  * core dom
    * standard for all document types
  * xml dom
    * standard for all xml
  * html dom
    * standard for html documents

* DOMs are document.head, document.h1, etc

* identifies where on page an object is

## CSS
* cascading style sheets
* alongside HTML to make things pretty

### Basics
* define styles of a class or type of HTML element
* header, body, etc
* font size, background color
* defines object traits with element {property:value}

### Usage
* quick calculations, deynically adjust the page properties, keystroke animations
* works with XML and SVG
* groundworks for mobile app development UI/UX

### Frameworks
* CSS frameworks include prebuilt design sheets
* optimized for webapp usage
  * bootstrap
  * sass
  * foundation
  * bulma
  * pure

## Javascript
* frontend mostly
* controls functionality of webpage
* loaded with <script type="text/javascript">
* you could also load code from another file
  * <script src="./script.js">
* JSFiddle is good for practicing javascript online
* AJAX allows advanced HTML request

## Sensitive Data Exposure
* Frontend attacks dont pose a threat to the abckend
* they do put clients at risk of being exploited if they are vulnerable
* front end vulnerability granting admin access, for instance
* https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure

### Sensitive Data Exposure
* availability of sensitive data in clear text to end user in source code.
* open developer tools with ctrl + u
* burpsuite can also see source code
* or you could just use curl...
* maybe passwords, hashes, and other stuff in here
* we can also examine external javascript code being imported with the network tab

### protection
* establish controls on what can be seen in source on the frontend
* 

## HTML injection
* much of the time sanitization only happens in the backend
* what about when data is onlyu received AND processed frontend?
* must validate user input

### HTML injection
* unfiltered user input displayed on page
* retrieve existing data from backend
* when input is controlled, user can submit HTML code and browser might show it as part of the page.
* Malicious HTML code
* phishing
* defacing
* without page sanitization, html injection and XSS are easy

## XSS
* INject javascript code

## Cross site equest forgery
* unfiltered user input
* xss to perform queries
* API calls on web app victim is authenticated to
  * perform actions as authenticated user
* http parameter attacks

### Common methods
* create a javascript payload automatically changing victim password to some arbitrary value
* when the user logs in using the link containing the javascript payload, it changes the account password and the attacker can control it

* attack admins and access their accounts

### prevention
* front end filtering
  * sanitization
    * remove special characters from input
  * validation
    * submitted data must be in valid requested format
* web app firewalls are also useful, but not infallible
* modern CSRF is harder, since browser have inbuild anti csrf which prevent automatic javascript execution (to replicate user behavior, like keystrokes)
* http headers and flags can also prevent automated requests
  * anti csrf token
  * http-only/X-XSS-Protection
* webapp might require MFA to change passwords also
* https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

## BAck end servers
* hardware and OS running webpage services
* web server
* database
* dev frameworks
* Vms, containers

* stacks:
  * LAMP: linux apache mysql php
  * WAMP: windows apache mysql php
  * WINS: windows iis .net SQL Server
  * MAMP: macos apache mysql php

## Web Servers
* Handles all http traffic from clients and forwards, or uses them to interface with server side resources

### Apache
* https://www.apache.org/
* httpd (http daemon)
* 40% share of websites
* PHP, .net, python, perl, bash

### NGINX
* 30% share of webpages
* concurrency, load balancing, asynchronicity
* relaibility
* very popular among big websites

### IIS
* Internet Information services
* 15% share
* microsoft native, windows server
* host web apps using .net
* active directory

## Databases
* store data
* speed, size, scalability, cost are all considerations

### Relational
* SQL
  * store data in tables, rows, columns
  * each table has unique keys linking tables together 
  * for instance, a message might have a UID attached to it, then you can search that UID in the users table
  * this makes it quick to find all data about someone 
* table relationships are called schemas

* MySQL: very common open source
* MSSQL: microsoft implementation of relational database
* Oracle: Reliable database for big business
* PostreSQL: Easily extensible, enabling adding advanced new features

### Non Relational NoSQL
* use other non relational storage models
* datastructures without much definition
  * key-value
  * document-based
  * wide-column
  * graph
* key value databases store data in json or XML
* document based stores data in json objects, each with metadata while storing the rest in key value model
  * basically key value + metadata
* MongoDB: document based model
* ElasticSearch: huge datasets. Very efficient
* Apache Cassandra: graceful handling of faulty values
* redis and neo4j are also nosql

### uses
* backend interfaces with database for storage and retrieval

## Dev frameworks
* programming libraries for developing the actual cod ebehind hte applications
  * Laravel: php
  * Express: Node.JS
  * Django: Python
  * Rails: Ruby

### APIs
* application program intercace
* specifies how application can interact with other application
* SOAP: 
  * simple objects access
  * share data with XML
  * good for transferring structured data
* REST:
  * representational state transfer
  * share data through the URL path and returns data in JSON


## Common vulnerabilities
### Broken authentication
* most common and dangerous vulnerabilitites 
* bypass authentication functions
* login without valid credentials, or allow user to become admin
* college management system 1.2 has sql broken auth injection vulnerability
* https://www.exploit-db.com/exploits/47388

### Broken access control
* allow attackers to access pages they shouldnt be able to

### Malicious FIle Upload
* file uploads, if not sanitized could contain malicious code
* wordpress plugin responsive thumbnail slider


# NOW
go build a webapp

1. 	Set up a VM with a web server
2. 	Create an HTML page
3. 	Design it with CSS
4. 	Add some simple functions with JavaScript
5. 	Program a simple web application
6. 	Connect your web application to the database
7. 	Experiment with APIs
8. 	Test your application for various vulnerabilities and security holes
9. 	Try to adjust your code and configurations to close the vulnerabilities