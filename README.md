# imgstack-deps

A single dependency to bootstrap image-processing projects. `imgstack-deps`
pulls in a curated, version-pinned-with-headroom set of the most commonly
needed image-processing libraries so you don't have to hand-pick and pin them
yourself. It installs the importable `image_stack` package.

## Install

```bash
pip install imgstack-deps
```

This brings in:

- [`numpy`](https://numpy.org/)
- [`pillow`](https://python-pillow.org/)
- [`scikit-image`](https://scikit-image.org/)
- [`scipy`](https://scipy.org/)
- [`imageio`](https://imageio.readthedocs.io/)
- [`tifffile`](https://github.com/cgohlke/tifffile)
- [`opencv-python-headless`](https://github.com/opencv/opencv-python)
- [`matplotlib`](https://matplotlib.org/)
- [`torch`](https://pytorch.org/) / [`torchvision`](https://pytorch.org/vision/stable/index.html)

`pip install imgstack-deps` on Linux/Windows pulls PyTorch's default PyPI wheel,
which bundles CUDA support out of the box (no extra index needed) — `torch.cuda.is_available()`
will be `True` on a machine with a compatible NVIDIA GPU and drivers installed.
On macOS you get the CPU/MPS build.

## Usage

`image_stack` itself has no API — it exists purely to declare dependencies.
Import the libraries you need directly:

```python
import numpy as np
from PIL import Image
import cv2
```

## Development

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

## Release process

Releases are published to PyPI automatically via GitHub Actions using
[trusted publishing](https://docs.pypi.org/trusted-publishers/) whenever a
GitHub Release is published. Bump `__version__` in
[`src/image_stack/__init__.py`](src/image_stack/__init__.py), then cut a
release/tag to trigger the publish workflow.

Dependency updates (both Python packages and GitHub Actions) are proposed
automatically via Dependabot.
