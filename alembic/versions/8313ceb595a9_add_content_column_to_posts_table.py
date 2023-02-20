"""add content column to posts table

Revision ID: 8313ceb595a9
Revises: 1514bc436cff
Create Date: 2023-02-20 20:05:58.977500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8313ceb595a9'
down_revision = '1514bc436cff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
