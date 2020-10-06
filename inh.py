class ConcatList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ConcatList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(f'{order} bla bla {self.name}')


# x = Supplier('mm', 'bla@bral.pl')
# x.order(1)


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(Contact)
        self.phone = phone


class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print('Calling method on Base Class')
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        #super().call_me()
        print('Calling method on Left Subclass')
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        #super().call_me()
        print('Calling method on right Subclass')
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        # super().call_me()
        print('Calling method on Subclass')
        self.num_sub_calls += 1

s = Subclass()
s.call_me()

print(s.num_sub_calls, s.num_right_calls, s.num_left_calls, s.num_base_calls)




# class LongNameDict(dict):
#     def longest_key(self):
#         longest = None
#         for key in self:
#             if not longest or len(key) > len(longest):
#                 longest = key
#         return longest
#
# longkeys = LongNameDict()
# longkeys['hello'] = 1
# longkeys['kjasdhkajsdh'] = 5
#
# print(
# longkeys.longest_key()
# )
