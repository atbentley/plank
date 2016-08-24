from plank import task


@task
def package():
    from distutils.core import run_setup

    run_setup('setup.py', script_args=['sdist'])
