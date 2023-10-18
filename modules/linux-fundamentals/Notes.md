### Linux Structure
#### Core Principles
1. everything is a file
2. small single purpose programs
3. chain programs together to perform complex tasks
4. no limiting user interfaces. use shell
5. configuration data is stored in a text file

#### main components
* bootloader: start the OS
* Kernel: manages relations between software and hardware
* Daemons: background programs, core software functions. automatically run in background
* shell: command line interpreter, bash
* graphics server: X-server, allows graphical programs to run locally or remotely
* window manager: GUI, gnome, kde, mate. Desktop environment and support for windowing
* Utilities: auxiliary programs users or programs can use

#### Architecture
* Hardware
* Kernel
* Shell: execute kernel functions
* System Utility: make all OS functions available

#### File Hierarchy
* tree

1. /: root directory, contains all the files in the system
2. /bin: binaries
3. /boot: bootloader, kernel binary, key files for booting
4. /dev: device files, allow access to hardware on system
5. /etc: system and application config files
6. /home: all users have subdirectory here
7. /lib: library files shared to entire system
8. /media: USB and stuff mount to here
9. /mnt: same as media, but for temporary filesystems on computer. Like VM
10. /opt: third party tools and files go here
11. /root: home of root user
12. /sbin: sysadmin binaries
13. /tmp: temporary files, cleared at boot
14. /usr: other executables and stuff
15. /var: variable files, logs, emaisl, webapps, cron

### Misc things
* $ denotes user, # denotes root

### customizing bash
* using special characters we can change the information the command line provides us while we enter commands
    1. \d, date
    2. \D{%Y-%m-%d}, mmddyy format date
    3. \H full hostname
    4. \j number jobs
    5. \n newline
    6. \r carriage return
    7. \s shell name
    8. \t current time 24 hr
    9. \T 12 hour time
    10. \@ current time
    11. \u username
    12. \w absolute PWD
* this can be designed with bashrcgenerator
* these are stored in the PS1 environment variable
  * PS1='\s:\u' means the prompt will look like bash:username.
  * you could write aliases or scripts to dynamically change this based on current task?

### Getting help
* most commands have --help arguments, and a manpage with `man command`
* `apropos (command)` is like a brief manpage
* https://explainshell.com/ can take a command input and describe what every command and argument does

### informational commands
* `hostname`: get hostname
* `id`: displays username and group information
* `uname`: display low level kernel and system information
* `ifconfig` network interface information
* `ip` manipulate routing, net devices, tunnels, interfaces
* `netstat` network information
* `ss` show socket
* `ps` show process information
* `who` is logged in?
* `env` prints environment variables or sets/executes commands
* `lsblk` show block devices
* `lsof` what files are open?
* `lspci` show PCI devices
* `lsattr` shows some information about the file
* `chattr` to add other things. immutability for instance on file

### Some file information
* when running `stat` on a file, 'inode' is the index of the file, the system unique identifier to that file

### Command tricks
* `cd -` takes you to the last directory you were in
* `(command) && (command)` will execute both commands, only if the first command is successful though

### Editing
* vimtutor to learn about it
* very efficient editor

### Locating
* `which (name)`
  * find the files of a program
* `find`
  * allows location of files by name, size, and other attributres
  * `find -perm o=s 2>/dev/null` identifies all suid binaries
* `locate`
  * quick to search through all syste, files based on local DB
  * update this with `sudo updatedb`
  * not as powreful filtering as find though

### file descriptors and redirection
* file descriptor indicated connection by kernel to support IO. Filehandle in windows.
* 0 is stdin, 1 is stdout, 2 is stderr
* we can redirect any one of these elsewhere
* `find silly 2>/dev/null` ignores permission denied errors for instance
* we can also redirect to files, different io handles can be redirected to different files
* '>>' appends to a file instead of overwriting/creating the file
* we can also define  astream to the redirected to file. `cat << (end delimeter) > file.txt` means we will enter consecutive lines of input until we enter the end of stream string, after which the whole thing writes to a file.
  * why does this work? creates a here document, a file, which cat reads. the file doesnt close, so cat keeps reading until the end delimiter is found, when you enter it. When the delimeter is found, the output gets redirected to the file
* `wc`: count number of occurences of certain things, like line count

### Pagers
* allows interactive viewing of large blocks of text
* `more` is the basic pager that just scrolls through text
* `less` is just more expanded
* `head` prints the first 10 lines of the file
* `tail` does the same but for the end of the file
* `sort` sort the input by any number of metrics, alphabetical by default
* `grep`
  * get results that match a specified pattern
  * grep 'x\|y' looks for x or y in the input
  * `grep -v` returns all lines which do not match the pattern
