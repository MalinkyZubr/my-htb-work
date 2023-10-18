# windows command line
## introduction
* cmd and powershell are separate
* automation, exploitation, etc

### Command prompt vs powershell
* powershell
  * batch commands and powershell cmdlets
  * command aliasing supported
  * cmdlet output can be piped
  * all outputs are objects
  * cmdlets can be executed in scripts
  * integrated scripting environment
  * access loibaries built in the .net framework
  * linux compatible
* command prompt
  * only batch commands
  * no aliasing
  * no piping
  * only textual output
  * can script
  * no integrated scripting environment ISE
  * no access to .net
  * only windows
* ssh htb-student@<IP-Address> 

### CMD.exe
* C:\Windows\System32\cmd.exe
* windows r to open 
* we can access cmd.exe via the recovery boot
  * then we replace the stickey keys.exe with another copy of cmd.exe
  * if we enable stickey keys now, the cmd prompt opens with high priveleges