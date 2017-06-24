Ansible Role: EPEL
==================

[![Build Status](https://travis-ci.org/giovtorres/ansible-role-epel.svg?branch=master)](https://travis-ci.org/giovtorres/ansible-role-epel)

Installs the `epel-release` package on EL 6 and 7 platforms.

Requirements
------------

None.

Role Variables
--------------

Whether the EPEL repo should be installed or not.  Set to `absent` to remove
from the system.  Defaults to `present`.

    epel_state: present

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-role-epel

License
-------

BSD
