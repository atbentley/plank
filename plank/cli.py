import os

import click
import sys
from plank import Inspector

from .runner import Runner


def list_available_tasks(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    tasks = Inspector().get_tasks()
    print 'Available tasks:'
    for task in tasks.values():
        print '\t{0}'.format(task.name)
    ctx.exit()


@click.command()
@click.argument('task')
@click.option('-l', '--list', is_flag=True, is_eager=True, expose_value=False, callback=list_available_tasks,
              help='List available tasks')
def main(task):
    sys.path.insert(0, os.getcwd())
    runner = Runner()
    runner.run(task)
    sys.path.pop(0)


if __name__ == '__main__':
    main.main()
