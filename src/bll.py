from src.DAL.managers import MemberManager
from src.models import Member


class MemberLogic:

    @staticmethod
    def add_member(member: Member):
        """ Semantics have to get checked here"""

        manager = MemberManager()
        manager.insert(member)
