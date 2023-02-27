from img import ImageItem
from PIL import ImageFilter
from pypipeline.pipeline_item import PipelineItem
from pypipeline.transformer import SEP, Transformer
from stdl import fs


class Crop(Transformer):
    """
    Crop the image to the given box.

    Args:
        x1 (int): The left edge of the box.
        y1 (int): The upper edge of the box.
        x2 (int): The right edge of the box.
        y2 (int): The lower edge of the box.

    """

    abbrev = "cr"

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        super().__init__()
        self.box = (x1, y1, x2, y2)

    def process(self, img: ImageItem) -> PipelineItem:
        img._data = img.data.crop(self.box)
        return img

    @classmethod
    def parse(cls, val: str):
        p1, p2 = val.split(SEP)
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        return cls(int(x1), int(y1), int(x2), int(y2))


class Convert(Transformer):
    """
    Convert the image to the given mode. Valid modes are: L, RGB, CMYK, GRAYSACLE.
    """

    abbrev = "cnv"

    MODES = ["L", "RGB", "CMYK", "GRAYSACLE"]

    def __init__(self, mode: str) -> None:
        super().__init__()
        mode = mode.upper()
        if mode == "GRAYSCALE":
            mode = "L"
        if not mode in self.MODES:
            raise ValueError(f"Invalid mode: {mode}. Valid modes: {', '.join(self.MODES)}")
        self.mode = mode

    def process(self, img: ImageItem) -> PipelineItem:
        img._data = img.data.convert(self.mode)
        return img

    @classmethod
    def parse(cls, val: str):
        return cls(val)


class Resize(Transformer):

    """
    Resize the image to the given size.

    Args:
        width (int): The width of the image.
        height (int): The height of the image.
    """

    abbrev = "rs"

    def __init__(self, width: int | None = None, height: int | None = None) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def process(self, img: ImageItem) -> PipelineItem:
        match (self.width, self.height):
            case (None, None):
                box = (img.data.width, img.data.height)
            case (None, h):
                box = (img.data.width, h)
            case (w, None):
                box = (w, img.data.height)
            case (w, h):
                box = (w, h)
            case _:
                raise ValueError((self.width, self.height))
        img._data = img.data.resize(size=box)
        return img

    @classmethod
    def parse(cls, val: str):
        args = [int(i) for i in val.split(SEP) if i != ""]
        match args:
            case ["", ""]:
                return cls(None, None)
            case [w, ""]:
                return cls(int(w), None)
            case ["", h]:
                return cls(None, int(h))
            case [x, y]:
                return cls(int(x), int(y))
            case _:
                raise ValueError(args)


class Save(Transformer):
    abbrev = "s"
    """
    Save the image to the given directory.
    """

    def __init__(self, directory: str) -> None:
        super().__init__()
        self.directory = directory

    def process(self, img: ImageItem) -> PipelineItem:
        filename = fs.basename(img.path)
        filepath = fs.joinpath(self.directory, filename)
        img.data.save(filepath)
        return img

    @classmethod
    def parse(cls, val: str):
        return cls(val)


class Move(Transformer):
    abbrev = "mv"
    """
    Move the image to the given directory.
    """

    def __init__(self, directory: str) -> None:
        super().__init__()
        self.directory = directory

    def process(self, img: ImageItem) -> PipelineItem:
        img_file = fs.File(img.path).move_to(self.directory)
        img.path = img_file.path
        return img

    @classmethod
    def parse(cls, val: str):
        return cls(val)


class Filter(Transformer):
    abbrev = "f"
    """
    Apply the given filter to the image.
    Valid filters are: blur, contour, detail, edge_enhance, edge_enhance_more, emboss, find_edges, sharpen, smooth, smooth_more.
    """

    filters = {
        f.name.upper().replace(" ", "_"): f
        for f in [
            ImageFilter.BLUR,
            ImageFilter.CONTOUR,
            ImageFilter.DETAIL,
            ImageFilter.EDGE_ENHANCE,
            ImageFilter.EDGE_ENHANCE_MORE,
            ImageFilter.EMBOSS,
            ImageFilter.FIND_EDGES,
            ImageFilter.SHARPEN,
            ImageFilter.SMOOTH,
            ImageFilter.SMOOTH_MORE,
        ]
    }

    def __init__(self, name: str) -> None:
        super().__init__()
        name = name.upper().replace(" ", "_")
        if not name in self.filters:
            raise ValueError(
                f"Invalid filter: {name}. Valid filters: {', '.join(self.filters.keys())}"
            )
        self.filter = self.filters[name]

    def process(self, img: ImageItem) -> PipelineItem:
        img._data = img.data.filter(self.filter)
        return img

    @classmethod
    def parse(cls, val: str):
        return cls(val)


class Rotate(Transformer):
    abbrev = "rot"

    def __init__(self, angle: int) -> None:
        super().__init__()
        self.angle = angle

    def process(self, img: ImageItem) -> PipelineItem:
        img._data = img.data.rotate(self.angle, expand=True)
        return img


class Scale(Transformer):
    abbrev = "sc"

    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def process(self, img: ImageItem) -> PipelineItem:
        img._data = img.data.resize((int(img.data.width * self.x), int(img.data.height * self.y)))
        return img

    @classmethod
    def parse(cls, val: str):
        args = [int(i) for i in val.split(SEP) if i != ""]
        match args:
            case ["", ""]:
                raise ValueError(val)
            case [w, ""]:
                return cls(float(w), float(w))
            case ["", h]:
                return cls(float(h), float(h))
            case [x, y]:
                return cls(float(x), float(y))
            case _:
                raise ValueError(args)


TRANSFORMERS_MAPPING = {
    i.__name__: i for i in [Scale, Rotate, Filter, Move, Save, Resize, Convert, Crop]
}
