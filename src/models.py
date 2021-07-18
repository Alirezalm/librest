from abc import ABC
from datetime import datetime


class BaseMember(ABC):
    _mem_id = 0


class Member(BaseMember):
    def __init__(self, name: str, family: str, address: str, phone: str, age: int):
        BaseMember._mem_id += 1
        self._mem_id = BaseMember._mem_id
        self.__name = name
        self.__family = family
        self.__address = address
        self.__phone = phone
        self.__age = age
        self.__date = str(datetime.now())

    @property
    def member_id(self):
        return self._mem_id

    @member_id.setter
    def member_id(self, value):
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        self.__family = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value: datetime.date):
        self.__date = value

    def __repr__(self):
        return f"<Member({self.member_id}, {self.name}, {self.family})>"
