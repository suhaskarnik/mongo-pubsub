from app import publish, subscribe, configure_logging

from db import DB
import click
import logging
    
logger = logging.getLogger(__name__)

@click.group()
def cli():
    """Main command group."""
    pass

@cli.command()
@click.option('-s', '--size', default=1000, help='Size of cappable collection', show_default=True)
def init(size):
    """(Re)inits the database"""
    configure_logging(logger, "initdb")
    db = DB()
    db.init_coll(size)    
    logger.info("Initialised the DB")
    
@cli.command()
@click.option('-f', '--freq', default=1, help="secs to wait after each message", show_default=True)
@click.argument("nouns", nargs=-1)
def pub(nouns=[], freq=1):
    """Publishes messages to the queue"""
    configure_logging(logger, "pub")
    db = DB()
    publish(db, nouns, freq)


@cli.command()
@click.option('-f', '--freq', default=2, help="secs to wait while polling", show_default=True)
def sub(freq=1):
    """Subscribes to messages from the queue"""
    configure_logging(logger, "sub")
    db = DB()
    subscribe(db, freq)


if __name__ == "__main__":    
    cli()

