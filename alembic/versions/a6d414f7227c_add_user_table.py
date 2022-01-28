"""add user table

Revision ID: a6d414f7227c
Revises: db26db5c4c02
Create Date: 2022-01-27 23:34:37.074883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a6d414f7227c"
down_revision = "db26db5c4c02"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
