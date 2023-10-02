# bashtalk

This is a command-line interface application that records voice input, converts the voice input into text, and uses an OpenAI LLM (language model) to generate a bash script corresponding to the converted text. It provides options to customize the actions, such as skipping the LLM model, automatically running the generated script, and providing verbose output.

## Requirements
- Python 3.6 or above
- [SoX](http://sox.sourceforge.net/)
- [OpenAI Python client](https://github.com/openai/openai-cookbook/blob/main/examples/setup.md)
- LLM

## Installation

### Pip Installation
You can now install `bashtalk` directly from PyPI:
```bash
pip install bashtalk
```

### Manual Installation
1. Make sure you have Python 3.6 or above installed. You can check your Python version using the following command in the terminal:
   ```
   python --version
   ```
2. Install the SoX from http://sox.sourceforge.net/.
3. Clone the repository and navigate to its root directory.
4. Install the package dependencies:
   ```
   pip install .
   ```
5. Setup and authenticate the OpenAI Python client. For more details, checkout [OpenAI Python client setup](https://github.com/openai/openai-cookbook/blob/main/examples/setup.md).
6. Download and setup the LLM.

## Usage

After installation, you can run `bashtalk` directly from the command line:

```bash
bashtalk -d ~/Documents -f audio.mp3 -m gpt-3.5-turbo -v
```

Here's a description of the various arguments:
- `-d`, `--dir_path` (default: `/tmp`): Directory to save files
- `-f`, `--file_name` (default: `audio_record.mp3`): Name of the audio file
- `-m`, `--model_name` (default: `gpt-3.5-turbo`): LLM model name
- `-s`, `--skip_llm`: Skip running the LLM model
- `-y`, `--auto_run`: Automatically run the script without asking for confirmation
- `-v`, `--verbose`: Verbose output
- `-c`, `--context_file`: Context file for LLM prompt

## Notes
This is a basic version of bashtalk. It uses external dependencies such as SoX, OpenAI, and LLM models. Please make sure that all dependencies are properly installed and setup. For more advanced usage, consider integrating it with other systems or extending it with more utility functions.

## License
This project is licensed under the terms of the MIT license.
