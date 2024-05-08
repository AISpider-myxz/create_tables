"""create_table_CentralCoast

Revision ID: 5d0a51e72155
Revises: e15b04d726e9
Create Date: 2024-05-08 11:22:17.330272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d0a51e72155'
down_revision: Union[str, None] = 'e15b04d726e9'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ndis',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_id', sa.String(length=255), nullable=True),
    sa.Column('app_title', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('building_type', sa.String(length=255), nullable=True),
    sa.Column('design_cat', sa.String(length=255), nullable=True),
    sa.Column('app_vacancy', sa.String(length=255), nullable=True),
    sa.Column('app_status', sa.String(length=255), nullable=True),
    sa.Column('room_num', sa.String(length=255), nullable=True),
    sa.Column('max_price_per_room', sa.String(length=255), nullable=True),
    sa.Column('firesprinklers', sa.String(length=255), nullable=True),
    sa.Column('app_ooa', sa.String(length=255), nullable=True),
    sa.Column('agent_email', sa.String(length=255), nullable=True),
    sa.Column('agent_phone', sa.String(length=255), nullable=True),
    sa.Column('internet_addr', sa.String(length=255), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vincent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_number', sa.String(length=128), nullable=False),
    sa.Column('address', sa.String(length=512), nullable=True),
    sa.Column('data_received', sa.Integer(), nullable=True),
    sa.Column('date_advertised', sa.Integer(), nullable=True),
    sa.Column('agenda', sa.String(length=512), nullable=True),
    sa.Column('minute', sa.String(length=512), nullable=True),
    sa.Column('determination', sa.String(length=512), nullable=True),
    sa.Column('type_work', sa.String(length=512), nullable=True),
    sa.Column('date_lodged', sa.Integer(), nullable=True),
    sa.Column('cost_work', sa.String(length=512), nullable=True),
    sa.Column('planning_officer', sa.String(length=512), nullable=True),
    sa.Column('determination_details', sa.String(length=512), nullable=True),
    sa.Column('determination_date', sa.Integer(), nullable=True),
    sa.Column('fee_type', sa.String(length=512), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_number')
    )
    # ### end Alembic commands ###
