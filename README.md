# Sorting Visualiser

Sorting Visualiser is a Python application built using `customtkinter` that visually demonstrates sorting algorithms such as **Bubble Sort** and **Selection Sort**. Users can interact with the application by selecting a sorting algorithm, adjusting animation speed, and shuffling the dataset.

## Features
- **Graphical Sorting Visualization**: Displays real-time sorting animations.
- **Sorting Algorithms Implemented**:
  - Bubble Sort
  - Selection Sort
- **Interactive UI**:
  - Dropdown menu to select sorting algorithms
  - Shuffle button to randomize array
  - Speed slider to adjust animation speed
- **Color Animations**:
  - Highlights elements being swapped or compared.
  - Animated transitions for swapping elements.

## Installation
To run the Sorting Visualiser, ensure you have Python installed and install the required dependencies.

### Prerequisites
- Python 3.7+
- `customtkinter` module

### Install Dependencies
Run the following command to install `customtkinter`:
```bash
pip install customtkinter
```

## Usage
Run the following command to start the application:
```bash
python main.py
```

## How It Works
1. **Choose a sorting algorithm** from the dropdown menu.
2. **Click 'SORT'** to visualize the sorting process.
3. **Click 'SHUFFLE'** to randomize the array.
4. **Adjust speed** using the slider to modify animation speed.

## Sorting Algorithms Complexity
| Algorithm       | Best Case | Average Case | Worst Case |
|---------------|-----------|-------------|------------|
| Bubble Sort    | O(n)      | O(n²)       | O(n²)      |
| Selection Sort | O(n²)     | O(n²)       | O(n²)      |

## File Structure
```
SortingVisualiser/
│── main.py          # Main application file
│── README.md        # Project documentation
```
