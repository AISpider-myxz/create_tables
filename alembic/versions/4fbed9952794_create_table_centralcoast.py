"""create_table_CentralCoast

Revision ID: 4fbed9952794
Revises: 11cbdab75532
Create Date: 2024-05-10 15:32:34.106629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fbed9952794'
down_revision: Union[str, None] = '11cbdab75532'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moretonbay_da_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('da_number', sa.String(length=255), nullable=False),
    sa.Column('lodged', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('update_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('da_number')
    )
    # ### end Alembic commands ###
