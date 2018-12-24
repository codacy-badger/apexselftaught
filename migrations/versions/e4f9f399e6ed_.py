"""empty message

Revision ID: e4f9f399e6ed
Revises: ae87fc43aa56
Create Date: 2018-12-23 20:58:25.852403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4f9f399e6ed'
down_revision = 'ae87fc43aa56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('url_link', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'url_link')
    # ### end Alembic commands ###