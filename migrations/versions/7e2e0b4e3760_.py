"""empty message

Revision ID: 7e2e0b4e3760
Revises: de0010f6f996
Create Date: 2019-03-05 19:36:36.240000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e2e0b4e3760'
down_revision = 'de0010f6f996'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('isactive', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('front_user', 'isactive')
    # ### end Alembic commands ###
