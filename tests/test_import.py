from importlib import import_module

import image_stack


def test_version_is_set():
    assert isinstance(image_stack.__version__, str)
    assert image_stack.__version__


def test_curated_dependencies_are_importable():
    for module_name in (
        "numpy",
        "PIL",
        "skimage",
        "scipy",
        "imageio",
        "tifffile",
        "cv2",
        "matplotlib",
        "torch",
        "torchvision",
    ):
        import_module(module_name)
