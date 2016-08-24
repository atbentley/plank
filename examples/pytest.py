# Run multiple test suites and combine the coverage report at the end.
# This example requires pytest and pytest-cov to be installed, it also assumes tests are organised as:
#   project-root
#   |_ tests
#      |_ unit
#      |_ integration
import os

from plank import task, depends


EXIT_SUCCESS = 0


@task
def unit_tests():
    import pytest
    exit_status = pytest.main(['--cov', 'plank', '--cov-report=', 'tests/unit'])
    os.rename('.coverage', '.unit.coverage')
    if exit_status != EXIT_SUCCESS:
        raise Exception('Unit tests failed')


@task
def integration_tests():
    import pytest
    exit_status = pytest.main(['--cov', 'plank', '--cov-report=', 'tests/unit'])
    os.rename('.coverage', '.integration.coverage')
    if exit_status != EXIT_SUCCESS:
        raise Exception('Integration tests failed')


@task
def coverage():
    import coverage
    cov = coverage.coverage()
    cov.load()
    cov.combine(['.unit.coverage', '.integration.coverage'])
    cov.save()
    cov.report()


@task
@depends('unit_tests', 'integration_tests', 'coverage')
def tests():
    pass
