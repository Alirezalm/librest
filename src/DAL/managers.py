from abc import ABC, abstractmethod

import click
import psycopg2

from src.DAL.connector import DBConnector
from src.models import BaseModel, Member


class IManager(ABC):

    @abstractmethod
    def insert(self, obj: BaseModel):
        pass

    @abstractmethod
    def list(self):
        pass


class MemberManager(IManager):

    def insert(self, member: Member):
        connection = DBConnector().get_connection()
        try:
            cursor = connection.cursor()

            sql = """INSERT INTO public."Members" (mem_id, mem_name, mem_family, address, phone, age, mem_date)""" + \
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
            click.echo("new Member inserted")
            return 1
        except (Exception, psycopg2.Error) as error:
            print(error)
        finally:
            connection.close()

    def list(self):
        connection = DBConnector().get_connection()
        try:
            cursor = connection.cursor()
            sql = """SELECT * FROM public."Members" """

            cursor.execute(sql)
            click.echo(f"number of items: {cursor.rowcount}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            cursor.close()

        except (Exception, psycopg2.Error) as error:
            click.echo(error)
        finally:
            connection.close()
