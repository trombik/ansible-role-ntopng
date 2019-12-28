# `trombik.ntopng`

[![Build Status](https://travis-ci.com/trombik/ansible-role-ntopng.svg?branch=master)](https://travis-ci.com/trombik/ansible-role-ntopng)

`ansible` role for `ntopng`.

## Notes for Ubuntu users

`ntopng` from the official distribution package repository and one from the
ntop.org has differences. The major one is the path to `ntopng.conf`:
`/etc/ntopng.conf` for the former and `/etc/ntopng/ntopng.conf`. The default
of the role is `/etc/ntopng/ntopng.conf`.

# Requirements

# Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ntopng_package` | Package name of `ntopng` | `{{ __ntopng_package }}` |
| `ntopng_service` | Service name of `ntopng` | `{{ __ntopng_service }}` |
| `ntopng_extra_packages` | A list of extra package to install | `[]` |
| `ntopng_user` | User name of `ntopng` | `{{ __ntopng_user }}` |
| `ntopng_group` | Group name of `ntopng` | `{{ __ntopng_group }}` |
| `ntopng_extra_groups` | A list of extra groups for `ntopng_user` | `[]` |
| `ntopng_config_dir` | Path to the configuration directory | `{{ __ntopng_config_dir }}` |
| `ntopng_config_file` | Path to `ntopng.conf` | `{{ ntopng_config_dir }}/sshd_config` |
| `ntopng_config` | The content of `ntopng.conf` | `""` |
| `ntopng_flags` | See below | `""` |
| `ntopng_db_dir` | Path to database directory | `__ntopng_db_dir` |
| `ntopng_log_dir` | Path to log directory. Depending on the source of the package, this directory might not be used at all | `__ntopng_log_dir` |

## `ntopng_flags`

This variable is used for overriding defaults for startup scripts. In Debian
variants, the value is the content of `/etc/default/ntopng`. In RedHat
variants, it is the content of `/etc/sysconfig/ntopng`. In FreeBSD, it
is the content of `/etc/rc.conf.d/ntopng`. In OpenBSD, the value is
passed to `rcctl set ntopng`.

## Debian

| Variable | Default |
|----------|---------|
| `__ntopng_service` | `ntopng` |
| `__ntopng_package` | `ntopng` |
| `__ntopng_extra_packages` | `["net-tools"]` |
| `__ntopng_config_dir` | `/etc/ntopng` |
| `__ntopng_user` | `ntopng` |
| `__ntopng_group` | `ntopng` |
| `__ntopng_db_dir` | `/var/lib/ntopng` |
| `__ntopng_log_dir` | `/var/log/ntopng` |

## FreeBSD

| Variable | Default |
|----------|---------|
| `__ntopng_service` | `ntopng` |
| `__ntopng_package` | `net/ntopng` |
| `__ntopng_extra_packages` | `[]` |
| `__ntopng_config_dir` | `/usr/local/etc/ntopng` |
| `__ntopng_user` | `ntopng` |
| `__ntopng_group` | `ntopng` |
| `__ntopng_db_dir` | `/var/db/ntopng` |
| `__ntopng_log_dir` | `{{ __ntopng_db_dir }}` |

## OpenBSD

| Variable | Default |
|----------|---------|
| `__ntopng_service` | `ntopng` |
| `__ntopng_package` | `ntopng` |
| `__ntopng_extra_packages` | `[]` |
| `__ntopng_config_dir` | `/etc/ntopng` |
| `__ntopng_user` | `_ntopng` |
| `__ntopng_group` | `_ntopng` |
| `__ntopng_db_dir` | `/var/db/ntopng` |
| `__ntopng_log_dir` | `{{ __ntopng_db_dir }}` |

## RedHat

| Variable | Default |
|----------|---------|
| `__ntopng_service` | `ntopng` |
| `__ntopng_package` | `ntopng` |
| `__ntopng_extra_packages` | `[]` |
| `__ntopng_config_dir` | `/etc/ntopng` |
| `__ntopng_user` | `ntopng` |
| `__ntopng_group` | `ntopng` |
| `__ntopng_db_dir` | `/var/lib/ntopng` |
| `__ntopng_log_dir` | `/var/log/ntopng` |

# Dependencies

# Example Playbook

```yaml
```

# License

```
Copyright (c) 2016 Tomoyuki Sakurai <y@trombik.org>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

# Author Information

Tomoyuki Sakurai <y@trombik.org>
