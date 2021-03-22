"""create account table

Revision ID: 2e20811e1113
Revises: 
Create Date: 2021-03-22 21:48:18.263117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e20811e1113'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('full_name', sa.String(50), index=True, nullable=False),
        sa.Column('email', sa.String(50), unique=True, index=True, nullable=False),
        sa.Column('hashed_password', sa.String(150), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('is_superuser', sa.Boolean, default=False),
        sa.Column('created_date', sa.DateTime)
    )


def downgrade():
    pass
