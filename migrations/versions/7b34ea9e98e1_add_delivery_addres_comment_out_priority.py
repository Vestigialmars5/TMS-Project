"""Add delivery_addres, Comment out priority

Revision ID: 7b34ea9e98e1
Revises: 8f14d7110c6d
Create Date: 2024-11-24 18:49:38.662704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b34ea9e98e1'
down_revision = '8f14d7110c6d'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.drop_index('ix_priority')
        batch_op.drop_column('priority')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('delivery_address', sa.String(length=255), nullable=False))
        batch_op.create_index('ix_deliver_address', ['delivery_address'], unique=False)

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_index('ix_deliver_address')
        batch_op.drop_column('delivery_address')

    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.add_column(sa.Column('priority', sa.INTEGER(), nullable=False))
        batch_op.create_index('ix_priority', ['priority'], unique=False)

    # ### end Alembic commands ###


def upgrade_wms():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_wms():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

