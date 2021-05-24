"""create-movie

Revision ID: c640cacb53d7
Revises: ea164a0c2a52
Create Date: 2021-05-21 15:39:04.092715

"""
from sqlalchemy.sql.expression import null
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c640cacb53d7'
down_revision = 'ea164a0c2a52'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False, unique=True),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('movie_src', sa.String, nullable=False),
        sa.Column('rating', sa.Float, nullable=False),
        sa.Column('movie_cover', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('movies')
