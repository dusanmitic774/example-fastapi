"""add content column to posts table

Revision ID: db26db5c4c02
Revises: 20f7fc00d214
Create Date: 2022-01-27 23:29:06.351223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "db26db5c4c02"
down_revision = "20f7fc00d214"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
