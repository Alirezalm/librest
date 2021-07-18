from src.models import Member


class MemberInsertController:
    def __init__(self, member_data: dict):
        self.member_data = member_data
        self.member = self._create_member()
        self._send_to_bll()

    def _create_member(self) -> Member:
        member = Member()
        member.name = self.member_data['name']
        member.family = self.member_data['family']
        member.address = self.member_data['address']
        member.phone = self.member_data['phone']
        member.age = self.member_data['age']
        return member

    def _send_to_bll(self):
        pass
