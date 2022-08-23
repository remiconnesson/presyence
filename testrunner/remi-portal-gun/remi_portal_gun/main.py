import typer
from .discovery import discovery
from .server import run_server
from .access_static import get_website_files

app = typer.Typer()

@app.command()
def run():
    """
    Shoot the portal gun
    """
    typer.echo("running tests...")
    # discovery()
    # run_server()
    get_website_files()
