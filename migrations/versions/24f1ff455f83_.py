"""empty message

Revision ID: 24f1ff455f83
Revises: a5769cee314c
Create Date: 2022-12-07 09:52:56.176852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24f1ff455f83'
down_revision = 'a5769cee314c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('avaliacao', 'comentario',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('avaliacao', 'comentario',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
