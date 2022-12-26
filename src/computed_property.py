class computed_property:
    def __init__(self, *args, **kwargs):
        self.properties = args

    def __call__(self, fn, *args, **kwargs):
        cls = self

        class fn_call:
            def __init__(self, *args, **kwargs) -> None:
                self.cached_value = None
                self.original_setter = None
                self.original_deleter = None

            def decorated_setter(self, instance, name, value):
                if name in cls.properties:
                    self.cached_value = None
                self.original_setter(instance, name, value)

            def decorated_deleter(self, instance, name):
                if name in cls.properties:
                    self.cached_value = None
                self.original_deleter(instance, name)

            def __set_name__(self, owner, *args, **kwargs):
                self.original_setter = owner.__setattr__
                self.original_deleter = owner.__delattr__
                owner.__setattr__ = lambda instance, name, value: self.decorated_setter(instance, name, value)
                owner.__delattr__ = lambda instance, name: self.decorated_deleter(instance, name)

            def __get__(self, obj, objtype=None):
                if self.cached_value:
                    return self.cached_value

                self.cached_value = fn(obj)
                return self.cached_value

        return fn_call()
