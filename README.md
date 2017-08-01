# Sample BGP/MLAG/Varp Playbook

Install the needed roles by creating a text file:

```
# roles.txt
arista.eos-bgp
arista.eos-bridging
arista.eos-interfaces
arista.eos-ipv4
arista.eos-mlag
arista.eos-route-control
arista.eos-system
arista.eos-virtual-router
arista.eos-vxlan
```

```
sudo ansible-galaxy install -r roles.txt
```
