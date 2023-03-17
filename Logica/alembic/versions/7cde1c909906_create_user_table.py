"""create user table

Revision ID: 7cde1c909906
Revises: 
Create Date: 2023-02-28 18:32:54.314654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cde1c909906'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nick_name', sa.String(50), nullable=False),
        sa.Column('fullname', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
