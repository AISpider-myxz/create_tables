"""create_table_CentralCoast

Revision ID: 74fd8157d7d0
Revises: abc4d47c25dc
Create Date: 2024-05-10 14:46:13.201198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74fd8157d7d0'
down_revision: Union[str, None] = 'abc4d47c25dc'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lockyer_valley', sa.Column('_tid', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###