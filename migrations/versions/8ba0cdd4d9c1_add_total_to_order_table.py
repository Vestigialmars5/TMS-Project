"""Add total to order table

Revision ID: 8ba0cdd4d9c1
Revises: 933078c513e2
Create Date: 2025-04-20 23:37:17.126201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ba0cdd4d9c1'
down_revision = '933078c513e2'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total', sa.Float(), server_default=sa.text("0.0"), nullable=False))
        batch_op.create_index('ix_total', ['total'], unique=False)

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_index('ix_total')
        batch_op.drop_column('total')

    # ### end Alembic commands ###


def upgrade_wms():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_wms():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

