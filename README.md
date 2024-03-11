# Parallel programming

## Description

This Python script is designed to showcase a performance comparison between multithreading and multiprocessing techniques for concurrent execution. The demonstration focuses on a geometric shape generation task, and the results are visualized using PyQT5 for a graphical representation of concurrent execution.

The script follows object-oriented programming principles to define classes representing various geometric shapes, including trapezoids, rectangles, and squares. 
To achieve concurrent execution, it leverages the ThreadPoolExecutor and ProcessPoolExecutor from the concurrent.futures module to distribute shape generation tasks across multiple threads and processes.

## Features

- **Multithreaded Fetching:** The application spawns multiple threads, each responsible for fetching JSON data for a specific object ID concurrently, enhancing performance.

- **Dynamic Number Selection:** Users can dynamically select the number from using a spinbox, providing flexibility.

- **Thread Control:** Users can choose to enable or disable multithreading, allowing for experimentation with different fetching strategies.

- **Progress Tracking:** Although not implemented in the provided code, the application has the potential to include a progress bar to track the completion status of the fetching process.

## Prerequisites

- Python 3.x
- PyQt5

## Installation

1. Clone or download the project repository.
2. Install the required dependencies using the provided requirements.txt file:

```py
pip install -r requirements.txt
```
3. After installing the dependencies, run the run.py file to start the Figure calculator app.
```py
python run.py
```

## Result 
### All together
Number - 10.000 
- Multithreading: 0.25358 seconds
- Multiprocessing: 1.94703 seconds
- Mixed Approach: 0.50337 seconds

Number 100.000 
- Multithreading: 2.62054 seconds
- Multiprocessing: 40.94703 seconds
- Mixed Approach: 1.60921 seconds

### Separately
Number - 10.000 
- Only Multithreading: 0.19250 seconds
- Only Multiprocessing: 1.64703 seconds
- Mixed Approach: 0.17337 seconds

Number 100.000 
- Only Multithreading: 2.32054 seconds
- Only Multiprocessing: 33.14703 seconds
- Mixed Approach: 0.30921 seconds
