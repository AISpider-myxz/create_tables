"""create_table_CentralCoast

Revision ID: c8ac805f867d
Revises: 2640d8b6b91d
Create Date: 2024-05-09 15:21:09.247214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8ac805f867d'
down_revision: Union[str, None] = '2640d8b6b91d'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweed_shire_council',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=False),
    sa.Column('app_num', sa.String(length=500), nullable=False),
    sa.Column('detail_text', sa.Text(), nullable=True),
    sa.Column('detail_Lodged_data', sa.Integer(), nullable=True),
    sa.Column('detail_Determined_data', sa.String(length=255), nullable=True),
    sa.Column('detail_cost', sa.String(length=255), nullable=True),
    sa.Column('detail_officer', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('people_Applicant', sa.String(length=255), nullable=True),
    sa.Column('documents_url', sa.Text(), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_id'),
    sa.UniqueConstraint('app_num')
    )
    # ### end Alembic commands ###
