# Sample BGP/MLAG/Varp Playbook

1) Install the needed roles by creating a text file:

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
The above command will install the need roles required to run the play book.

2) The playbook can be executed by running:

```
ansible-playbook -i hosts site.yml
```

The ```site.yml`` playbook is divided into to two child playbooks ```spine.yml``` and ```leaf.yml```.  As their name implies ```spine.yml``` will run against hosts in the spine group and ```leaf.yml``` will run against hosts in the leaf group.

To feed the correct IP addresses/username/acls into the play change the requiste host_var or group_var file to meet your needs.

For example if my host file looks like this:

```
[leaf]
dc1-tora
dc1-torb

[spine]
dc1-spine1
dc1-spine2
```

If I needed to change the IP address that will be configued on dc1-spine1 I would edit the ```host_var/dc1-spine1``` file.
