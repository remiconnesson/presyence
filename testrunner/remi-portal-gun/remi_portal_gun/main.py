import typer
from .discovery import discovery
from .server import run_server

app = typer.Typer()

@app.command()
def run():
    """
    Shoot the portal gun
    """
    typer.echo("running tests...")
    discovery()
    run_server()
