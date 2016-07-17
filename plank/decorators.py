from .task import Task


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
