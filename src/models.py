from abc import ABC
from dataclasses import dataclass
from datetime import datetime


class BaseModel(ABC):
    pass


class BaseMember(BaseModel):
    _mem_id = 0


@dataclass
class Member(BaseMember):
    def __init__(self):
        BaseMember._mem_id += 1
        self._mem_id = BaseMember._mem_id
        self.__name: str = ''
        self.__family: str = ''
        self.__address: str = ''
        self.__phone: str = ''
        self.__age: int = 0
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
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value: datetime.date):
        self.__date = value

    def __repr__(self):
        return f"<Member({self.member_id}, {self.name}, {self.family})>"
