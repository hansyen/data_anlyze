"""empty message

Revision ID: c2e1f7e86123
Revises: 
Create Date: 2019-03-08 04:29:29.649147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2e1f7e86123'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bank_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('bank_name', sa.String(length=20), nullable=False),
    sa.Column('bank_account', sa.String(length=20), nullable=False),
    sa.Column('quota', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('qr_code', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bank_account_remain',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bid', sa.Integer(), nullable=True),
    sa.Column('daily_quota', sa.Integer(), nullable=True),
    sa.Column('remain', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cash_client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('brand_name', sa.String(length=30), nullable=False),
    sa.Column('token_seed', sa.String(length=32), nullable=False),
    sa.Column('notify_uri', sa.String(length=90), nullable=True),
    sa.Column('notify_uri_rollin', sa.String(length=90), nullable=True),
    sa.Column('revenue', sa.Numeric(precision=4, scale=3), nullable=True),
    sa.Column('latest_login', sa.DateTime(), nullable=True),
    sa.Column('is_test', sa.Boolean(), nullable=True),
    sa.Column('is_block', sa.Boolean(), nullable=True),
    sa.Column('test_name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('brand_name'),
    sa.UniqueConstraint('token_seed'),
    sa.UniqueConstraint('username')
    )
    op.create_table('channel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('api_uri', sa.String(length=60), nullable=False),
    sa.Column('account', sa.String(length=30), nullable=False),
    sa.Column('token_seed', sa.String(length=60), nullable=True),
    sa.Column('is_avaliable', sa.Boolean(), nullable=True),
    sa.Column('alipay', sa.Boolean(), nullable=True),
    sa.Column('weixin', sa.Boolean(), nullable=True),
    sa.Column('online_pay', sa.Boolean(), nullable=True),
    sa.Column('nocard', sa.Boolean(), nullable=True),
    sa.Column('qq', sa.Boolean(), nullable=True),
    sa.Column('jd_pay', sa.Boolean(), nullable=True),
    sa.Column('union_pay', sa.Boolean(), nullable=True),
    sa.Column('weixin_wap', sa.Boolean(), nullable=True),
    sa.Column('qq_wap', sa.Boolean(), nullable=True),
    sa.Column('wx_cashier', sa.Boolean(), nullable=True),
    sa.Column('alipay_wap', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account')
    )
    op.create_table('fourth_ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('chid', sa.Integer(), nullable=False),
    sa.Column('client_tid', sa.String(length=30), nullable=True),
    sa.Column('fourth_tid', sa.String(length=30), nullable=True),
    sa.Column('third_tid', sa.String(length=30), nullable=True),
    sa.Column('cur', sa.String(length=10), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('product_name', sa.String(length=30), nullable=True),
    sa.Column('product_cate', sa.String(length=30), nullable=True),
    sa.Column('product_desc', sa.String(length=30), nullable=True),
    sa.Column('payment', sa.String(length=30), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['chid'], ['channel.id'], ),
    sa.ForeignKeyConstraint(['cid'], ['cash_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fourth_ticket_test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('chid', sa.Integer(), nullable=False),
    sa.Column('client_tid', sa.String(length=30), nullable=True),
    sa.Column('fourth_tid', sa.String(length=30), nullable=True),
    sa.Column('third_tid', sa.String(length=30), nullable=True),
    sa.Column('cur', sa.String(length=10), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('product_name', sa.String(length=30), nullable=True),
    sa.Column('product_cate', sa.String(length=30), nullable=True),
    sa.Column('product_desc', sa.String(length=30), nullable=True),
    sa.Column('payment', sa.String(length=30), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['chid'], ['channel.id'], ),
    sa.ForeignKeyConstraint(['cid'], ['cash_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('merchant_channel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('alipay', sa.Integer(), nullable=True),
    sa.Column('weixin', sa.Integer(), nullable=True),
    sa.Column('online_pay', sa.Integer(), nullable=True),
    sa.Column('nocard', sa.Integer(), nullable=True),
    sa.Column('qq', sa.Integer(), nullable=True),
    sa.Column('jd_pay', sa.Integer(), nullable=True),
    sa.Column('union_pay', sa.Integer(), nullable=True),
    sa.Column('weixin_wap', sa.Integer(), nullable=True),
    sa.Column('qq_wap', sa.Integer(), nullable=True),
    sa.Column('wx_cashier', sa.Integer(), nullable=True),
    sa.Column('alipay_wap', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['cash_client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rolling_ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tid', sa.String(length=20), nullable=True),
    sa.Column('mh', sa.String(length=10), nullable=False),
    sa.Column('mh_tid', sa.String(length=20), nullable=True),
    sa.Column('currency_from', sa.String(length=10), nullable=True),
    sa.Column('currency_to', sa.String(length=10), nullable=True),
    sa.Column('amount', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('note', sa.String(length=60), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('bank_account', sa.Integer(), nullable=True),
    sa.Column('to_bank', sa.String(length=30), nullable=True),
    sa.Column('to_bank_user', sa.String(length=30), nullable=True),
    sa.Column('to_bank_no', sa.String(length=30), nullable=True),
    sa.Column('chk_value', sa.String(length=40), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['mh'], ['cash_client.brand_name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rolling_ticket_test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tid', sa.String(length=20), nullable=True),
    sa.Column('mh', sa.String(length=10), nullable=False),
    sa.Column('mh_tid', sa.String(length=20), nullable=True),
    sa.Column('currency_from', sa.String(length=10), nullable=True),
    sa.Column('currency_to', sa.String(length=10), nullable=True),
    sa.Column('amount', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('note', sa.String(length=60), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('bank_account', sa.Integer(), nullable=True),
    sa.Column('to_bank', sa.String(length=30), nullable=True),
    sa.Column('to_bank_user', sa.String(length=30), nullable=True),
    sa.Column('to_bank_no', sa.String(length=30), nullable=True),
    sa.Column('chk_value', sa.String(length=40), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['mh'], ['cash_client.brand_name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fourth_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ftid', sa.Integer(), nullable=False),
    sa.Column('change_from', sa.Integer(), nullable=True),
    sa.Column('change_to', sa.Integer(), nullable=True),
    sa.Column('change_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ftid'], ['fourth_ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fourth_log_test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ftid', sa.Integer(), nullable=False),
    sa.Column('change_from', sa.Integer(), nullable=True),
    sa.Column('change_to', sa.Integer(), nullable=True),
    sa.Column('change_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ftid'], ['fourth_ticket_test.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fourth_revenue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fid', sa.Integer(), nullable=False),
    sa.Column('mh', sa.String(length=10), nullable=False),
    sa.Column('revenue', sa.Numeric(precision=20, scale=10), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['fid'], ['fourth_ticket.id'], ),
    sa.ForeignKeyConstraint(['mh'], ['cash_client.brand_name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rolling_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rtid', sa.Integer(), nullable=False),
    sa.Column('change_from', sa.Integer(), nullable=True),
    sa.Column('change_to', sa.Integer(), nullable=True),
    sa.Column('change_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['rtid'], ['rolling_ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rolling_log_test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rtid', sa.Integer(), nullable=False),
    sa.Column('change_from', sa.Integer(), nullable=True),
    sa.Column('change_to', sa.Integer(), nullable=True),
    sa.Column('change_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['rtid'], ['rolling_ticket_test.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rolling_log_test')
    op.drop_table('rolling_log')
    op.drop_table('fourth_revenue')
    op.drop_table('fourth_log_test')
    op.drop_table('fourth_log')
    op.drop_table('rolling_ticket_test')
    op.drop_table('rolling_ticket')
    op.drop_table('merchant_channel')
    op.drop_table('fourth_ticket_test')
    op.drop_table('fourth_ticket')
    op.drop_table('channel')
    op.drop_table('cash_client')
    op.drop_table('bank_account_remain')
    op.drop_table('bank_account')
    # ### end Alembic commands ###
