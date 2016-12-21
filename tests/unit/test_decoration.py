from plank import Task, task, depends, description


def test_decorator_converts_function_into_task():
    @task()
    def task_func():
        pass

    assert isinstance(task_func, Task)


def test_lazy_decorator_converts_function_into_task():
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


def test_description_sets_description_on_task():
    some_description = 'lalala'

    @task
    @description(some_description)
    def task_func():
        pass

    assert task_func.description == some_description
