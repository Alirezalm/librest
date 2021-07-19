from src.DAL.managers import MemberManager
from src.models import Member


class MemberLogic:

    def __init__(self):
        self.manager = MemberManager()

    def add_member(self, member: Member):
        """ Semantics have to get checked here"""
        self.manager.insert(member)

    def list_members(self):
        self.manager.list()
        return 1
