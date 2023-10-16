# CozyHosting
* time for another easy challenge *eyeroll* 
* ip 10.10.11.230

## NMAP
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

## Services
* oh boy, a webserver. Gonna try navigating to it
* nothing

## exploits
* nginx 1.18.0 (Ubuntu)
  * CVE-2020-12440
    * request smuggling
    * abnormal HTTP request, which middleware hardware like firewalls and proxy can interpret improperly, allowing attacker to smuggle a request without the devices being aware. No auth
    * looks like we gotta construct an http request
    * eg, a firewall interprets same set of bytes as a different message than the web server
    * allows
      * web cache poisoning attack
      * firewall bypass
      * invoke script on page that returns client credentials
    * nginx is a reverse proxy, maybe this is useful?
    * what does nmap -p- 10.10.11.230 -o deep_scan.nmap say?
    * the website redirects to cozyhosting.htb
    * add the ip and hostname to the hosts file