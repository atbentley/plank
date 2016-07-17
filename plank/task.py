class NoisySet(set):
    def add(self, x):
        if x in self:
            return False
        super(NoisySet, self).add(x)
        return True


class Task(object):
    def __init__(self, func):
        self.func = func
        self.has_been_run = False
        self.pre_req_tasks = []

    @classmethod
    def make(cls, func_or_task):
        if isinstance(func_or_task, cls):
            return func_or_task
        else:
            return Task(func_or_task)

    def has_circular_dependency(self, visited_tasks=None):
        visited_tasks = visited_tasks or NoisySet([self])
        for pre_req_task in self.pre_req_tasks:
            if not visited_tasks.add(pre_req_task) or pre_req_task.has_circular_dependency(visited_tasks):
                return True
        return False

    def run(self):
        if self.has_been_run:
            return

        for pre_req_task in self.pre_req_tasks:
            pre_req_task.run()

        self.has_been_run = True
        return self.func()
