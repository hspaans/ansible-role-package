"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("pkg", ["nano"])
def test_pkg_installed(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("pkg", ["joe"])
def test_pkg_not_installed(host, pkg):
    package = host.package(pkg)

    assert not package.is_installed
