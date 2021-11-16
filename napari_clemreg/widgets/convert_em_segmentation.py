#!/usr/bin/env python3
# coding: utf-8
from magicgui import magic_factory
from napari.types import LabelsData, ImageData
from pathlib import Path
import numpy as np

# @magic_factory
# def change_layer_type(input: ImageData) -> LabelsData:
#     return input

def predict_from_model():
    pass

@magic_factory
def predict_from_unet(input: ImageData, model_path: Path) -> LabelsData:
    segmentation = predict_from_model(input)
    return segmentation
# Widget to load unet model
# Choose layer which was used for sparse segmentation
# Train button
# Run predictions on chosen layer from unet model
