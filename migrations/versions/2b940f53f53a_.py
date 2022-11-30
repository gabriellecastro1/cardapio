"""empty message

Revision ID: 2b940f53f53a
Revises: 2a38d557ef1e
Create Date: 2022-11-30 08:56:58.440819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b940f53f53a'
down_revision = '2a38d557ef1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('avaliacao',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('refeicao_id', sa.BigInteger(), nullable=False),
    sa.Column('nota', sa.Integer(), nullable=False),
    sa.Column('comentario', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['refeicao_id'], ['refeicao.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('avaliacao')
    # ### end Alembic commands ###
