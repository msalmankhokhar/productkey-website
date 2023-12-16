"""empty message

Revision ID: 8a7fbca2030c
Revises: e19ffb6eb7ed
Create Date: 2023-12-16 22:09:07.163526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a7fbca2030c'
down_revision = 'e19ffb6eb7ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('softwares', schema=None) as batch_op:
        batch_op.add_column(sa.Column('desc', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('softwares', schema=None) as batch_op:
        batch_op.drop_column('desc')

    # ### end Alembic commands ###
