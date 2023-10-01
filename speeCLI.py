import argparse
import re
import subprocess
import openai
import os
import llm
import tempfile


def record_voice(file_path, verbose):
    """Records voice using sox and saves to a temporary file."""
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
            temp_wav_path = temp_wav.name

        if verbose:
            print("Recording. Press Ctrl+C to stop.")

        sox_process = subprocess.Popen(["sox", "-q", "-d", temp_wav_path])
        sox_process.wait()

    except KeyboardInterrupt:
        sox_process.terminate()
        sox_process.wait()
        if verbose:
            print("Recording stopped.")

    subprocess.run(["sox", temp_wav_path, file_path])
    os.remove(temp_wav_path)


def convert_to_text(file_path):
    """Converts audio file to text using OpenAI's Whisper ASR."""
    with open(file_path, "rb") as f:
        transcription = openai.Audio.transcribe("whisper-1", f)
    return transcription["text"]


def run_llm(text, model):
    """Runs llm to get a bash script for the transcribed text."""
    return model.prompt(f"Give me a bash script inside ```bash ``` to do the following: {text}").text()


def extract_script(text):
    """Extracts the bash script from llm output."""
    pattern = r'```bash\n(.*?)\n```'
    matches = re.findall(pattern, text, re.DOTALL)
    if len(matches) == 0:
        return [""]
    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Voice to Text to Script CLI")
    parser.add_argument("-d", "--dir_path", default="/tmp",
                        help="Directory to save files")
    parser.add_argument(
        "-f", "--file_name", default="audio_record.mp3", help="Name of the audio file")
    parser.add_argument(
        "-m", "--model_name", default="gpt-3.5-turbo", help="LLM model name")
    parser.add_argument("-s", "--skip_llm", action="store_true",
                        help="Skip running the LLM model")
    parser.add_argument("-y", "--auto_run", action="store_true",
                        help="Automatically run the script without asking")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose output")

    args = parser.parse_args()
    file_path = os.path.join(args.dir_path, args.file_name)

    record_voice(file_path, args.verbose)

    if args.verbose:
        print()
        print("Converting audio to text...")

    transcribed_text = convert_to_text(file_path)

    if args.verbose:
        print("Transcribed text:")
        print(transcribed_text)
        print()

    if not args.skip_llm:
        model = llm.get_model(args.model_name)
        llm_output = run_llm(transcribed_text, model)

        if args.verbose:
            print("LLM output:")
            print(llm_output)
            print()

        script_text = extract_script(llm_output)[0]

        if args.verbose:
            print("Script:")
            print(script_text)

        script_file_path = os.path.join(args.dir_path, "bash_script.sh")
        with open(script_file_path, "w") as f:
            f.write(script_text)

        if not args.auto_run:
            print("Do you want to run the script? [Yn]")
            answer = input().strip().lower()
            if answer != "n":
                subprocess.run(["bash", script_file_path])
        else:
            subprocess.run(["bash", script_file_path])

