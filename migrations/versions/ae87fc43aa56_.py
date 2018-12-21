"""empty message

Revision ID: ae87fc43aa56
Revises: c2eb1a539782
Create Date: 2018-12-20 16:33:26.487235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae87fc43aa56'
down_revision = 'c2eb1a539782'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('jobposts_contact_email_key', 'jobposts', type_='unique')
    op.drop_constraint('jobposts_contact_number_key', 'jobposts', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('jobposts_contact_number_key', 'jobposts', ['contact_number'])
    op.create_unique_constraint('jobposts_contact_email_key', 'jobposts', ['contact_email'])
    # ### end Alembic commands ###