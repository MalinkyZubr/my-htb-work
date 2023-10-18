# Wifinetic
* easy lab on hackthebox
* IP 10.10.11.247
* we search for a 32 hex character string..
  
# Nmap scan
21/tcp open  ftp        vsftpd 3.0.3
22/tcp open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
53/tcp open  tcpwrapped

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

## vsftpd 3.0.3
* CVE-2021-30047 
  * DOS attack
* doesnt seem useful to us

## Openssh 8.2p1
* CVE-2023-28408
  * emote code execution if agent forwarded to attacker

## tcpwrapped
* this service is tcpwrapped, blocking us from connecting via tcp
* port 53 is DNS
* this means the DNS server is configured for TCP, not UDP

### Getting access
* try logging into ftp server, just for kicks since I have no other ideas
* try to login
* anonymous login only? set username to anonymous
* im in
* theres a tar file here, lets check it out!
  * backup-OpenWrt-2023-07-26.tar
  * wifi password is VeRyUniUqWiFIPasswrd1! according to config file 'wireless'
  * passwd file
    * root
    * nobody
    * netadmin
    * try wifi password on user accounts
      * netadmin used the wifi password as his password
  * profile file
    * no root password defined on device? setup new password to prevent unauthorized ssh? goody

* reaver allows retrieval of wpa keys. How does this work? This is due to a wps vulnerability that allows for brute forcing

* wash -i (monitoring interface) is useful for identifying interfaces that have wps enabled
* its always a good idea to check for WEP enabled interfaces that might eb vulnerable!!
* flaw in how the random numbers are generated