* `cut`
  * characters can become separator delimiters
  * for instance, if we have  astring of text with : separating words. The delemeter can be sepcified with `-d"(delimeter)"`.
  * this splits the string by the delimeter into an array. To get elements, do `-f(index)`
  * index starts at 1
* `tr`
  * replace characters in a line with other pieces of text
  * `tr "(delimeter) "(what to replace with)"`
* `column`
  * when many rows of text are separated by spaces, we can display it as a chart
  * `column -t` takes input and displays it in tabular form
* `awk`
  * allows advanced filtering of text with AWK scripting 
  * `awk '{print $1, $NF}` prints the first and last results of a line of text, words separated by spaces
* `sed`
  * stream editor for substituting text
  * looks for patterns in regex and replace with a string
  * `sed 's/bin/HTB/g`
  * search for bin in the input and replace it with HTB
  * 's' specifies substitute. First / deliniates patter to match, 2nd for the replacement, then g to replace all matches

### Regex
* very annoying but very powerful
* 3 principles
1. grouping
   1. (): group parts of expression. All patterns in here are processed together
   2. '[a-z]' define character classes. Specify list of characters to earch for
   3. {1,10} number or range to say how often previous pattern should execute
2. and
   1. .* only display if both expressions match
3. or
   1. | or, self explanatory

* examples
  * "(my|false)" search for line with my or false inside
  * "(my.*false)" search for a line with my and false inside

### Permissions
* who can access a file?
* read, write, execute, set
* to access directory, must have execute permissions  
  * this does not mean you can add or remove anything from the directory
* permissions can be set for owner, group, and others
* output of `ls -l`
  * 1 root root 1641 May  4 23:42 /etc/passwd
  * 1 is # hard links
  * root 1 is the owner
  * root 2 is the group
* `chmod` to change permissions for u, owner, g, group, o, others, and a, all users. Also add + or - to add or remove permissions
* for example, `chmod a+r` gives the group a, all, read rights, r
* we could also use the octal value for this assignment, 754

* to change the owner of a file, use `chown`
* `chown <user>:<group> <file>`

* the other two special permissions, SUID and SGID allow users to become other users during runtime of programs. the S replaces the x for executable

* sticky bits are file permission for directory
* extra security for control deletion and renaming
* shared directories/files to prevent accidental changing of shared resource
* setting sticky bit allows only owner of file, dir or root to edit file.
* If the t is lowercase, all users still have execute permissions
* if the T is capital, nobody but the aforementioned users have execute rights

### managing users
* `sudo` execute command as different user
* `su` requests user creds and switches to the user ID (superuser by default). then shell executed
* `useradd` create user or update default new user info
* `userdel` delete a user
* `usermod` modify user
* `addgroup` adds group
* `delgroup` remove group
* `passwd` change user password

### Package Management
* must know how to manage 3rd party software
* features of package manager:
  * package download
  * dependency resolution
  * standard package format for binaries
  * common installation locations
  * additional system functions
  * quality control
* options
  * dpkg: managing and installing debian packages. Use aptitude for user friendliness
  * apt: "advanced package manager", silly acronym and high level management interface
    * uses APT cache database
    * `apt-cache search (package)` shows everything related to a package
    * `apt-cache show (package)` shows detailed package info
    * `apt list --installed` lists installed packages
  * aptitude: dpkg alternative
  * snap: secure distributions of apps. Good for IoT and servers
  * gem: ruby package manager

* what is a package?
  * archive containing .deb files, installed with dpkg. apt works on top of dpkg
  * apt finds and installs dependencies by itself
  * linux system updates are conducted using apt
    * the packages list can be optained from /etc/apt/sources.list

* using wget
  * `wget (link to raw github page)` download individual programs and directories from github repo

### Service and Process
* internal services are hardware and kernel related, user services do user defined tasks, like servers and stuff.
* user services are daemons, identified by letter d at end of program name. 'sshd', 'systemd'
* systemd is the init daemon, starts at machine startup with PID 1
  * manages other services
* PID is process ID, PPID is parent process ID

* to start a service, `systemctl start (service name)`
* `systemctl start ssh` starts openssh server
* to see status of a service, `systemctl status (service name)`
  * this will display logs also
* service operations can be modified in config
* how can we run something on startup?
  * add to the SysV script to tell system to run on startup
  * `systemctl enable (service name)`
