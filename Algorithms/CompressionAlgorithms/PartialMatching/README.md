# Prediction by Partial Matching (PPM) Algorithm

## Overview

Prediction by Partial Matching (PPM) is a family of data compression algorithms based on the prediction of the next symbol in a sequence. PPM uses a model based on context and history to predict the probability distribution of the next symbol, and encodes the data based on these probabilities.

### Example
- **Input:** `abracadabra`
- **Compressed:** A list of integer counts representing the frequency of characters given the context.
- **Decompressed:** Reconstructs the original string from the compressed data.

## Files

- **ppm.py:** Contains the implementation of the PPM compression and decompression algorithms.
- **example.py:** Demonstrates how to use the PPM algorithm with example data.

## Usage

### Training the PPM Model

To train the PPM model on a given text:

```python
from ppm import ppm_train

text = "abracadabra"
order = 2
model = ppm_train(text, order)
print(f"Model: {model}")
