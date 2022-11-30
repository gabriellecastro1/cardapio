"""empty message

Revision ID: 2a38d557ef1e
Revises: 27a059364c66
Create Date: 2022-11-30 08:47:37.367937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a38d557ef1e'
down_revision = '27a059364c66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno_refeicao',
    sa.Column('matricula', sa.String(length=20), nullable=False),
    sa.Column('refeicao_id', sa.BigInteger(), nullable=False),
    sa.Column('confirmado', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['matricula'], ['aluno.matricula'], ),
    sa.ForeignKeyConstraint(['refeicao_id'], ['refeicao.id'], ),
    sa.PrimaryKeyConstraint('matricula', 'refeicao_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aluno_refeicao')
    # ### end Alembic commands ###
