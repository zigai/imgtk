import os
import re
from typing import Any, Callable

from PIL import Image
from pypipeline.pipeline_item import PipelineItem


class ImageItem(PipelineItem):
    def __init__(self, path: str, loader: Callable = Image.open) -> None:
        super().__init__()
        self.path = path
        assert os.path.exists(self.path), path
        self._data: Image.Image = None
        self.loader = loader

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(path='{self.path}', discarded={self.discarded})"

    def load(self):
        if self._data is None:
            self._data = self.loader(self.path)

    def unload(self):
        if self._data is not None:
            self._data.close()
            self._data = None

    @property
    def data(self):
        self.load()
        return self._data
