import click
import re
import os
import collections

from iunctus.utils.files import find, filter_file


def preview_files(files, statuses):

    if len(files) < 1:
        click.echo("No file to preview")
        return

    colors = ["green", "red", "bright_black"]
    messages = ["", " (OVERWRITE)", " (IGNORE)"]
    lines = "\n".join(
        click.style(file + messages[status], fg=colors[status])
        for file, status in zip(files, statuses)
    )

    C = collections.Counter(statuses)
    C0 = C[0]
    C1 = C[1]
    C2 = C[2]

    lines += f"\n\n{len(files)} files: {C0} new, {C1} overwritten and {C2} ignored."
    click.echo(lines)


@click.command()
@click.pass_context
@click.argument("path", type=click.Path(exists=True), required=False)
@click.option(
    "-p",
    "--pattern",
    type=str,
    multiple=True,
    help="REGEX pattern(s) that images files must match.",
)
@click.option(
    "-r",
    "--recursive",
    is_flag=True,
    default=False,
    help="Search recursively in PATH (default: FALSE).",
)
@click.option(
    "-w",
    "--preview",
    is_flag=True,
    default=False,
    help="Preview list of images to add and exit.",
)
@click.option(
    "-a",
    "--any_pattern",
    is_flag=True,
    default=False,
    help="Image paths must match ANY pattern (default: ALL).",
)
@click.option(
    "-o",
    "--overwrite",
    is_flag=True,
    default=False,
    help="Overwrite image data files when duplicates.",
)
def add(ctxt, path, pattern, recursive, preview, any_pattern, overwrite):
    """
    Add image files to the current iunctus project.
    """
    if not path:
        path = "."

    print(dir(ctxt))
    print(ctxt.parent.params)

    patterns = [re.compile(p) for p in pattern]

    files = find(path, recursive)
    files = filter(lambda file: filter_file(file, patterns, any_pattern), files)

    if preview:
        files = list(files)
        preview_files(files, [2 for _ in files])
