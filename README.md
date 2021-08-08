# Role Name

Installs or removes packages from distribution repositories.

## Requirements

None.

## Role Variables

Default variables are set in `defaults/main.yml`.

## Dependencies

No dependency on other Ansible Galaxy roles.

## Example Playbook

```yml
---
- hosts: servers
  var:
    package_install:
      - vim
    package_remove:
      - nano
  roles:
    - role: hspaans.package
      become: true
```

## License

MIT

## Author Information

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).
