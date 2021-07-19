from src.bll import MemberLogic
from src.models import Member


class MemberInsertController:
    def __init__(self, member_data: dict):
        self.member_data = member_data
        self.member = self._create_member()
        self._send_to_bll()

    def _create_member(self) -> Member:
        """ Syntax validation here """
        member = Member()
        member.name = self.member_data['name']
        member.family = self.member_data['family']
        member.address = self.member_data['address']
        member.phone = self.member_data['phone']
        member.age = self.member_data['age']
        return member

    def _send_to_bll(self):
        member_logic = MemberLogic()
        member_logic.add_member(self.member)


class MemberListController:
    def __init__(self):
        self.member_logic = MemberLogic()
        self.member_list = self._fetch_all()

    def _fetch_all(self):
        return self.member_logic.list_members()

    def make_dict(self):
        initial_dict = self.member_list[0].__dict__
        final_dict = {}
        for key, value in initial_dict.items():
            final_dict[key.split("__")[-1]] = value
        return final_dict
