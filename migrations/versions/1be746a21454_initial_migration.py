"""Initial migration

Revision ID: 1be746a21454
Revises: 
Create Date: 2024-11-24 18:54:50.675199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1be746a21454'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('middle_name',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.alter_column('dob',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.drop_index('first_name')
        batch_op.drop_index('last_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('last_name', ['last_name'], unique=True)
        batch_op.create_index('first_name', ['first_name'], unique=True)
        batch_op.alter_column('dob',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.alter_column('middle_name',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###