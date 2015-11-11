# Sample BGP/MLAG/Varp Playbook

This playbook requires the arista.eos role version v1.2.0 and pyeapi v0.4.0

Install the needed roles by creating a text file:

```
# roles.txt
arista.eos
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
