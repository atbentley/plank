import inspect
import importlib
import click

__version__ = '0.0.1'


def task(task_func):
    setup_task(task_func)
    return task_func


class depends(object):
    def __init__(self, *tasks):
        self.tasks = tasks

    def __call__(self, task_func):
        setup_task(task_func)
        for task in self.tasks:
            if task not in task_func._plank_depends:
                task_func._plank_depends.append(task)
        return task_func


def has_circular_dependency(task_func, task_maps, visited_funcs=None):
    if not visited_funcs:
        visited_funcs = [task_func]
    for pre_req_task_func in [task_maps[task_name] for task_name in task_func._plank_depends]:
        if pre_req_task_func in visited_funcs:
            return True
        visited_funcs.append(pre_req_task_func)
        if has_circular_dependency(pre_req_task_func, task_maps, visited_funcs):
            return True
    return False


def setup_task(task_func):
    if not hasattr(task_func, '_plank'):
        task_func._plank = True
        task_func._plank_has_been_run = False
        task_func._plank_depends = []


def run_task(task_func, tasks_map):
    if has_circular_dependency(task_func, tasks_map):
        raise Exception('Circular dependency detected')
    for pre_req_task_name in task_func._plank_depends:
        pre_req_task_func = tasks_map.get(pre_req_task_name)
        if not pre_req_task_func._plank_has_been_run:
            run_task(pre_req_task_func, tasks_map)
    task_func()
    task_func._plank_has_been_run = True


@click.command()
@click.argument("task")
def plank_runner(task):
    tasks_map = {}
    planks = importlib.import_module('planks')
    for name, member in inspect.getmembers(planks):
        if getattr(member, '_plank', False):
            tasks_map[name] = member
    task_func = tasks_map.get(task)
    run_task(task_func, tasks_map)


if __name__ == '__main__':
    plank_runner.main()
