"""create_table_CentralCoast

Revision ID: 5a921ad77ca1
Revises: c8ac805f867d
Create Date: 2024-05-09 15:46:18.905517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '5a921ad77ca1'
down_revision: Union[str, None] = 'c8ac805f867d'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stonnington', 'lodged',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('stonnington', 'site_address',
               existing_type=mysql.INTEGER(),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###