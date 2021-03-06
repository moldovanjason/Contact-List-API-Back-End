"""empty message

Revision ID: b96f9143d734
Revises: b16090cc121b
Create Date: 2021-01-09 17:29:18.722178

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b96f9143d734'
down_revision = 'b16090cc121b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('address', sa.String(length=60), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=60), nullable=False))
    op.add_column('user', sa.Column('phone', sa.String(length=12), nullable=False))
    op.add_column('user', sa.Column('stage', sa.String(length=20), nullable=False))
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('user', 'stage')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'name')
    op.drop_column('user', 'address')
    # ### end Alembic commands ###
