import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_app_working(host):
    http = host.check_output('curl -L 127.0.0.1')

    assert 'Hello World' in http


def test_nginx_working(host):
    http = host.check_output('curl -I -L 127.0.0.1')

    assert '200 OK' in http


def test_nginx_pkg(host):
    pkg = host.package('nginx')

    assert pkg.is_installed
    assert '1.18.0' in pkg.version


@pytest.mark.parametrize(
    'path', [
        ('/etc/nginx/conf.d/default.conf'),
        ('/var/www/index.html'),
    ])
def test_minirole_files(host, path):
    assert host.file(path).exists
