import click


@click.group()
@click.option("-p", "--path", default=None)
def iunctus(path):
    pass


from iunctus.cli.add import add
from iunctus.cli.new import new
from iunctus.cli.show import show

iunctus.add_command(add)
iunctus.add_command(new)
iunctus.add_command(show)

if __name__ == "__main__":
    iunctus()
