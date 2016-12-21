import os

import click
import sys

from .inspector import Inspector
from .runner import Runner


def list_available_tasks(ctx, param, value):
    sys.path.insert(0, os.getcwd())
    if not value or ctx.resilient_parsing:
        return
    print('Available tasks:')
    tasks = Inspector().get_tasks()
    if any(task.description for task in tasks.values()):
        n = max(len(task.name) for task in tasks.values())
        for task in tasks.values():
            padding = ' ' * (4 + n - len(task.name))
            if task.description:
                print('{0}{1} - {2}'.format(padding, task.name, task.description))
            else:
                print('{0}{1}'.format(padding, task.name))
    else:
        for task in tasks.values():
            padding = '    '
            print('{0}{1}'.format(padding, task.name))
    sys.path.pop(0)
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
