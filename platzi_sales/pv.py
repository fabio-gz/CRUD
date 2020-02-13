import click

from clients import commands as clients_commands

@click.group() # to make function cli the entry point
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_command(clients_commands.all)
