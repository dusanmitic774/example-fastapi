"""add foreign-key to posts table

Revision ID: 624e92bfe28c
Revises: a6d414f7227c
Create Date: 2022-01-27 23:41:11.859054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "624e92bfe28c"
down_revision = "a6d414f7227c"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
