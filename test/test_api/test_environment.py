import pytest

from jedi._compatibility import py_version
from jedi.api.virtualenv import Environment, DefaultEnvironment, NoVirtualEnv


def test_sys_path():
    assert DefaultEnvironment('/foo').get_sys_path()


@pytest.mark.parametrize(
    'version',
    ['2.6', '2.7', '3.3', '3.4', '3.5', '3.6', '3.7']
)
def test_versions(version):
    executable = 'python' + version
    try:
        env = Environment('some path', executable)
    except NoVirtualEnv:
        if int(version.replace('.', '')) == py_version:
            # At least the current version has to work
            raise
        return

    sys_path = env.get_sys_path()
    assert any(executable in p for p in sys_path)