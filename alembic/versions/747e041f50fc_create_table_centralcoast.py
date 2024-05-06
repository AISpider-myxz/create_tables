"""create_table_CentralCoast

Revision ID: 747e041f50fc
Revises: 77dab8a9035a
Create Date: 2024-05-06 15:59:11.836091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '747e041f50fc'
down_revision: Union[str, None] = '77dab8a9035a'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moyne',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_number', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('documents', sa.Text(), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_number')
    )
    # ### end Alembic commands ###