* we can see running processes with `ps` tool
* `systemctl list-units --type=service` list all services
* `systemctl stop (service)` to stop
* to read logs of a service, use the `journalctl` tool

* systemd units and unit files
  * unit is any resource system knows how to operate and manage
  * object of systemd interest
  * standardized representatives for system resources
  * these add many features for activation of services, security, dependency handling (parent child processes)
  * units are stored as unit files

* process can be in one of 4 states: running, wating (for event or resource), stopped, and zombie (stoped but with an entry in process table)
* `kill`, `pkill`, `pgrep`, `killall` kill process
* we will using signal IDs. These determine what happens as the process is killed

* background processes
  * after a program starts, ctrl z suspends it
  * to make it run again, enter `bg`
  * this will allow us to run commands as the program is running, even if it is printing to sdout
* you can also just add the & to the end of the command
* `jobs` lists all background commands
* to bring job from background, do `fg (id)`

### Task SCheduling
* allows taks and jobs to be scheduled to be executed later
* automates functions effectively 
* systemd can do some of the scheduling using timers
    1. createa  timer for systemd
       1. made in /etc/systemd/system/(timername).d
       2. edit it, but only use the timername without .d
    2. configure the timer
        [Unit]
        Description=My Timer

        [Timer]
        OnBootSec=3min // how long after boot to run
        OnUnitActiveSec=1hour // how often between runs during OS runtime

        [Install]
        WantedBy=timers.target
    3. create a service
       1. /etc/systemd/system/(timername).service
        [Unit]
        Description=My Service

        [Service]
        ExecStart=/full/path/to/my/script.sh // path to script the service represents

        [Install]
        WantedBy=multi-user.target

    4. reload system with `systemctl daemon-reload`
    5. then enable the service

* cron
  * another scheduler
  * execute tasks at specific times or at intervals
  * all we need to do is create a script then tell the daemon to call it
  * to use cron, we must store tasks in the crontab file
  * then we configure the daemon
  * every entry in cron has these
    1. minutes 0-59
    2. hours 0-23
    3. days 1-31
    4. months 1-12
    5. days of week 0-7

* example crontab file

```
# System Update
* */6 * * /path/to/update_software.sh

# Execute scripts
0 0 1 * * /path/to/scripts/run_scripts.sh

# Cleanup DB
0 0 * * 0 /path/to/scripts/clean_database.sh

# Backups
0 0 * * 7 /path/to/scripts/backup.sh
```
* system update service runs every 6th hour
  * denoted by /6
* execute scripts executes midnight the 1st day of the month
* cleanup db executed every sunday (0th day of the week) at midnight (0th hour 0th minute)
* backups is also executed every sunday at midnight
* we could also setup notifications for task completion, or create logs to minitor execution

### Network Services
* allow for interaction
* ssh
  * secure transmission of data nad commands
  * openssh server allows for usage
  * securely manage remote systems without being next ot he system
* NFS
  * network file system
  * allows storing and managing files on remote systems
  * NFS servers include nfs-utils, nfs-ganesha, opennfs
  * `sudo apt install nfs-kernel-server`
  * configures in the /etc/exports file
    * Specifies what directories should be shared
    * transfer speed
    * encryption
    * access rights:
      * rw: read write permissions for directory
      * ro: read only access to directory
      * no_root_squash: elevates root user beyond normal user rights
      * root_squash: root user must abide by user rules
      * sync: changes only transferred across the network after being saved by the client making the change
      * async: transfer data asyncrhonosuly. Increased speed, ,aybe inconsistencies in file system
    * to create a shared directory
      * `mkdir (directory)`
      * `echo '/home/user/nfs_sharing hostname(rw,sync,no_root_squash)`
      * then we can mount this to our NFS shared file system based on target IP and path
      * sometimes we can escalate priveleges using NFS
* web server
  * criticial web app infrastructure, targets for attack
  * provides internet function using HTTP
  * apache, nginx, lighttpd, caddy
    * of these, apache is the most popular
  * they can do:
    * transfer files
    * remote access
    * phishing
  * apache has many features to improve app design experience
    * installation `sudo apt install apache2`
    * to specify what files can be accessed, edit the apache2.conf file directory field
    * we could put files in the specified directory and then wget them down to us
  * .htaccess allows for more specific management
* python web server is a good alternative, easier. 
  * `sudo ap tinstall python3`
  * `python3 -m http.server`
  * starts on tcp8000
  * ew can also specify the --directory argument to tell the server what directories it can access
