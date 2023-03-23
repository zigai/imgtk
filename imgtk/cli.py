import select
import sys
from glob import glob

from pypipeline import PyPipelineCLI
from pypipeline.pipeline_action import get_parsable_actions
from stdl.fs import IMAGE_EXT, os, yield_files_in

from imgtk.filters import FILTERS_MAPPING
from imgtk.img import ImageItem
from imgtk.transformers import TRANSFORMERS_MAPPING


def read_stdin():
    if select.select([sys.stdin], [], [], 0.3)[0]:
        return sys.stdin.read().strip().splitlines()
    return []


def collect_files(items: list[str], ext=None, stdin=True):
    if stdin:
        items.extend(read_stdin())

    for filepath in items:
        if os.path.isdir(filepath):
            for i in yield_files_in(filepath, ext):
                yield i
        elif os.path.isfile(filepath):
            if ext is None or filepath.endswith(ext):
                yield filepath
        elif "*" in filepath:
            for i in glob(filepath, recursive=True):
                if ext is None or i.endswith(ext):
                    yield i
        else:
            raise ValueError(f"invalid path: {filepath}")


class imgtkCLI(PyPipelineCLI):
    name = "imgtk"

    def collect_items(self, items: list[str]) -> list[ImageItem]:
        images = [ImageItem(i) for i in collect_files(items, IMAGE_EXT)]
        self.log_info(f"found {len(images)} images")
        return images


def cli():
    imgtkCLI(
        filters=get_parsable_actions(FILTERS_MAPPING.values()),  # type: ignore
        transformers=get_parsable_actions(TRANSFORMERS_MAPPING.values()),  # type: ignore
    )


if __name__ == "__main__":
    cli()

__all__ = ["cli", "imgtkCLI"]
