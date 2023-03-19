import click
import typer
import typer.core

from great_expectations.cli.init import init as gx_init
from kedro.framework.cli.utils import call

from kedro_great_expectations._util import doc

typer.core.rich = None  # https://github.com/kedro-org/kedro/issues/1752


@click.group(name="kedro-great-expectations")
def commands():
    pass


@commands.group()
def great_expectations():
    """Validate, document, and profile data using Great Expectations."""


app = typer.Typer()


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
@doc(gx_init.__doc__)
def init(ctx: typer.Context):
    call(["great_expectations", "init", *ctx.args])


typer_click_object = typer.main.get_command(app)

great_expectations.add_command(typer_click_object, "init")