* VPN
  * direct encrypted access to a central computing resource
  * openvpn and l2tp ipsec are the two most popular
  * secure remote access
* openvpn to connect to internal networks
  * configure using openvpn.conf
  * to connect using openvpn, use the openvpn file received from server
  
### Communicating with web services
* cURL allows file transfer over HTTP, HTTPS, FTP, SFTP, FTPS, and SCP. 
  * test websites
  * tailor individual requests and examine responses
* wget is an alternative
  * download from ftp or http

### Redundancy and backups
* efficiently protect data while allowing easy access to that data
* tools
  * rsync
    * quickly secure backups
    * good for large network data transfers
  * deja dup
    * graphical backup tool
    * simplified process
    * uses rsync
  * duplicity
    * graphical backup, focuses on security. uses duplicity in backend. FTP
* encrypt backups!
  * gnuPG, ecryptfs, LUKS
  * essential to protect data
* rsync backup commands
  * `rsync -av (my directory) user@backupserver:(remote directory)`
  * we can customize this process to add compressions, repeated backups and such
  * to restore a backup, we just reverse the order of the remote and local direectory in the first command
  * to secure the transfer, we can add ssh after -av
  * to do auto synchronization combine rsync and cron

### File System Management
* support for ext2,3,4, xfs, btrfs, ntfs formats.
* all offer unique benefits and drawbacks.
* which we choose depends on our intentions
* in hierarchy of files, inode table at the top
  * metadata on filesystem. Allows quick management of files by OS
* files are either files or directories
  * directories are collections of files
  * every file has permissions
* links can be used to access files in different parts of the system

* disk management is managing hardware storage
  * HDD and SSD
  * `fdisk` tool. Manage partitions
  * `fdisk -l` shows partition information
  * divide physical space to logical sections
  * each partitiion gets a format, as metnioned before
  * `gpart` and `gparted` are also good partitioners
* mounting
  * every partition must be assigned a directory
  * attach partition to directory so its accessible
  * `mount` tool. running the command by itself lists all mounted devices
  * when mounted, it can be accessed like any directory
  * /etc/fstab defines what systems are mounted at boot time
  * we can use mount to mount a usb to the main fileysstem
  * `unmount` will unmount a file system as the name suggests 
  * unmounting when a process is using that file system is bad, check that there are no processes running in the filesystem using `lsof`
  * by adding an entry to the fstab file, we can allow for auto unmounting at shutdown

* SWAP space
  * very importent to runtime
  * when primary memory depleted
  * kernel transfer inactive memory pages to swap space, allowing other data to occupy main memory
  * used when installing operating systems
  * also invoked using `mkswap` and swapon commands
  * `swapon` activates area. Size fo swap space is user preference, hwo much space do you need?
  * should be in its own file partition
  * swap space should be encrypted, sensitive data is stored here sometimes!
  * data is also stored in swap space when the system sleeps, instead of just wiping main memory
  
### Containerization
* create deploy and manage applications easily
* container security is essential for data integrity on containers
* isolate containers from system
* see script for docker install
* building docker image is done with dockerfile
  * instructions for engine
  * can use container as file hosting server
    * for this, container with apache and ssh running
    * scp from the server to system
* the dockerfile is just linux commands to tell the image what to do
* convert this to image using `build`
  * executes the script
  * error=abort
  * `-t` for image tag
* `docker run` to run container
* docker provides many mangemetn commands
  * `docker ps` list running containers
  * `docker stop` stop a container
  * `docker start` start a container
  * `docker restart` restart a contianer
  * `docker rm` remove container
  * `docker rmi` remove image
  * `docker logs` to view container logs
* we can do docker image inheritance using the FROM (image) statement
* changes made during runtime are reverted when shutdown
  * this necessitates orchestration tools

* Linux containers
  * LXC
  * many isolated linuxes on a single host
  * resource isolation, `cgroups`, `namepsaces`
  * combined with docker, very powerful
  * differ in approach, image building, portability, ease of use, and security

* LXC manually build a new root filesystem with proper configs and packages
  * not easily portable
  * more configuration
* Docker is on top of LXC
  * better interface
  * portable
* `sudo apt-get install lxc lxc-utils` for lxc installation
  * `sudo lxc-create -n linuxcontainer -t (type, like ubuntu)` to create container
    * on another note, entering the template as 'download' will bring up a list of templates to choose from to execute the command
  * `lxc-ls` list containers
  * `lxc-stop -n (container)` stop container running
  * `lxc-start -n (container)` start container
  * `lxc-restart -n (container)` 
  * `lxc-config -n (container) -s (storage/network/security)` container mgmt
  * `lxc-attach -n (container)` connect to container
  * `lxc-attach -n (container) -f (filepath)` connect and share filepath
