import sys
import numpy as np
from matchering.presets import load_preset

def inspect_preset(preset_path: str):
    """Loads and inspects a preset file."""
    print(f"Inspecting preset: {preset_path}")
    try:
        preset = load_preset(preset_path)
    except FileNotFoundError:
        print(f"Error: Preset file not found at '{preset_path}'")
        return

    for key, value in preset.items():
        print(f"\n--- Key: '{key}' ---")
        if isinstance(value, np.ndarray):
            print(f"  Type: NumPy Array")
            print(f"  Shape: {value.shape}")
            print(f"  Data Type: {value.dtype}")
            # Print a small sample of the array
            print(f"  Sample (first 5 elements): {value.flatten()[:5]}...")
        else:
            print(f"  Type: {type(value).__name__}")
            print(f"  Value: {value}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inspect_preset.py <path_to_preset.pkl>")
        sys.exit(1)

    preset_file = sys.argv[1]
    inspect_preset(preset_file)
