from plank import Task, task, depends


def test_decorator_converts_function_into_task():
    @task
    def task_func():
        pass

    assert isinstance(task_func, Task)


def test_depends_sets_pre_req_tasks():
    @task
    @depends('other_task')
    def task_func():
        pass

    assert task_func.pre_req_tasks == ['other_task']
