from flask.cli import AppGroup
from .users import seed_users, undo_users
from .movies import seed_movies, undo_movies
from .genres import seed_genres, undo_genres
from .profiles import seed_profiles, undo_profiles
from .reviews import seed_reviews, undo_reviews
from .movie_genres import seed_movie_genres, undo_movie_genres
from .my_list import seed_my_list, undo_my_list
from .tv_shows import seed_tv, undo_tv
from .tv_show_genres import seed_tv_show_genres, undo_tv_show_genres
from .tv_show_episodes import seed_tv_episodes, undo_tv_episodes
from .tv_show_reviews import seed_tv_reviews, undo_tv_reviews

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_profiles()
        undo_genres()
        undo_movies()
        undo_tv()
        undo_movie_genres()
        undo_tv_show_genres()
        undo_tv_episodes()
        undo_reviews()
        undo_tv_reviews()
        undo_my_list()
    seed_users()
    seed_profiles()
    seed_genres()
    seed_movies()
    seed_tv()
    seed_movie_genres()
    seed_tv_show_genres()
    seed_tv_episodes()
    seed_reviews()
    seed_tv_reviews()
    seed_my_list()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_my_list()
    undo_tv_reviews()
    undo_reviews()
    undo_tv_episodes()
    undo_tv_show_genres()
    undo_movie_genres()
    undo_tv()
    undo_movies()
    undo_genres()
    undo_profiles()
    undo_users()
    # Add other undo functions here
