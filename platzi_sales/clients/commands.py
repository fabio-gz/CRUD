import click

@click.group() #turns client function into a decorator
def clients():
    """Manages de clients lifecycle"""
    pass

@clients.command()
@click.pass_context # pass the context
def create(ctx, name, company, email, position):
    """Creeates a new client"""
    pass

@clients.command()
@click.pass_context
def list(ctx):
    """list all clients"""
    pass

@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    pass

@clients.command()
@click.pass_context
def delete(ctc, client_uid):
    """Deletes a client"""
    pass

all = clients #alias all variable points to clients
