"""create_table_CentralCoast

Revision ID: 0f0f2b34df9e
Revises: 33813c3f1677
Create Date: 2024-05-09 10:53:00.250915

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f0f2b34df9e'
down_revision: Union[str, None] = '33813c3f1677'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('northern_beaches_council',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=False),
    sa.Column('app_num', sa.String(length=500), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('applicationType', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('submitted', sa.Integer(), nullable=True),
    sa.Column('exhibitionPeriod', sa.String(length=255), nullable=True),
    sa.Column('determined', sa.Integer(), nullable=True),
    sa.Column('determination_level', sa.String(length=255), nullable=True),
    sa.Column('appeal_status', sa.String(length=255), nullable=True),
    sa.Column('cost', sa.String(length=255), nullable=True),
    sa.Column('officer', sa.String(length=255), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('people', sa.Text(), nullable=True),
    sa.Column('docs', sa.Text(), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_id'),
    sa.UniqueConstraint('app_num')
    )
    # ### end Alembic commands ###