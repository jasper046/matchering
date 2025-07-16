
import pickle
import numpy as np

def save_preset(preset: dict, file_path: str):
    """Saves an analysis preset to a file."""
    with open(file_path, "wb") as f:
        pickle.dump(preset, f)

def load_preset(file_path: str) -> dict:
    """Loads an analysis preset from a file."""
    with open(file_path, "rb") as f:
        return pickle.load(f)

def blend_presets(preset_paths: list, new_preset_path: str):
    """Blends multiple presets into a new one by padding and averaging."""
    presets = [load_preset(path) for path in preset_paths]

    blended_preset = {}
    all_keys = set(key for p in presets for key in p.keys())

    for key in all_keys:
        values = [p.get(key) for p in presets if p.get(key) is not None]
        if not values:
            continue

        if isinstance(values[0], np.ndarray):
            arrays = values

            # Find the maximum shape across all arrays for this key
            max_shape = list(arrays[0].shape)
            for arr in arrays[1:]:
                for i in range(len(max_shape)):
                    max_shape[i] = max(max_shape[i], arr.shape[i])

            # Pad each array to the max shape
            padded_arrays = []
            for arr in arrays:
                pad_width = []
                for i in range(arr.ndim):
                    pad_width.append((0, max_shape[i] - arr.shape[i]))
                padded_arr = np.pad(arr, pad_width, 'constant', constant_values=0)
                padded_arrays.append(padded_arr)

            # Calculate the mean of the padded arrays
            blended_preset[key] = np.mean(padded_arrays, axis=0)

        elif isinstance(values[0], (int, float)):
            blended_preset[key] = np.mean(values)
        else:
            # For non-numeric/non-array types, just take the value from the first preset
            blended_preset[key] = values[0]

    save_preset(blended_preset, new_preset_path)
