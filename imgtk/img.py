from typing import Callable

from PIL import Image
from pypipeline.item import Item
from stdl.fs import ensure_paths_exist


class ImageItem(Item):
    def __init__(self, path: str, loader: Callable = Image.open) -> None:
        super().__init__()
        self.path = path
        ensure_paths_exist(self.path)
        self._data: Image.Image = None  # type:ignore
        self.loader = loader

    def __repr__(self) -> str:
        return self.path

    def load(self):
        if self._data is None:
            try:
                self._data = self.loader(self.path)
            except Exception as e:
                self.discarded = True
                self.unload()

    def unload(self):
        if self._data is not None:
            self._data.close()
            self._data = None  # type:ignore

    def on_discard(self) -> None:
        self.unload()

    @property
    def data(self) -> Image.Image:
        self.load()
        return self._data
