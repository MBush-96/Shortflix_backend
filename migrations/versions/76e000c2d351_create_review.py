"""create-review

Revision ID: 76e000c2d351
Revises: d4544b297c24
Create Date: 2021-05-24 17:01:16.165070

"""
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76e000c2d351'
down_revision = 'd4544b297c24'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('review_body', sa.String, nullable=False),
        sa.Column('movie_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('reviews')
