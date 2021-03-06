"""queue table for pq

Revision ID: 8acbad111ef6
Revises: f31ad1385ed5
Create Date: 2017-03-03 11:07:25.491350

"""

# revision identifiers, used by Alembic.
revision = '8acbad111ef6'
down_revision = 'f31ad1385ed5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('queue',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('enqueued_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('dequeued_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('expected_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('schedule_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('q_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('priority_idx', 'queue', ['schedule_at', 'expected_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('priority_idx', table_name='queue')
    op.drop_table('queue')
    # ### end Alembic commands ###
