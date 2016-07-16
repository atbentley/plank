from plank import task


@task
def unit_tests():
    import pytest

    exit_status = pytest.main(['tests'])

    if exit_status != 0:
        raise Exception('Unit tests failed')
