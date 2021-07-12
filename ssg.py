import typer
from ssg.site import Site

def main(source="content",dest="dist"):
    typer.config = {
        "source": source,
        "dest": dest
    }

    Site(**main.config).build

typer.run()