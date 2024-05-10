"""create_table_CentralCoast

Revision ID: e435e55d48ce
Revises: 0b35fb90d958
Create Date: 2024-05-08 17:06:34.501438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e435e55d48ce'
down_revision: Union[str, None] = '0b35fb90d958'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city_of_stirling',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_num', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('primary_group', sa.String(length=255), nullable=True),
    sa.Column('group_', sa.String(length=255), nullable=True),
    sa.Column('primary_category', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('sub_category', sa.String(length=255), nullable=True),
    sa.Column('stage_decision', sa.String(length=255), nullable=True),
    sa.Column('estimated_cost', sa.String(length=255), nullable=True),
    sa.Column('formatted_address', sa.String(length=255), nullable=True),
    sa.Column('suburb', sa.String(length=255), nullable=True),
    sa.Column('street', sa.String(length=255), nullable=True),
    sa.Column('initial_target', sa.Integer(), nullable=True),
    sa.Column('current_target', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('year', sa.String(length=255), nullable=True),
    sa.Column('charge_balance', sa.String(length=255), nullable=True),
    sa.Column('house_No', sa.String(length=255), nullable=True),
    sa.Column('property_name', sa.String(length=255), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_num')
    )
    op.create_table('yass',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.String(length=128), nullable=False),
    sa.Column('close_date', sa.String(length=512), nullable=True),
    sa.Column('applicant_name', sa.String(length=512), nullable=True),
    sa.Column('address', sa.String(length=512), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('documents', sa.Text(), nullable=True),
    sa.Column('payable', sa.String(length=512), nullable=True),
    sa.Column('folio_identifier', sa.String(length=512), nullable=True),
    sa.Column('street_number', sa.String(length=512), nullable=True),
    sa.Column('locality', sa.String(length=512), nullable=True),
    sa.Column('status', sa.String(length=512), nullable=True),
    sa.Column('determination_date', sa.String(length=128), nullable=True),
    sa.Column('time_days', sa.String(length=512), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('application_id')
    )
    # ### end Alembic commands ###