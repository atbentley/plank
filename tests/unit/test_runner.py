import pytest
from fluentmock import create_mock, when, verify

from plank import Runner, Inspector, Task, TaskNotFound, CircularDependency


@pytest.fixture
def happy_task():
    task = create_mock(Task)
    when(task).has_circular_dependency().then_return(False)
    return task


@pytest.fixture
def circular_dependency_task():
    task = create_mock(Task)
    when(task).has_circular_dependency().then_return(True)
    return task


@pytest.fixture
def inspector(happy_task, circular_dependency_task):
    inspector = create_mock(Inspector)
    when(inspector).get_tasks().then_return({'happy_task': happy_task,
                                             'circular_dependency_task': circular_dependency_task})
    return inspector


@pytest.fixture
def runner(inspector):
    return Runner(inspector=inspector)


def test_run_calls_task(runner, happy_task):
    runner.run('happy_task')

    verify(happy_task).run()


def test_run_raises_not_found_error(runner):
    with pytest.raises(TaskNotFound):
        runner.run('non_existant_task')


def test_run_raises_circular_dependency(runner):
    with pytest.raises(CircularDependency):
        runner.run('circular_dependency_task')
