class Value:
    def __init__(self):
        self.value = 0

    def __get__(self, obj, obj_type):
        return int(self.value)

    def __set__(self, obj, value):
        self.value = value - obj.commission * value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.5)
new_account.amount = 10000

print(new_account.amount)
