"""add last few columns to posts table

Revision ID: 038d212aa0cc
Revises: 624e92bfe28c
Create Date: 2022-01-27 23:46:14.373888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "038d212aa0cc"
down_revision = "624e92bfe28c"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
