Role Name
=========

Installs or removes packages from distribution repositories.

Requirements
------------

None.

Role Variables
--------------

Default variables are set in `defaults/main.yml`.

Dependencies
------------

No dependency on other Ansible Galaxy roles.

Example Playbook
----------------

    - hosts: servers
      var:
        package_installed:
          - vim
        package_removed:
          - nano
      roles:
         - { role: hspaans.package, become: true }

License
-------

MIT

Author Information
------------------

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).
