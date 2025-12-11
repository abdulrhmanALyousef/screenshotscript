# Screenshot Processing Script

A Python script that captures a screenshot, converts it to grayscale, flips it horizontally, and saves the result to your Desktop.

## Features

- Captures a screenshot of your entire screen
- Converts the screenshot to grayscale
- Flips the image horizontally (mirror effect)
- Saves the processed image to your Desktop
- Displays the final image in a window

## Requirements

- Python 3.x
- pyautogui
- opencv-python (cv2)
- numpy

## Installation

Install the required packages using pip:

```bash
pip install pyautogui opencv-python numpy
```

## Configuration

Before running the script, open `p.py` and set your desired output path:

```python
# Set your desired output path here
imgPath = "/Users/YOUR_USERNAME/Desktop/final_image.png"  # Change this to your desired path
```

Replace `/Users/YOUR_USERNAME/Desktop/final_image.png` with your preferred location and filename.

### Example Paths:
- macOS: `/Users/username/Desktop/my_screenshot.png`
- Windows: `C:/Users/username/Desktop/my_screenshot.png`
- Linux: `/home/username/Pictures/my_screenshot.png`

## Usage

Run the script:

```bash
python3 p.py
```

The script will:
1. Take a screenshot of your screen
2. Process it (convert to grayscale and flip horizontally)
3. Save the result to your specified path
4. Display the image in a window
5. Wait for you to press any key to close the window

## How It Works

1. **Screenshot Capture**: Uses `pyautogui.screenshot()` to capture the current screen
2. **Color Conversion**: Converts the image from RGB to BGR format (OpenCV format)
3. **Grayscale Conversion**: Converts the colored image to grayscale
4. **Horizontal Flip**: Flips the image horizontally using `cv2.flip()`
5. **Save**: Saves the processed image to your specified path
6. **Display**: Shows the final result in a window

## Output

The processed image will be saved at the path you specified in the `imgPath` variable.

## Notes

- Press any key while the image window is active to close it
- The script will overwrite any existing file at the specified path
- Make sure the directory in your path exists before running the script
