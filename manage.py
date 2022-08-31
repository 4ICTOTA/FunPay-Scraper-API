import os, uvicorn, typer
from typing import Optional
from core.config import PROJECT_HOST, PROJECT_PORT


app = typer.Typer()


@app.command()
def version():
    """ Command to get python version
    """

    os.system("python --version")


@app.command()
def runserver(
    host: Optional[str] = PROJECT_HOST,
    port: Optional[int] = PROJECT_PORT,
    reload: Optional[bool] = True
):
    """ Command to run server
        >>> python manage.py runserver --host [HOST: default 127.0.0.1] --port [PORT: default 8000] --reload [RELOAD: default True]
    """

    typer.secho(
        message = f"\nStartup server on {host}:{port}...\n",
        fg = typer.colors.BRIGHT_GREEN)

    uvicorn.run(
        app = "main:app",
        host = host,
        port = port,
        reload = reload)


if __name__ == "__main__":
    app()
