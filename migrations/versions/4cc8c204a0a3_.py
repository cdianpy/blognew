"""empty message

Revision ID: 4cc8c204a0a3
Revises: 085f8f55bf73
Create Date: 2017-10-25 10:17:51.267186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cc8c204a0a3'
down_revision = '085f8f55bf73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('icon', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'icon')
    # ### end Alembic commands ###
