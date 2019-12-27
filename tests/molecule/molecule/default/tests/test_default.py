import os

import testinfra
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def get_service_name(host):
    if host.system_info.distribution == 'freebsd':
        return 'ntopng'
    if host.system_info.distribution == 'openbsd':
        return 'ntopng'
    elif host.system_info.distribution == 'ubuntu':
        return 'ntopng'
    elif host.system_info.distribution == 'centos':
        return 'ntopng'
    raise NameError('Unknown distribution')


def get_ansible_vars(host):
    return host.ansible.get_variables()


def get_ansible_facts(host):
    return host.ansible('setup')['ansible_facts']


def is_docker(host):
    ansible_facts = get_ansible_facts(host)
    if 'ansible_virtualization_type' in ansible_facts:
        if ansible_facts['ansible_virtualization_type'] == 'docker':
            return True
    return False


def get_listen_ports(host):
    return [3000]


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root' or f.group == 'wheel'


def test_service(host):
    s = host.service(get_service_name(host))

    assert s.is_running
    assert s.is_enabled


def test_port(host):
    ports = get_listen_ports(host)

    for p in ports:
        # XXX host.socket() does not work on FreeBSD
        if not host.system_info.distribution == 'freebsd':
            assert host.socket("tcp://:::%d" % p).is_listening
