import importlib
import inspect

from .task import Task


class Inspector(object):
    DEFAULT_PLANKS_MODULE_NAME = 'planks'

    def __init__(self, planks_module_name=None):
        self.planks_module_name = planks_module_name or self.DEFAULT_PLANKS_MODULE_NAME
        self.planks_module = None
        self.tasks = None

    def get_tasks(self):
        if self.tasks is None:
            self.inspect_planks_module()
        return self.tasks

    def inspect_planks_module(self):
        if not self.planks_module:
            self.import_planks_module()

        self.tasks = {}
        for name, member in inspect.getmembers(self.planks_module):
            if isinstance(member, Task):
                self.tasks[name] = member
        self.materialise_tasks()

    def import_planks_module(self):
        self.planks_module = importlib.import_module(self.planks_module_name)

    def materialise_tasks(self):
        for task in self.tasks.values():
            task.pre_req_tasks = [self.tasks[name] for name in task.pre_req_tasks]
