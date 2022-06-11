## [Jamboard Link] (https://jamboard.google.com/d/1xU5urhuyO24RN3zqcTneqa-bvDH7gInC-9BDUXhjjZE/edit?usp=sharing)

## Network Namespace Basics
### See list of namespaces
`lsns`
### Create network namespaces
`sudo ip netns add ETHC`
### Check network namespaces
`sudo ip netns`
### Turn up localhost inside network namespaces
`sudo ip netns exec ETHC ip link set dev lo up`
### Check address of localhost inside network namespaces
`sudo ip netns exec ETHC ip address`
### Ping testing localhost inside network namespaces
`sudo ip netns exec ETHC ping -c10 127.0.0.1`
### Create a virtual link
`sudo ip link add v-enp2s0 type veth peer name v-eth0`
### Attach one end of the virtual link to the network namespace
`sudo ip link set v-eth0 netns ETHC`
### Assign IP to the host end of virtual link
`sudo ip -n ETHC addr add 10.0.1.0/24 dev v-eth0`
### Turn up the virtual link
`sudo ip -n ETHC link set v-eth0 up`
### firewall inside network namespace
`sudo ip netns exec ETHC sudo ufw status`
### Delete namespace
`sudo ip netns del ETHC`


## Mininet Basics
### Check
`sudo mn`
### Cleanup
`sudo mn -c`
### Use tree topology
`sudo mn --topo=tree,depth=3,fanout=2`
