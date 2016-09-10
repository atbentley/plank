from plank import task


@task
def install_requirements():
    import pip
    pip.main(['install', '--upgrade', '-r', 'requirements.txt', '-r', 'build-requirements.txt'])


@task
def check_requirements():
    import pip
    pip.main(['list', '--outdated'])
