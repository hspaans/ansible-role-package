"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("pkg", ["zip"])
def test_pkg_installed(host, pkg):
    """Test if package installed."""
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("pkg", ["bzip2"])
def test_pkg_not_installed(host, pkg):
    """Test if package installed."""
    package = host.package(pkg)

    assert not package.is_installed
