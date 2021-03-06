"""test

Revision ID: 1a592997f580
Revises: d236e9852d61
Create Date: 2021-08-27 01:20:35.702157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a592997f580'
down_revision = 'd236e9852d61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('last_name', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'last_name')
    # ### end Alembic commands ###
