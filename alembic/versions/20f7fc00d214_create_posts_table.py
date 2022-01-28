"""create posts table

Revision ID: 20f7fc00d214
Revises: 
Create Date: 2022-01-27 23:18:09.381162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20f7fc00d214"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
