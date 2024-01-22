"""empty message

Revision ID: 5099b4f700d3
Revises: 8a7fbca2030c
Create Date: 2024-01-11 11:13:41.920749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5099b4f700d3'
down_revision = '8a7fbca2030c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('softwares', schema=None) as batch_op:
        batch_op.add_column(sa.Column('keys', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('platforms', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('cracks', sa.String(length=500), nullable=True))
        batch_op.drop_column('key')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('softwares', schema=None) as batch_op:
        batch_op.add_column(sa.Column('key', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('cracks')
        batch_op.drop_column('platforms')
        batch_op.drop_column('keys')

    # ### end Alembic commands ###