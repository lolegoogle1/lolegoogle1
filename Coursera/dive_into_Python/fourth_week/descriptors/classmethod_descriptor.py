class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        if owner is None:
            owner = type(instance)

        def new_func(*args, **kwargs):
            return self.func(owner, *args, **kwargs)

        return new_func

