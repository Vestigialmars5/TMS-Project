"""Fix typo and add indexes

Revision ID: ca638b9ae460
Revises: 89ef6b5d5b90
Create Date: 2024-08-21 12:14:04.854585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca638b9ae460'
down_revision = '89ef6b5d5b90'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_driver_details')
    with op.batch_alter_table('driver_details', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=False))
        batch_op.drop_index('ix_user_id')
        batch_op.create_index('ix_driver_details_user_id', ['user_id'], unique=False)
        batch_op.drop_column('driver_status')

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.drop_index('ix_status')
        batch_op.create_index('ix_invoice_status', ['status'], unique=False)

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=False))
        batch_op.drop_index('ix_customer_id')
        batch_op.drop_index('ix_order_status')
        batch_op.create_index('ix_order_status', ['status'], unique=False)
        batch_op.create_index('ix_order_customer_id', ['customer_id'], unique=False)
        batch_op.drop_column('order_status')

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.create_index('ix_payment_status', ['status'], unique=False)

    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.create_index('ix_role_name', ['role_name'], unique=False)

    with op.batch_alter_table('shipments', schema=None) as batch_op:
        batch_op.create_index('ix_driver_id', ['driver_id'], unique=False)
        batch_op.create_index('ix_shipment_customer_id', ['customer_id'], unique=False)
        batch_op.create_index('ix_shipment_order_id', ['order_id'], unique=False)
        batch_op.create_index('ix_shipment_status', ['status'], unique=False)
        batch_op.create_index('ix_shipment_vehicle_id', ['vehicle_id'], unique=False)
        batch_op.create_index('ix_warehouse_id', ['warehouse_id'], unique=False)

    with op.batch_alter_table('user_details', schema=None) as batch_op:
        batch_op.create_index('ix_user_details_user_id', ['user_id'], unique=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_email', ['email'], unique=False)
        batch_op.create_index('ix_role_id', ['role_id'], unique=False)
        batch_op.create_index('ix_username', ['username'], unique=False)

    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('litres_per_100km', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=False))
        batch_op.create_index('ix_vehicle_plate', ['vehicle_plate'], unique=False)
        batch_op.create_index('ix_vehicle_status', ['status'], unique=False)
        batch_op.create_index('ix_vehicle_type', ['vehicle_type'], unique=False)
        batch_op.drop_column('litres_per_100jkm')

    with op.batch_alter_table('warehouses', schema=None) as batch_op:
        batch_op.create_index('ix_warehouse_location', ['location'], unique=False)
        batch_op.create_index('ix_warehouse_name', ['warehouse_name'], unique=False)

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('warehouses', schema=None) as batch_op:
        batch_op.drop_index('ix_warehouse_name')
        batch_op.drop_index('ix_warehouse_location')

    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('litres_per_100jkm', sa.FLOAT(), nullable=False))
        batch_op.drop_index('ix_vehicle_type')
        batch_op.drop_index('ix_vehicle_status')
        batch_op.drop_index('ix_vehicle_plate')
        batch_op.drop_column('status')
        batch_op.drop_column('litres_per_100km')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_username')
        batch_op.drop_index('ix_role_id')
        batch_op.drop_index('ix_email')

    with op.batch_alter_table('user_details', schema=None) as batch_op:
        batch_op.drop_index('ix_user_details_user_id')

    with op.batch_alter_table('shipments', schema=None) as batch_op:
        batch_op.drop_index('ix_warehouse_id')
        batch_op.drop_index('ix_shipment_vehicle_id')
        batch_op.drop_index('ix_shipment_status')
        batch_op.drop_index('ix_shipment_order_id')
        batch_op.drop_index('ix_shipment_customer_id')
        batch_op.drop_index('ix_driver_id')

    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index('ix_role_name')

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.drop_index('ix_payment_status')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_status', sa.VARCHAR(length=50), nullable=False))
        batch_op.drop_index('ix_order_customer_id')
        batch_op.drop_index('ix_order_status')
        batch_op.create_index('ix_order_status', ['order_status'], unique=False)
        batch_op.create_index('ix_customer_id', ['customer_id'], unique=False)
        batch_op.drop_column('status')

    with op.batch_alter_table('invoices', schema=None) as batch_op:
        batch_op.drop_index('ix_invoice_status')
        batch_op.create_index('ix_status', ['status'], unique=False)

    with op.batch_alter_table('driver_details', schema=None) as batch_op:
        batch_op.add_column(sa.Column('driver_status', sa.VARCHAR(length=50), nullable=False))
        batch_op.drop_index('ix_driver_details_user_id')
        batch_op.create_index('ix_user_id', ['user_id'], unique=False)
        batch_op.drop_column('status')

    op.create_table('_alembic_tmp_driver_details',
    sa.Column('driver_detail_id', sa.INTEGER(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=50), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('license_number', sa.VARCHAR(length=50), nullable=False),
    sa.Column('license_expiry', sa.DATETIME(), nullable=False),
    sa.Column('vehicle_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.vehicle_id'], ),
    sa.PrimaryKeyConstraint('driver_detail_id'),
    sa.UniqueConstraint('license_number')
    )
    # ### end Alembic commands ###


def upgrade_wms():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_wms():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

