arista.eos_bgp
==============

The arista.eos_bgp role leverages the modules provided in the arista.eos role to
quickly configure your BGP neighbors and networks.

Requirements
------------

None

Role Variables
--------------

The eos_bgp role assumes a certain object model as described below.  You can
put this object in group_vars or host_vars or dynamically gather this data
from a database; your choice.

BGP object

```
bgp:
  enable: [true, false]
  bgp_as: int
  redistribute:
    - list of redistribute statements
  log_neighbor_changes: [no, yes]
  timers:
    keep_alive: int
    hold: int
  neighbors:
    - name:
      remote_as: 65002
      peer_group: demoleaf
      enable: true
    - name: 10.1.1.3
      remote_as: 65002
      peer_group: demoleaf
      enable: true
  listeners:
    - name: 10.1.0.0/16
      peer_group: demoleaf
      remote_as: 65001
```


Example

```
bgp:
  enable: true
  bgp_as: 65001
  redistribute:
    - connected
    - static
  log_neighbor_changes: yes
  timers:
    keep_alive: 1
    hold: 3
  neighbors:
    - name: 10.1.1.1
      remote_as: 65002
      peer_group: demoleaf
      enable: true
    - name: 10.1.1.3
      remote_as: 65002
      peer_group: demoleaf
      enable: true
  listeners:
    - name: 10.1.0.0/16
      peer_group: demoleaf
      remote_as: 65001
```

The defaults/main.yaml creates a bgp object with no data


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
