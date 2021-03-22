"""create item table

Revision ID: f4b7eed59232
Revises: 2e20811e1113
Create Date: 2021-03-22 23:12:44.754557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4b7eed59232'
down_revision = '2e20811e1113'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'item',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String(50), index=True, nullable=False),
        sa.Column('description', sa.Unicode(150), nullable=False),
        sa.Column('owner_id', sa.Integer)
    )


def downgrade():
    pass
