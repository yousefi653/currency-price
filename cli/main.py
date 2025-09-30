import click
import shlex
import feature


@click.group()
def cli():
    """To get the price and specifications of currency and gold."""
    pass


@cli.command(help="""To get the price of the currency you want.""")
@click.option(
    "--symbol",
    "-s",
    prompt="Please enter the currency symbol you want: ",
    help="Usage => price (--symbol or -s) SYBMOL",
)
def price(symbol):
    click.clear()
    symbol = symbol.strip()
    click.secho("=" * 30, bg="blue")
    feature.price(symbol)
    click.secho("=" * 30, bg="blue")


@cli.command(
    help="""To see the list of currencies and gold whose prices you can view."""
)
@click.option(
    "--type",
    "-t",
    required=False,
    type=click.Choice(["gold", "currency", "cryptocurrency"], case_sensitive=False),
    help="You can enter the type of what you want so that it will be shown to you.",
)
@click.option(
    "--all",
    "-a",
    is_flag=True,
    required=False,
    help="To see all available currencies and gold.",
)
def List(all=True, type=None):
    click.clear()
    click.secho(
        "\nThe list of currencies and gold whose prices you can view is as follows:\n",
        bold=True,
    )
    feature.List(type, all)
    click.echo("*".center(100, "*"))


def shell():
    click.clear()
    click.echo("=".center(100, "="))
    click.secho("Currency-price".center(100), fg="blue", bg="green", bold=True)
    click.secho("\nHello, thank you very much for using this program.", bold=True)
    click.echo("-".center(100, "-"))
    click.secho("\nHelp:\n", bold=True)
    cli(["--help"], standalone_mode=False)
    click.secho(
        "\n!!! Before you use any command, read the usage instructions with the command => [COMMAND] --help",
        bold=True,
        fg='red'
    )

    line = 0
    while True:
        try:
            line += 1
            command = input(f"\n[{line}]>> ")
            args = shlex.split(command.strip().lower())

            if args[0] == "clear":
                click.clear()
                continue
            if args[0] in ("exit", "quit"):
                break
            
            result = feature.check_command(args)
            if result is True:
                cli(args, standalone_mode=False)
            else:
                click.secho(result, bg='red', bold=True)

        except Exception as Error:
            print(f"had a Error {Error}")


if __name__ == "__main__":
    shell()
