"""empty message

Revision ID: 208b18cc3f9
Revises: None
Create Date: 2015-11-21 12:18:14.071000

"""

# revision identifiers, used by Alembic.
revision = '208b18cc3f9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('game', sa.String(length=64), autoincrement=False, nullable=False),
    sa.Column('character_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('join_date', sa.DateTime(), nullable=True),
    sa.Column('login_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('game', 'character_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###
