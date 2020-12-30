# Role Name

Installs or removes packages from distribution repositories.

## Requirements

None.

## Role Variables

Default variables are set in `defaults/main.yml`.

## Dependencies

No dependency on other Ansible Galaxy roles.

## Platforms

The role is tested agains [LTS](https://en.wikipedia.org/wiki/Long-term_support) distribution versions with official support and fall within N and N-1.

| Platform | Versions       |
|:--------:|:--------------:|
| CentOS   | 7              |
| CentOS   | 8              |
| Debian   | 9 (Stretch)    |
| Debian   | 10 (Buster)    |
| Ubuntu   | 18.04 (Bionic) |
| Ubuntu   | 20.04 (Focal)  |

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
