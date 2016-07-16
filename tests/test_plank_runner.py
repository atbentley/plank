import pytest
from fluentmock import create_mock, verify, when

from plank import Task, plank_runner, CircularDependencyError


@pytest.fixture
def tasks(monkeypatch):
    task_a = create_mock(Task, pre_req_tasks=['task_b'])
    when(task_a).has_circular_dependency().then_return(False)
    task_b = create_mock(Task, pre_req_tasks=[])
    when(task_b).has_circular_dependency().then_return(False)
    tasks = {'task_a': task_a, 'task_b': task_b}
    monkeypatch.setattr('plank.get_tasks', lambda: tasks)
    return tasks


def test_materialise_pre_req_tasks(tasks):
    plank_runner.main(['task_a'], standalone_mode=False)

    assert tasks['task_a'].pre_req_tasks == [tasks['task_b']]


def test_check_for_circular_dependencies(tasks):
    when(tasks['task_a']).has_circular_dependency().then_return(True)

    with pytest.raises(CircularDependencyError):
        plank_runner.main(['task_a'], standalone_mode=False)


def test_plank_runner_should_run_task(tasks):
    plank_runner.main(['task_a'], standalone_mode=False)

    verify(tasks['task_a']).run()
