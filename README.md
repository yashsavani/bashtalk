# bashtalk

This is a command-line interface application that records voice input, converts the voice input into text, and uses an OpenAI LLM (language model) to generate a bash script corresponding to the converted text. It provides options to customize the actions, such as skipping the LLM model, automatically running the generated script, and providing verbose output.

## Requirements
- Python 3.6 or above
- [SoX](http://sox.sourceforge.net/)
- [OpenAI Python client](https://github.com/openai/openai-cookbook/blob/main/examples/setup.md)
- LLM

## Installation
1. Make sure you have Python 3.6 or above installed. You can check your Python version using the following command in the terminal:
   ```
   python --version
   ```
2. Install the SoX from http://sox.sourceforge.net/.
3. Install the package dependencies by running pip install from the root directory:
   ```
   pip install -r requirements.txt
   ```
4. Setup and authenticate the OpenAI Python client. For more details, checkout [OpenAI Python client setup](https://github.com/openai/openai-cookbook/blob/main/examples/setup.md).
5. Download and setup the LLM.

## Usage
You can run the program as a Python script. Here's a description of the various arguments:
- `-d`, `--dir_path` (default: `/tmp`): Directory to save files
- `-f`, `--file_name` (default: `audio_record.mp3`): Name of the audio file
- `-m`, `--model_name` (default: `gpt-3.5-turbo`): LLM model name
- `-s`, `--skip_llm`: Skip running the LLM model
- `-y`, `--auto_run`: Automatically run the script without asking for confirmation
- `-v`, `--verbose`: Verbose output
- `-c`, `--context_file`: Context file for LLM prompt

Here is an example of running the script:
```
python main.py -d ~/Documents -f audio.mp3 -m gpt-3.5-turbo -v
```
This command records audio input, saves it to `~/Documents/audio.mp3`, converts it to text, runs the `gpt-3.5-turbo` LLM model to generate a bash script, and outputs all actions verbosely.

## Notes
This is a basic version of "Voice to Text to Script" service. It uses external dependencies such as SoX, OpenAI, and LLM models. Please make sure that all dependencies are properly installed and setup. For more advanced usage, consider integrating it with other systems or extending it with more utility functions.

## License
This project is licensed under the terms of the MIT license.
