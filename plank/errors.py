class PlankError(Exception):
    pass


class TaskNotFound(PlankError):
    pass


class CircularDependency(PlankError):
    pass
