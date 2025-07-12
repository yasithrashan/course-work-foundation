# Progression Outcome Histogram

This is a foundation coursework project that collects student credit data, determines progression outcomes, and visualizes the results using a histogram.

## Features

- Validates input credits for PASS, DEFER, and FAIL.
- Calculates progression outcomes:
  - **Progress**
  - **Trailer**
  - **Retriever**
  - **Exclude**
- Displays a histogram showing the count of each outcome using the `graphics` module.
- Saves progression data to a text file (`progression_data.txt`).
- Reads and prints saved progression data.

## Requirements

- Python 3.x
- `graphics.py` module (for drawing the histogram).  
  You can download it from [here](https://mcsp.wartburg.edu/zelle/python/graphics.py) or use any compatible graphics library.

## How to Run

1. Ensure `graphics.py` is in the same directory as the program.
2. Run the program:
   ```bash
   python progression_histogram.py
