"""empty message

Revision ID: e19ffb6eb7ed
Revises: 
Create Date: 2023-12-14 19:36:01.844720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e19ffb6eb7ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('softwares', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tags', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('softwares', schema=None) as batch_op:
        batch_op.drop_column('tags')

    # ### end Alembic commands ###
