class Meta(type):
    def __init__(cls, name, bases, attrs):
        print('Initializing - {}, base {}'.format(name, bases))

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)


class Base(metaclass=Meta):
    pass


class A(Base):
    pass


class B(Base):
    pass


class C(A):
    pass


print(Base.registry)
print(Base.__subclasses__())