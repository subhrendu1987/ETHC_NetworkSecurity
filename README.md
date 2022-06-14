# ETHC_NetworkSecurity: 
## Mininet Environment Setup

### Download Mininet
* Download mininet from [here](https://github.com/mininet/mininet/releases/)
	- Choose Image name: "mininet-2.3.0-210211-ubuntu-20.04.1-legacy-server-amd64-ovf.zip"
	- Extract the VM. After extraction you should have two files
		+ 'mininet-2.3.0-210211-ubuntu-20.04.1-legacy-server-amd64.ovf'
		+ 'mininet-vm-x86_64.vmdk'
### Install VirtualBox
* Install VirtualBox in your host system from [here](https://www.virtualbox.org/wiki/Downloads).
### Import Mininet VM
* Open your VirtualBox and import the mininet VM as follows.
	- Top Bar -> File -> Import Appliance
	- In the File textbox add the complete path to the 'mininet-2.3.0-210211-ubuntu-20.04.1-legacy-server-amd64.ovf' and press "Next"
	- In the next window press "Import" and wait till the process finishes.
	- After successful completion of "Import" start the VM 
### Configure Mininet VM
#### GUI Installation
Open a Terminal in the guest "Mininet VM" and use the commands one after another.
* `sudo apt update`
* `sudo apt install tasksel`
* `sudo tasksel install ubuntu-desktop`
* `sudo apt install lightdm` (Select lightdm as your default GUI manager if prompted)
* `sudo reboot`
#### SSH from Host (Optional)
* Power-off the VM and goto the VirtualBox window.
* Select the Mininet-VM and press "settings". In the side pane select "Network" and expand the "Advanced" option. Press "Port Forwarding". Add a new rule by selecting the "+" sign in the right pane of this window. Add the following values in the corresponding fields. 
	- `Name: Rule1`
	- `Protocol:TCP`
	- `Host Port: 2222`
	- `Guest Port: 22`
	- Leave rest of the fields as blank.
* Start the VM and open a terminal inside it. Use the following commands inside the VM.
	- `sudo apt update`
	- `sudo apt install openssh-server`
	- `sudo service sshd restart`
	