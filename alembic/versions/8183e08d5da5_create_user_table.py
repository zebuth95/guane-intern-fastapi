"""create user table

Revision ID: 8183e08d5da5
Revises: 
Create Date: 2021-05-25 22:40:41.917274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8183e08d5da5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(100), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade():
    op.drop_table('users')
    
