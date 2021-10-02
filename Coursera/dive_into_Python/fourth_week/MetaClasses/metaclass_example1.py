class Object:
    pass


class Meta(type):
    def __new__(cls, name, parents, attrs):
        print(f'Creating {name}, parents {parents}, attr {attrs}')

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()
            print(attrs)

        return super().__new__(cls, name, parents, attrs)


class A(Object, metaclass=Meta):
    pass


print('A.class_id: "{}"'.format(A.class_id))
