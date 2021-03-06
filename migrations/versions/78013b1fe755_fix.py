"""fix

Revision ID: 78013b1fe755
Revises: 39a6e5a91fa6
Create Date: 2021-08-29 15:57:24.804432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78013b1fe755'
down_revision = '39a6e5a91fa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('school_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('school_subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('school_class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['school_class_id'], ['school_classes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assessment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assessment', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('school_subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['school_subject_id'], ['school_subject.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assessment')
    op.drop_table('student')
    op.drop_table('school_subject')
    op.drop_table('school_classes')
    # ### end Alembic commands ###
