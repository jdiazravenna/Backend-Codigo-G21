"""agregamos columna fecha vencimiento

Revision ID: 3dc91395db20
Revises: f41d6e9a44f2
Create Date: 2024-11-29 20:28:30.529786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dc91395db20'
down_revision = 'f41d6e9a44f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fecha_vencimiento', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producto_model', schema=None) as batch_op:
        batch_op.drop_column('fecha_vencimiento')

    # ### end Alembic commands ###