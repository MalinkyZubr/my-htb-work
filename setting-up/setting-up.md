# setting up
* internal penentration test
  * from point of view of employee inside the network gaining access to restricted resources
  * needs a dedicated server from which to download tools and scripts, since the company will give a local machine to use
* remote
  * ship them device that will allow us to connect, or give them a VM
* up to date linux and windows vm
* windows for AD
* having standard VM increases efficiency

### Browsers
* we might have bookmarked websites for pentesting
* we might have browser based apps
* using firefox, we can save all of these with our account

### Maintenance
* keep software and OS up to date

### Note taking
* new information
  * new ip address, username, password, source code
* ideas for further tests and processing
  * record ideas
  * record things we notice or should be investigates
  * obsidian is very good for markdown notetaking, works on top of vscode
* scan results
  * too much information to process wthout notes
  * pwndoc containers are good for this
* logging
  * important to log what we do
  * what if the company is attacked during pentest? we cant prove we didnt cause the damage without logs
  * script is a good tool for this
    * every command saved to file
    * to display date and time, set PS1 variable in .bashrc to 
    * "\[\033[1;32m\]\342\224\200\$([[ \$(/opt/vpnbash.sh) == *\"10.\"* ]] && echo \"[\[\033[1;34m\]\$(/opt/vpnserver.sh)\[\033[1;32m\]]\342\224\200[\[\033[1;37m\]\$(/opt/vpnbash.sh)\[\033[1;32m\]]\342\224\200\")[\[\033[1;37m\]\u\[\033[01;32m\]@\[\033[01;34m\]\h\[\033[1;32m\]]\342\224\200[\[\033[1;37m\]\w\[\033[1;32m\]]\n\[\033[1;32m\]\342\224\224\342\224\200\342\224\200\342\225\274 [\[\e[01;33m\]$(date +%D-%r)\[\e[01;32m\]]\\$ \[\e[0m\]"
    * to start logging, `script <date>-<start_time>-<log name>.log`
  * windows equivalent is start-transcript
    * `Start-Transcript -Path (path to log file)`
  * logging also allows documentation and examination of process, to optimize with scripts later
  * tools like tmux and terminator allow logging of all commands and output
  * some tools support log writing
  * otherwise, use redirects for command output
* screenshots
  * flameshot
  * peek: gif recording

### Virtualization
* hardware
  * virtual machine. Make hardware components available without them physically being there
* applicaton
* storage
* data
* network

#### VMWARE
* vmware player can run one virtual machine at a time
* OVF open virtualization format files
  * used openly by many virtualization softwares

#### Virtualbox
* always encrypt VMs

#### Containers
* processes running on one host which make a complete application
* only stores binaries and libraries, not kernel
* containers are isolated
* scalability
* look into kubernetes

#### Docker
* docker engine:
  * interface host resources with running containers

#### Vagrant
* create, configure, manage virtual machines and environments
* VMs described in Vagrantfile

### linux
* we must have a standard for our linux environments
* we should have an OS ready before the test starts
* encrypt vms, like kali and parrot, logical volume mapper
  * LVM: flexible partitioning of storage resources
* to see the locations from which parrot downloads updates, `parrot repository`
* `cat tools.list` to see tools
	* these must be installed using sudo apt install (list of tools)
* after doing all installs, and configurations, good to take a snapshot
* `sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y` to fully upgrade a system