import click

from .runner import Runner


@click.command()
@click.argument('task')
def main(task):
    runner = Runner()
    runner.run(task)