* good for configuration testing
* also can run on any host machine
* set up sepcific software versions for testing. If a service is running outdated apache server, we can spin up the same server version in our container and test against it
* test malware and exploits in controlled environment
  * for malware, must restrict access and configure security!
  * isolate the container! mandatory access control!
* access
  * ssh or console
  * disable unecessary services
  * we could remove openssh-server to disable ssh service
  * since container shares kernel resources, it has access to those
  * use cgroups to limit memory consumption
* configuration
  * container configurations are in `/usr/share/lxc/config/container_name.conf`. 
  * we must make this usually

```
lxc.cgroup.cpu.shares = 512
lxc.cgroup.memory.limit_in_bytes = 512M
```

* limits cpu and memory consumption. 
* cpu shares is cpu time container cna use compared to others. 1024 is the default, the maximum cgroup cpu time. 512 means it consumes half of cgroup cpu time
* to apply changes to an lxc config file, restart lxc.service with systemctl

* LXC use namespaces for isolation of processes, networks, file systems from host
  * namespace are abstraction of system resources
  * isolating containers made more secure
  * each container gets a PID number space away from system process ids
  * each container have separate network interface and firewall
  * all container activity is separate from host activity
* container has root directory, mnt
  * separate from host root, low chance that it influences host operations.

### Network Config
* 3 types of access control
  * discretionary: DAC
  * mandatory: MAC
  * role based: RBAC
* TCP wrappers, selinux, apparmor
* network monitoring, syslogs, ss, lsof, elk
* configure network nterfaces with `ifconfig` and `ip`
* `ip addr` and `ifconfig` do the same thing basically
* activate interface: `sudo ifconfig (interface) up`
  * `sudo ip link set eth0 up`
* assign ip address
  * `sudo ifconfig (interface) (ip address)`
* assign netmask
  * `sudo ifconfig eth0 netmask 255.255.255.0`
* add default gateway
  * `sudo route add default gw (ip) (interface)`
* to edit DNS server list, go to `/etc/resolv.conf`
  * contains DNS information
* to edit interface config, go to `/etc/network/interfaces`
  * here we can configure what ip addresses the interfaces will request using DHCP

* DAC discretionary access control
  * provide access and manage risks of unauthroized access
  * grant resource owners responsibility for their own resources
* MAC mandatory access control
  * define rule to delineate resource access
  * access based on security level of user
  * every process assigned security clearance
  * 0 trust frameworks
  * no unauthorized access
* RBAC role based access control
  * assign permissions to users
  * simplified version of MAC
  * more flexible
  * access based n role rather than identity or ownership
  * many users, large organizations

* monitoring
  * capture network traffic and analyze behavior
* troubleshooting
  * diagnose and resolve network issues
  * ensure network operations
  * `ping`
  * `traceroute`
    * no response represented by 3 ***, maybe because down or blocking port
  * `netstat`
    * show active connections on ports
  * `tcpdump`
  * `wireshark`
  * `nmap`
* common problems
  * network connection issiues
  * dns resolution failure
  * packet loss
  * network performance 
* misconfiguration, damage, bad settings, unpatched firmware
* we use these to our advantage

### Hardening
* SELinux, app armor, tcp wrappers
* selinux
  * MAC control system in linux kernel
  * enforce policy defining access for every file
  * limit damage compromised process can do
* apparmor
  * MAC system
  * linux security mode application
  * application profiles defining resources application can access (application metadata)
  * easier to use than selinux
* tcp wrappers
  * host based network AC method
  * restrict access to services by IP address. Is this just a firewall? NO
    * firealls deal with packet flow at protocol level. TCP wrappers work solely on IP address

### Remote Desktop Protocols
* graphial remote access
* XServer
  * user side of x window system network protocol
  * XServer is how GUI communicates with kernel
  * the desktop is dependent on the kernel internal network
  * x11 unencrypted without ssh
  * to do this, add `X11Forwarding yes` to the /etc/ssh/sshd_config file
  * X11 Vulnerabilities are very dangerous. Allow surveillance and arbitrary code execution
* XDMCP
  * udp 177
  * communicate between x terminals, linux only
  * very weak encryption
  * vulnerable to MITM
