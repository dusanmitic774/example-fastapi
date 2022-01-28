"""add phone number

Revision ID: 528a63f5bda1
Revises: f3ead195fa5f
Create Date: 2022-01-27 23:58:09.153590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '528a63f5bda1'
down_revision = 'f3ead195fa5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###