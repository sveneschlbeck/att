# **att**
Terminal-based audio-to-text converter

*****
![GitHub language count](https://img.shields.io/github/languages/count/sveneschlbeck/att?color=pink)
![GitHub top language](https://img.shields.io/github/languages/top/sveneschlbeck/att?color=white)
![GitHub search hit counter](https://img.shields.io/github/search/sveneschlbeck/att/goto?color=brown)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sveneschlbeck/att?color=azure)
![GitHub repo size](https://img.shields.io/github/repo-size/sveneschlbeck/att?color=orange)
![GitHub last commit](https://img.shields.io/github/last-commit/sveneschlbeck/att)attatt
*****

## Project description

A terminal-based audio-to-text converter written in python, enabling you to convert `.wav` files or microphone input into text and save it to a file.

## Requirements

To run the main python modules `att_wav.py` and `mtt.py`, you need to install the following packages:  
- `speech_recognition`
- `pydub`
- `time`
- `pyaudio`

The installation method depends on the environment/ package manager you are using. The following examples show the installation of `pydub` for a standard python environment with pip and for an Anaconda environment via conda.

```python
pip install pydub
```

```python
conda install -c conda-forge pydub
```

## License

This code is licensed under ``GPL-3.0 License``.

## Example usage

To convert an audio file to text, start a terminal session, navigate to the location of the required module (e.g. `att_wav.py`) and start a python shell running the code by typing ```python att_wav.py```.

## Hardware & Software Requirements

These programs can be run without much computing power. They can be executed on any modern device fullfilling minimal RAM/ CPU standards.
