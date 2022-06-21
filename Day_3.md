## Introduction to Protocol
### Assignment 


### Experiment 2
* Open `sudo mn -x`
* Inside h1.xterm `tcpdump`
* Inside h2.xterm `ping h1`
* Look into h1.xterm


### Experiment 3
* Open `sudo mn -x`
* h1.xterm -> `tcpdump -w h1.pcap`
* h2.xterm -> `python -m http.server`
* mininet  -> `h1 wget 10.0.0.2:8000`
* h1.xterm -> `^c` (Stop tcpdump)
* h2.xterm -> `^c` (Stop http.server)
* GUI      -> Open h1.pcap with wireshark
