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
