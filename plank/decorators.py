from .task import Task


__all__ = ['task', 'depends', 'description']


def parameterised(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


def task(task_func=None):
    if task_func:
        return Task.make(task_func)
    else:
        def wrapped(task_func):
            return Task.make(task_func)
        return wrapped


@parameterised
def depends(task_func, *pre_req_tasks):
    task = Task.make(task_func)
    for pre_req_task in pre_req_tasks:
        if pre_req_task not in task.pre_req_tasks:
            task.pre_req_tasks.append(pre_req_task)
    return task


@parameterised
def description(task_func, description):
    task = Task.make(task_func)
    task.description = description
    return task
