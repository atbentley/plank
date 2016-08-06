import pytest
from fluentmock import create_mock
from plank import Inspector


@pytest.fixture
def inspector():
    return Inspector()


def test_materialise_tasks_replaces_task_names_with_actual_tasks(inspector):
    task_a = create_mock(pre_req_tasks=['task_b'])
    task_b = create_mock(pre_req_tasks=[])
    inspector.tasks = {'task_a': task_a, 'task_b': task_b}
    inspector.materialise_tasks()

    assert task_a.pre_req_tasks == [task_b]
