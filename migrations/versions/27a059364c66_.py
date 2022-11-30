"""empty message

Revision ID: 27a059364c66
Revises: 8e6008ae683a
Create Date: 2022-11-30 08:39:59.557802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27a059364c66'
down_revision = '8e6008ae683a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('refeicao', sa.Column('prato_id', sa.BigInteger(), nullable=False))
    op.create_foreign_key(None, 'refeicao', 'prato', ['prato_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'refeicao', type_='foreignkey')
    op.drop_column('refeicao', 'prato_id')
    # ### end Alembic commands ###