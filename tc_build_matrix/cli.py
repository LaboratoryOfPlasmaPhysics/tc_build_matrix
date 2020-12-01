"""Console script for tc_build_matrix."""
import sys
import click
from tc_build_matrix import scan
from tc_build_matrix.io import to_yaml, from_yaml, to_dict


@click.group()
def main(args=None):
    return 0


@main.command(name='scan')
@click.option('--image-name', '-i')
def _(image_name):
    print(to_yaml(scan(name=image_name)))


@main.command(name='merge')
@click.option('--file', '-f', 'files', multiple=True)
def _(files):
    for file_name in files:
        with open(file_name, 'r') as data:
            from_yaml(data.read())


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
