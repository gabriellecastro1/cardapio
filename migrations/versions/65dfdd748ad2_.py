"""empty message

Revision ID: 65dfdd748ad2
Revises: 0c4bc6a01253
Create Date: 2022-11-30 08:25:40.470599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65dfdd748ad2'
down_revision = '0c4bc6a01253'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cardapio',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cardapio')
    # ### end Alembic commands ###
