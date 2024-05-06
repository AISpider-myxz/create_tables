"""create_table_CentralCoast

Revision ID: 74096d56c5b2
Revises: 
Create Date: 2024-05-06 10:57:55.026057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74096d56c5b2'
down_revision: Union[str, None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kalamunda',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_number', sa.String(length=255), nullable=False),
    sa.Column('lodgement_date', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('applicant', sa.Text(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('telephone', sa.String(length=255), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('decision', sa.String(length=255), nullable=True),
    sa.Column('decision_date', sa.String(length=255), nullable=True),
    sa.Column('stage_', sa.String(length=255), nullable=True),
    sa.Column('start_date', sa.String(length=255), nullable=True),
    sa.Column('end_date', sa.String(length=255), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_number')
    )
    # ### end Alembic commands ###