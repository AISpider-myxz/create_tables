"""create_table_CentralCoast

Revision ID: d1bc8e58dd42
Revises: 7c159f0c5fcd
Create Date: 2024-05-07 14:21:36.672261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1bc8e58dd42'
down_revision: Union[str, None] = '7c159f0c5fcd'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('geelongaustralia',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_num', sa.String(length=255), nullable=False),
    sa.Column('vic_smart', sa.String(length=255), nullable=True),
    sa.Column('lodge_date', sa.Integer(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('changes_', sa.String(length=255), nullable=True),
    sa.Column('type_', sa.String(length=255), nullable=True),
    sa.Column('notice_date', sa.Integer(), nullable=True),
    sa.Column('authority', sa.String(length=255), nullable=True),
    sa.Column('decision_date', sa.Integer(), nullable=True),
    sa.Column('decision', sa.Text(), nullable=True),
    sa.Column('vc_refno', sa.Text(), nullable=True),
    sa.Column('vc_decision', sa.Text(), nullable=True),
    sa.Column('vc_date', sa.Integer(), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_num')
    )
    # ### end Alembic commands ###