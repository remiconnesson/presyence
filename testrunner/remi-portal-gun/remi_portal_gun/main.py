import typer

app = typer.Typer()

@app.command()
def run():
    """
    Shoot the portal gun
    """
    typer.echo("running tests...")
