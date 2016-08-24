from plank import task


@task
def publish():
    from devpi.main import main as devpi_client

    devpi_client(argv=['devpi', 'use', 'index_name'])
    devpi_client(argv=['devpi', 'login', 'username', '--password', 'password'])
    devpi_client(argv=['devpi', 'upload', 'path/to/sdist'])
