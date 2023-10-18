# Traffic analysis
* tcpdump
  * command line utility with libpcap. Captures and interprets network traffic
* TShark
  * packet analyzer for capturing live network data
  * cli for wireshark
* gui verison of gshark
* ngrep
  * grep for web traffic
  * understand how to read live traffic or fraffic from pcap
  * regex and berkely packet filter syntax
* tcpick
  * command line packet sniffer
  * track and reassemble tcp streams
* network taps
  * gigamon, niagra-taps
  * man in the middle basically, analyze and forward packets, or forward them elsewhere for analysis
* network span ports
  * copy frames and packets during transmission, send to collection points
* elastic stack
  * full stack traffic analysis
* SIEMS
  * splunk
  * integrated analysis tool to detect threats as they come

### analysis workflow
1. ingest traffic
   1. capture packets
2. filter
   1. filter out unwanted data to naroow our search
3. analyze
   1. is traffic encrypted?
   2. are users attempting to access unauthorized resources?
   3. are there unusual traffic patterns?
4. detect root issue
   1. errors?
   2. malicious use?
   3. IDS and IPS to run ehuristics
5. fix and monitor

## TCPDump
* 