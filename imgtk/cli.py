from pypipeline import PyPipelineCLI
from pypipeline.pipeline_action import get_parsable_actions
from stdl.fs import IMAGE_EXT, get_files_in, os

from imgtk.filters import FILTERS_MAPPING
from imgtk.img import ImageItem
from imgtk.transformers import TRANSFORMERS_MAPPING


class imgtkCLI(PyPipelineCLI):
    name = "imgtk"

    def collect_items(self, items: list[str]) -> list[ImageItem]:
        image_files = []
        for i in items:
            if os.path.isdir(i):
                image_files.extend(get_files_in(i, IMAGE_EXT))
            else:
                if os.path.isfile(i) and i.endswith(IMAGE_EXT):
                    image_files.append(i)
        images = [ImageItem(i) for i in image_files]
        self.log_info(f"found {len(images)} images")
        return images


def cli():
    PARSABLE_FILTERS = get_parsable_actions(FILTERS_MAPPING.values())  # type: ignore
    PARSABLE_TRANSFORMERS = get_parsable_actions(TRANSFORMERS_MAPPING.values())  # type: ignore
    cli = imgtkCLI(filters=PARSABLE_FILTERS, transformers=PARSABLE_TRANSFORMERS)
    cli.run()


if __name__ == "__main__":
    cli()

__all__ = ["cli"]
