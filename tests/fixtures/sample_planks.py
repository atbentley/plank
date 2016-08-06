from plank import task


@task
def raises_value_error():
    raise ValueError
