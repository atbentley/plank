import plank


def test_self_referential():
    task = plank.Task(None)
    task.pre_req_tasks = [task]

    assert task.has_circular_dependency()


def test_immediate_dependency():
    task_a = plank.Task(None)
    task_b = plank.Task(None)
    task_a.pre_req_tasks = [task_b]
    task_b.pre_req_tasks = [task_a]

    assert task_a.has_circular_dependency()
    assert task_b.has_circular_dependency()


def test_transitive_dependency():
    task_a = plank.Task(None)
    task_b = plank.Task(None)
    task_c = plank.Task(None)
    task_a.pre_req_tasks = [task_b]
    task_b.pre_req_tasks = [task_c]
    task_c.pre_req_tasks = [task_a]

    assert task_a.has_circular_dependency()
    assert task_b.has_circular_dependency()
    assert task_c.has_circular_dependency()


def test_no_dependency():
    task_a = plank.Task(None)
    task_b = plank.Task(None)
    task_c = plank.Task(None)
    task_a.pre_req_tasks = [task_b]
    task_b.pre_req_tasks = [task_c]

    assert not task_a.has_circular_dependency()
    assert not task_b.has_circular_dependency()
    assert not task_c.has_circular_dependency()
