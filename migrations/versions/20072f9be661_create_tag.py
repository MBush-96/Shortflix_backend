"""create-tag

Revision ID: 20072f9be661
Revises: c640cacb53d7
Create Date: 2021-05-21 16:15:25.160437

"""
from sqlalchemy.sql.expression import null
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20072f9be661'
down_revision = 'c640cacb53d7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('movie_id', sa.Integer, nullable=False),
        sa.Column('genre', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('tags')
