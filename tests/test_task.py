import pytest
from plank import Task


def test_make_should_convert_function_to_task():
    def task_func():
        pass

    task = Task.make(task_func)
    assert isinstance(task, Task)
    assert task.func == task_func


def test_make_is_idempotent():
    task = Task(None)
    assert Task.make(task) == task


def test_run_only_runs_once():
    class SideEffect(Exception):
        pass

    def task_func():
        raise SideEffect

    task = Task(task_func)

    with pytest.raises(SideEffect):
        task.run()

    task.run()  # no exception raised second time because it didn't run


def test_self_referential_dependency_is_detected():
    task = Task(None)
    task.pre_req_tasks = [task]

    assert task.has_circular_dependency()


def test_immediate_dependency_is_detected():
    task_a = Task(None)
    task_b = Task(None)
    task_a.pre_req_tasks = [task_b]
    task_b.pre_req_tasks = [task_a]

    assert task_a.has_circular_dependency()
    assert task_b.has_circular_dependency()


def test_transitive_dependency_is_detected():
    task_a = Task(None)
    task_b = Task(None)
    task_c = Task(None)
    task_a.pre_req_tasks = [task_b]
    task_b.pre_req_tasks = [task_c]
    task_c.pre_req_tasks = [task_a]

    assert task_a.has_circular_dependency()
    assert task_b.has_circular_dependency()
    assert task_c.has_circular_dependency()


def test_no_dependency_is_detected():
    task_a = Task(None)
    task_b = Task(None)
    task_c = Task(None)
    task_a.pre_req_tasks = [task_b]
    task_b.pre_req_tasks = [task_c]

    assert not task_a.has_circular_dependency()
    assert not task_b.has_circular_dependency()
    assert not task_c.has_circular_dependency()
