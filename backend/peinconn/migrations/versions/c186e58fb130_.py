"""empty message

Revision ID: c186e58fb130
Revises: 
Create Date: 2023-04-24 12:19:42.917605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c186e58fb130'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('country_abbrev', sa.String(length=3), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('country'),
    sa.UniqueConstraint('country_abbrev')
    )
    op.create_table('interest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('hobby', sa.String(length=80), nullable=False),
    sa.Column('hobby_image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hobby')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('introduction', sa.Text(), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('userImage', sa.String(), nullable=True),
    sa.Column('coverImage', sa.String(), nullable=True),
    sa.Column('is_admin', sa.SmallInteger(), nullable=True),
    sa.Column('is_active', sa.SmallInteger(), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('activity', sa.Text(), nullable=True),
    sa.Column('picture', sa.String(), nullable=True),
    sa.Column('interest_id', sa.Integer(), nullable=False),
    sa.Column('like_no', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interest_id'], ['interest.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interests',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('interest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['interest_id'], ['interest.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'interest_id')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('room', sa.String(length=225), nullable=False),
    sa.Column('user1_id', sa.Integer(), nullable=False),
    sa.Column('user2_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user1_id'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user2_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connected',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('connected_user_id', sa.Integer(), nullable=False),
    sa.Column('connection_room_id', sa.Integer(), nullable=False),
    sa.Column('channel_name', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['connected_user_id'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['connection_room_id'], ['room.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('liked',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('is_liked', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('sender', sa.Integer(), nullable=False),
    sa.Column('receiver', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['receiver'], ['user.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.ForeignKeyConstraint(['sender'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_At', sa.DateTime(), nullable=False),
    sa.Column('updated_At', sa.DateTime(), nullable=True),
    sa.Column('notification_user_id', sa.Integer(), nullable=False),
    sa.Column('notification_message_id', sa.Integer(), nullable=False),
    sa.Column('notification_read', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['notification_message_id'], ['message.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['notification_user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notifications')
    op.drop_table('message')
    op.drop_table('liked')
    op.drop_table('connected')
    op.drop_table('room')
    op.drop_table('interests')
    op.drop_table('activity')
    op.drop_table('user')
    op.drop_table('interest')
    op.drop_table('country')
    # ### end Alembic commands ###
