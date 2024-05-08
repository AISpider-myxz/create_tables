"""create_table_CentralCoast

Revision ID: da5f31d8b452
Revises: 80cfeed2db55
Create Date: 2024-05-08 13:59:39.824862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da5f31d8b452'
down_revision: Union[str, None] = '80cfeed2db55'


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('launceston',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('app_group', sa.String(length=512), nullable=True),
    sa.Column('category', sa.String(length=512), nullable=True),
    sa.Column('app_names', sa.String(length=512), nullable=True),
    sa.Column('app_status', sa.String(length=512), nullable=True),
    sa.Column('closing_date', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=512), nullable=True),
    sa.Column('legal_description', sa.String(length=512), nullable=True),
    sa.Column('officer', sa.String(length=512), nullable=True),
    sa.Column('council_minute', sa.String(length=512), nullable=True),
    sa.Column('use_class', sa.String(length=512), nullable=True),
    sa.Column('develop_description', sa.String(length=512), nullable=True),
    sa.Column('received', sa.Integer(), nullable=True),
    sa.Column('decision', sa.Integer(), nullable=True),
    sa.Column('valid', sa.Integer(), nullable=True),
    sa.Column('stopped', sa.Integer(), nullable=True),
    sa.Column('restarted', sa.Integer(), nullable=True),
    sa.Column('advertised', sa.Integer(), nullable=True),
    sa.Column('meeting', sa.Integer(), nullable=True),
    sa.Column('documents', sa.String(length=1024), nullable=True),
    sa.Column('_tid', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('application_id')
    )
    # ### end Alembic commands ###