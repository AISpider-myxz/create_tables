"""create_table_CentralCoast

Revision ID: 6d8f978b5381
Revises: 8e31300ddd0d
Create Date: 2024-05-10 15:10:51.683512

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6d8f978b5381'
down_revision: Union[str, None] = '8e31300ddd0d'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('busselton', 'cost')
    # ### end Alembic commands ###
