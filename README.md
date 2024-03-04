Certainly! Below is a basic README file for your Python script:

---

# MusicTools

## Introduction

`MusicTools` is a Python class that provides tools for working with music files. It includes functionality for finding the BPM (Beats Per Minute), detecting the key of a song, and extracting vocals and beats.

## Installation

To use the `MusicTools` class, you need to have the following Python libraries installed:

- [os](https://docs.python.org/3/library/os.html)
- [librosa](https://librosa.org/doc/main/index.html)
- [numpy](https://numpy.org/doc/stable/)
- [soundfile](https://pysoundfile.readthedocs.io/en/latest/)
- [datetime](https://docs.python.org/3/library/datetime.html)

You can install these libraries using the following command:

```bash
pip install librosa numpy soundfile
```

## Usage

To use the `MusicTools` class, follow these steps:

1. Import the class:

```python
from music_tools import MusicTools
```

2. Create an instance of the `MusicTools` class, providing the file path of the music file as an argument:

```python
music_tools = MusicTools(filepath="path/to/your/music/file.mp3")
```

3. Access the tools provided by the class, such as BPM detection, key finding, and vocal-beat extraction:

```python
bpm = music_tools.bpm_detector()
print(f"The BPM of the song is: {bpm}")

key = music_tools.key_finder()
print(f"The key of the song is: {key}")

music_tools.vocal_beat_extractor()
print("Vocal and beat files extracted successfully.")
```

## Class Methods

### `__init__(self, filepath=None)`

- Initializes the `MusicTools` class with an optional `filepath`.

### `load_file(self) -> bool`

- Loads the music file specified by `filepath` and sets the `y` (audio signal) and `sr` (sampling rate) attributes.

### `bpm_detector(self) -> str`

- Finds the BPM (Beats Per Minute) of the loaded music file and returns it as a formatted string.

### `key_finder(self) -> str`

- Calculates the chroma features of the loaded music file and determines the key of the song.

### `vocal_beat_extractor(self)`

- Separates the vocal and beat components of the loaded music file and saves them as separate audio files on the desktop.

## Example

For a complete example of using the `MusicTools` class, refer to the provided script `example_usage.py`.

---

Feel free to customize the README according to your needs, and if you have additional features or considerations, you can include them in the documentation.
