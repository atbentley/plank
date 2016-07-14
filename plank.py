import inspect
import importlib
import os
import sys

import click

__version__ = '0.0.1'


class NoisySet(set):
    def add(self, x):
        if x in self:
            return False
        super(NoisySet, self).add(x)
        return True


class Task(object):
    def __init__(self, func):
        self.func = func

        self.has_been_run = False
        self.pre_req_tasks = []

    @classmethod
    def make(cls, func_or_task):
        if isinstance(func_or_task, cls):
            return func_or_task
        else:
            return Task(func_or_task)

    def has_circular_dependency(self, visited_tasks=None):
        visited_tasks = visited_tasks or NoisySet([self])
        for pre_req_task in self.pre_req_tasks:
            if not visited_tasks.add(pre_req_task) or pre_req_task.has_circular_dependency(visited_tasks):
                return True
        return False

    def run(self):
        if self.has_been_run:
            return

        for pre_req_task in self.pre_req_tasks:
            pre_req_task.run()

        self.has_been_run = True
        return self.func()


def task(task_func):
    return Task.make(task_func)


class depends(object):
    def __init__(self, *pre_req_tasks):
        self.pre_req_tasks = pre_req_tasks

    def __call__(self, task_func):
        task = Task.make(task_func)
        for pre_req_task in self.pre_req_tasks:
            if pre_req_task not in task.pre_req_tasks:
                task.pre_req_tasks.append(pre_req_task)
        return task


def get_tasks():
    sys.path.insert(0, os.getcwd())
    planks = importlib.import_module('planks')
    sys.path.pop(0)
    tasks_map = {}
    for name, member in inspect.getmembers(planks):
        if isinstance(member, Task):
            tasks_map[name] = member
    return tasks_map


def materialise_pre_req_tasks(tasks):
    for task in tasks.values():
        task.pre_req_tasks = [tasks[name] for name in task.pre_req_tasks]


@click.command()
@click.argument("task")
def plank_runner(task):
    tasks = get_tasks()
    materialise_pre_req_tasks(tasks)
    task = tasks.get(task)
    if task.has_circular_dependency():
        raise Exception("Circular dependency detected")
    task.run()


if __name__ == '__main__':
    plank_runner.main()
