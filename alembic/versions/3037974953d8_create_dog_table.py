"""create dog table

Revision ID: 3037974953d8
Revises: 8183e08d5da5
Create Date: 2021-05-25 23:45:55.800988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3037974953d8'
down_revision = '8183e08d5da5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dogs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('picture', sa.String(250), nullable=False),
        sa.Column('is_adopted', sa.Boolean, default=True),
        sa.Column('create_date', sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column('id_user', sa.Integer, sa.ForeignKey('users.id') )
    )


def downgrade():
    pass
