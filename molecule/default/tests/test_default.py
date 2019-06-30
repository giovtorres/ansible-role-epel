import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_epel_repo_conf(host):
    f = host.file("/etc/yum.repos.d/epel.repo")
    assert f.exists
    assert f.is_file


def test_epel_gpg_key(host):
    if host.system_info.release.startswith("7"):
        assert host.package("gpg-pubkey-352c64e5-52ae6884").is_installed
    if host.system_info.release.startswith("6"):
        assert host.package("gpg-pubkey-0608b895-4bd22942").is_installed


def test_epel_repo_enabled(host):
    cmd = "yum -v repolist epel"
    assert "Repo-status  : enabled" in host.check_output(cmd)
