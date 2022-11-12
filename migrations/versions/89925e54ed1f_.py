"""empty message

Revision ID: 89925e54ed1f
Revises: 
Create Date: 2022-11-12 09:44:48.615682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89925e54ed1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cargo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('controller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('pais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('iso', sa.String(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('iso')
    )
    op.create_table('estado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('sigla', sa.String(length=2), nullable=False),
    sa.Column('pais_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pais_id'], ['pais.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sigla')
    )
    op.create_table('regra',
    sa.Column('acao', sa.String(length=20), nullable=False),
    sa.Column('cargo_id', sa.Integer(), nullable=False),
    sa.Column('controller_id', sa.Integer(), nullable=False),
    sa.Column('permitir', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['cargo_id'], ['cargo.id'], ),
    sa.ForeignKeyConstraint(['controller_id'], ['controller.id'], ),
    sa.PrimaryKeyConstraint('acao', 'cargo_id', 'controller_id')
    )
    op.create_table('cidade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('ibge', sa.String(length=255), nullable=False),
    sa.Column('estado_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['estado_id'], ['estado.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ibge')
    )
    op.create_table('perfil',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('pis', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=50), nullable=False),
    sa.Column('cep', sa.String(length=20), nullable=False),
    sa.Column('rua', sa.String(length=255), nullable=False),
    sa.Column('numero', sa.String(length=20), nullable=False),
    sa.Column('complemento', sa.String(length=50), nullable=True),
    sa.Column('cidade_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['cidade_id'], ['cidade.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('pis')
    )
    op.create_table('usuario',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.Column('perfil_id', sa.BigInteger(), nullable=True),
    sa.Column('cargo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cargo_id'], ['cargo.id'], ),
    sa.ForeignKeyConstraint(['perfil_id'], ['perfil.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('perfil_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('perfil')
    op.drop_table('cidade')
    op.drop_table('regra')
    op.drop_table('estado')
    op.drop_table('pais')
    op.drop_table('controller')
    op.drop_table('cargo')
    # ### end Alembic commands ###
