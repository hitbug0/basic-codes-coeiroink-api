# basic-codes-coeiroink-api
A set of basic Python code snippets to utilize the COEIROINK API.

## Requirement
### COEIROINK Installation
Please download and install COEIROINK from [the official page](https://coeiroink.com/).

### Environment
Supported platforms: Windows 10 or 11

### Code Modifications
- `connect.ps1`
    - 20th line: Please specify the correct path for chrome.exe.
- `start.bat`
    - 2nd line: Please specify the correct path for COEIROINKv2.exe.
- `text2audio.py`
    - Please update `SPEAKER_INFO` in this code according to the 'Usage' section below.

## Usage
1. Run start.bat:
    - COEIROINK will launch automatically.
    - The API documentation page will also open automatically.
        - Please refer to this page if you wish to improve the codes.
    - `check_speaker_info.py` will also be executed automatically.
1. When adding a new model, update `SPEAKER_INFO` in `text2audio.py` according to the output of `check_speaker_info.py`.
    - Write the conversation content you want to convert to audio in `input.txt`.
1. Run run.bat:
    - `text2audio.py` will be executed automatically.
