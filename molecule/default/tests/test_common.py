import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_etc_folder(host):
    f = host.file('/etc')

    assert not f.is_symlink
    assert not f.is_pipe
    assert not f.is_file
    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755
