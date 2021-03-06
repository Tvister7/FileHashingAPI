"""New Migration

Revision ID: f3716a913050
Revises: 
Create Date: 2021-09-29 22:20:03.046591

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f3716a913050'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('md5files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', postgresql.UUID(), nullable=True),
    sa.Column('hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_md5files_id'), 'md5files', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_md5files_id'), table_name='md5files')
    op.drop_table('md5files')
    # ### end Alembic commands ###
