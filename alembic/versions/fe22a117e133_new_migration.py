"""New Migration

Revision ID: fe22a117e133
Revises: f3716a913050
Create Date: 2021-09-30 12:56:51.633520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fe22a117e133'
down_revision = 'f3716a913050'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('md5files', sa.Column('file_id', postgresql.UUID(), nullable=True))
    op.drop_column('md5files', 'task_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('md5files', sa.Column('task_id', postgresql.UUID(), autoincrement=False, nullable=True))
    op.drop_column('md5files', 'file_id')
    # ### end Alembic commands ###