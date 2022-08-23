import typer
from .discovery import discovery

app = typer.Typer()

@app.command()
def run():
    """
    Shoot the portal gun
    """
    typer.echo("running tests...")
    discovery()
