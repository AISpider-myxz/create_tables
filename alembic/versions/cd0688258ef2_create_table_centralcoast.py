"""create_table_CentralCoast

Revision ID: cd0688258ef2
Revises: d1bc8e58dd42
Create Date: 2024-05-07 14:27:31.382845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd0688258ef2'
down_revision: Union[str, None] = 'd1bc8e58dd42'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('monash',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_number', sa.String(length=512), nullable=False),
    sa.Column('loged', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=512), nullable=True),
    sa.Column('current_decision', sa.String(length=512), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('decision_date', sa.Integer(), nullable=True),
    sa.Column('decision_type', sa.String(length=512), nullable=True),
    sa.Column('decision_lssuedby', sa.String(length=512), nullable=True),
    sa.Column('location', sa.String(length=512), nullable=True),
    sa.Column('application_date', sa.Integer(), nullable=True),
    sa.Column('application_type', sa.String(length=512), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('application_number')
    )
    # ### end Alembic commands ###
