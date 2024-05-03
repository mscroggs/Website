"""Venue: add server-side default for venuetype-related array columns.

Revision ID: 521f0a142614
Revises: 4166f94375f5
Create Date: 2024-05-03 01:17:40.459411

"""

# revision identifiers, used by Alembic.
revision = '521f0a142614'
down_revision = '4166f94375f5'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'allowed_types',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    op.alter_column('venue', 'default_for_types',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'default_for_types',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    op.alter_column('venue', 'allowed_types',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    # ### end Alembic commands ###
