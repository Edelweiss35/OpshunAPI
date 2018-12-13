"""empty message

Revision ID: a83a18808f2
Revises: ae025575696
Create Date: 2015-05-02 23:23:15.402960

"""

# revision identifiers, used by Alembic.
revision = 'a83a18808f2'
down_revision = 'ae025575696'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('preferences', sa.Column('characteristic', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('preferences', 'characteristic')
    ### end Alembic commands ###
