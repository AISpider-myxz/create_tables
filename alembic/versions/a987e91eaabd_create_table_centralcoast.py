"""create_table_CentralCoast

Revision ID: a987e91eaabd
Revises: 745c39b8639a
Create Date: 2024-05-23 10:50:57.627559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a987e91eaabd'
down_revision: Union[str, None] = '745c39b8639a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('your_table')
    # ### end Alembic commands ###