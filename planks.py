import os
import subprocess

from plank import task, depends


@task
def unit_tests():
    # Run tests in subprocess since we've imported some of the code we are testing
    # and coverage will not accurately reflect the lines we test
    exit_status = subprocess.check_call(['py.test', '--cov', 'plank', '--cov-report=', 'tests/unit'])
    os.rename('.coverage', '.unit.coverage')
    if exit_status != 0:
        raise Exception('Unit tests failed')


@task
def integration_tests():
    # Run tests in subprocess since we've imported some of the code we are testing
    # and coverage will not accurately reflect the lines we test
    exit_status = subprocess.check_call(['py.test', '--cov', 'plank', '--cov-report=', 'tests/integration'])
    os.rename('.coverage', '.integration.coverage')
    if exit_status != 0:
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


@task
def package():
    from distutils.core import run_setup

    run_setup('setup.py', script_args=['sdist'])
