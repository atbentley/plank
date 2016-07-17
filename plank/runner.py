from .errors import TaskNotFound, CircularDependency
from .inspector import Inspector


class Runner(object):
    def __init__(self, inspector=None):
        self.inspector = inspector or Inspector()

    def run(self, task_name):
        tasks = self.inspector.get_tasks()
        task = tasks.get(task_name)
        if not task:
            raise TaskNotFound('Could not find task: {0}'.format(task_name))
        if task.has_circular_dependency():
            raise CircularDependency('Circular dependency detected in task: {0}'.format(task_name))
        task.run()
