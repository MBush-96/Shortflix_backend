"""create-rating

Revision ID: d4544b297c24
Revises: 20072f9be661
Create Date: 2021-05-21 16:44:59.891863

"""
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4544b297c24'
down_revision = '20072f9be661'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ratings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('movie_id', sa.Integer, nullable=False),
        sa.Column('rating', sa.Float, nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('ratings')
