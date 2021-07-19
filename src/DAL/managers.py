from abc import ABC, abstractmethod

import click
import psycopg2

from src.DAL.connector import DBConnector
from src.models import BaseModel, Member


class IManager(ABC):

    @abstractmethod
    def insert(self, obj: BaseModel):
        pass


class MemberManager(IManager):

    def insert(self, member: Member):
        connection = DBConnector().get_connection()
        try:
            cursor = connection.cursor()

            sql = """INSERT INTO public."Members" (mem_id, mem_name, mem_family, address, phone, age, mem_date)""" +\
                  """VALUES (%s, %s, %s, %s, %s, %s, %s);"""

            cursor.execute(
                sql,
                (
                    member.member_id,
                    member.name,
                    member.family,
                    member.address,
                    member.phone,
                    member.age,
                    member.date
                )
            )
            connection.commit()
            cursor.close()
            connection.close()
            click.echo("new Member inserted")
            return 1
        except (Exception, psycopg2.Error) as error:
            print(error)
        # finally:
        #     connection.close()