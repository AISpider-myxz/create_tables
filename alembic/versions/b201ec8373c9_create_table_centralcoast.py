"""create_table_CentralCoast

Revision ID: b201ec8373c9
Revises: 208cada9920d
Create Date: 2024-05-06 17:07:02.761033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b201ec8373c9'
down_revision: Union[str, None] = '208cada9920d'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('whitehorse',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_number', sa.String(length=64), nullable=False),
    sa.Column('name_details', sa.Text(), nullable=True),
    sa.Column('decision_type', sa.String(length=256), nullable=True),
    sa.Column('decision_date', sa.Integer(), nullable=True),
    sa.Column('app_class', sa.String(length=256), nullable=True),
    sa.Column('app_type', sa.String(length=64), nullable=True),
    sa.Column('app_description', sa.String(length=256), nullable=True),
    sa.Column('location', sa.String(length=256), nullable=True),
    sa.Column('status', sa.String(length=256), nullable=True),
    sa.Column('current_decision', sa.Text(), nullable=True),
    sa.Column('application_date', sa.Integer(), nullable=True),
    sa.Column('lodgement_date', sa.Integer(), nullable=True),
    sa.Column('to_be_commenced_by_date', sa.Integer(), nullable=True),
    sa.Column('expiry_date', sa.Integer(), nullable=True),
    sa.Column('office', sa.String(length=256), nullable=True),
    sa.Column('start_date', sa.Integer(), nullable=True),
    sa.Column('document', sa.Text(), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_number')
    )
    # ### end Alembic commands ###
