# splitflac

**Note:** This script requires external tools such as `shnsplit`, `cuetag.sh`, and `flac`. It is a command-line utility for splitting `.flac` audio files using a `.cue` sheet.

## Overview

`splitflac` is a minimal CLI tool that splits a single `.flac` album file into individual tracks using a `.cue` file.  
It also applies tags using `cuetag.sh` if available.

## Features

- 🎵 Splits `.flac` files based on `.cue` sheets
- 🏷️ Adds tags automatically using `cuetag.sh` (if present)
- 📁 Organises output into a separate directory
- 🐧 Designed for Linux systems

## Requirements

- `shntool`
- `cuetag.sh` (part of cuetools)
- `flac`
- Bash-compatible shell

Make sure these are installed and available in your `$PATH`.

## Installation

```bash
git clone https://github.com/loglux-lab/splitflac.git
cd splitflac
chmod +x split.py
```

## Usage

```bash
python split.py album.flac album.cue
```

The script will:
1. Create a folder named `album_split`
2. Use `shnsplit` to split the `.flac` file
3. Add tags with `cuetag.sh` (if found)
4. Move the resulting `.flac` files into the folder

## Example

```bash
python split.py "Pink Floyd - Animals.flac" "Pink Floyd - Animals.cue"
```

## License

MIT License — see [LICENSE](LICENSE) for details.
