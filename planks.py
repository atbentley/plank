from plank import task


@task
def tests():
    import pytest

    exit_status = pytest.main(['tests', '--cov', 'plank'])

    if exit_status != 0:
        raise Exception('Unit tests failed')
