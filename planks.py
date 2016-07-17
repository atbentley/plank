from plank import task


@task
def tests():
    import pytest

    exit_status = pytest.main(['--cov', 'plank', 'tests'])

    if exit_status != 0:
        raise Exception('Unit tests failed')
