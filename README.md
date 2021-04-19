Minirole
========

Sample minirole

Requirements
------------

Python

Role Variables
--------------

	---
	minirole__nginx_version: 1.18.0
	minirole__vhost_root: /var/www/
	minirole__app_content: Hello World


Dependencies
------------

No

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      vars:
        - minirole__app_content: Another Hello World
      roles:
         - minirole

License
-------

MIT

Author Information
------------------

Andrei
