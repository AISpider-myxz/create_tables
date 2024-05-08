"""create_table_CentralCoast

Revision ID: e15b04d726e9
Revises: c5d4d0717bef
Create Date: 2024-05-08 10:33:11.275043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e15b04d726e9'
down_revision: Union[str, None] = 'c5d4d0717bef'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bendigo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=False),
    sa.Column('app_num', sa.String(length=255), nullable=False),
    sa.Column('app_type', sa.String(length=255), nullable=True),
    sa.Column('date_received', sa.Integer(), nullable=True),
    sa.Column('proposal', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('location_ward', sa.Text(), nullable=True),
    sa.Column('people', sa.String(length=255), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_id'),
    sa.UniqueConstraint('app_num')
    )
    # ### end Alembic commands ###