* VNC
  * virtual network computing
    * RFB protocol
    * fairly secure
    * VNC servers are divided into the graphical and authentication servers
  * TCP 5900
  * tigerVNC is the most stable
    * `xfce4 xfce4-goodies tigervnc-standalone-server`
    * `vncpasswd` to configure password
    * creates the .vnc folder.
    * must create xstartup and config
      * xstartup determines how VNC session created
      * config determines settings
      * xstartup needs executable rights
    * `vncserver` to start
    * we must create an ssh tunnel, then connect to the same port and host as the ssh tunnel using xtightvncviewer
  * Gnome connections are unsable

### Security
* keep updates
* use firewall or iptables to restrict traffic
* ssh server should disable password login and root login
* set up sudoers, no root login
* least privelege system
* use fail2ban to do an action if too many login attempts
* audit system regularly, check for bad cron, manually update kernel if needed
* SELinux and AppArmor. Access control
* other tools: `snort`, `chrootkit`, `rkhunter`, `lynis`

1. remove unecessary services and software
2. remove unencrypted services
3. enable NTP and syslog for logging
4. each user has its own account
5. enforce strong passwords
6. password aging, restrict use of previous passwords
7. lock accounts after login failures
8. disable as many SUID and SGID binaries as possible

* TCP wrappers
  * allows control to what IPs can access device on what services
  * /etc/hosts.allow allowed IPs
  * /etc/hosts.deny
  * example:
    * sshd : 192.168.1.0/24
    * anyone on the 192.168.1.0 network can access sshd service
    * ALL : .inlanefreight.com
    * anyone in the inlanefreight.com domain can access all services
    * ftpd : 192.168.1.15
    * single host can access

### Firewall
* filter incoming and outgoing traffic based on rules
* iptables allows for customizable protection and DOS protection
* netfilter framework
  * provide hooks to interfcept and modify traffic going in the system

* iptables
  * filter based on
    * ip 
    * port
    * protocol
  * nftables, ufw, firewalld.
    * these are more modern
    * nftables is modern syntax. Requires effort to go from iptables to this
    * ufw: uncomplicated firwall. better UI
    * Firewalld: complex configs
 
* Tables: organize firewall rules
  * organize based on traffic type
  * 3 tables: each have a different function on incoming and outgoing traffic
    * filter: filter traffic . Chains with input, forward and output
    * nat: modify source and destination IP/port, prerouting, postrouting
    * mangle: modify header fields. Uses all previous chains
* chains: group firewall rules together to make more complex rules
  * user defined
    * simplify rule management by grouping rules. Can be added to the main table chains
  * built in
    * filter
      * INPUT
      * OUTPUT
      * FORWARD
    * nat
      * PREROUTING
      * POSTROUTING
* rules: network traffic filterws
  * when do you filter, or do whatever to the packets?
  * add to chains using `-A`
  * contains matches and targets, what packets to capture, and what to do with them respectivley
* matches: match criteria for filters
* targets: action for packets that meet a match
  * accept: pass
  * drop: discard
  * reject: discard and send error to sender
  * log: save packet info
  * snat: modify source IP for NAT 
  * dnat: modify destination IP for NAT
  * masquerade: snat, but source IP is dynamic
  * redirect: redirect packets to different port or IP
  * mark: modifies netfilter mark for advanced networking

### logging
* log whether our attempt to intrude triggered security measures
* we must
  * configure proper log levels
  * log rotating (not all logs to to one giant file)
  * secure storage
  * review logs
* there are
  * kernel logs
    * hardware drivers, system calls, kernel events
    * reveal vulnerable drivers
    * reveal resource limitations
    * suspicious system calls
    * /var/log/kern.log
  * system logs
    * /var/log/syslog
    * service starting and stopping, failures
    * login attempts
    * reboots
    * access activites
  * auth logs
    * /var/log/auth.log
    * user authentication
    * identify security threats
    * identify compromises in system
  * app logs
    * application activities
    * /var/log/apache2/error.log for example
    * how applications process and handle data
    * potential vulnerabilities
    * access logs record user and process activity
      * who accessed a file when?
    * audit logs do security logging
  * security logs
    * logs made by security services. get logged to manhy files

### Solaris
* scalable, high fault tolerance unix based system used for critical missions
* proprietary
* uses ZFS, zettabyte file system, compression, snapshots, scaling
* SMF service management facility

### Display Managers
* loads destkop environment, ubuntu desktop
* gdm3
* disable guest account
* require users enter username and password for login
* auto login
* others are cdm, nodm, lightdm, xdm