# [My Moodle](https://github.com/marcocrowe/my-moodle-template "My Moodle")

This repository is a template for a Python package to download data from Moodle. Press the button below to use this template to create a new repository:

Clone the repository to your local machine:

Replace `USERNAME` with your GitHub username and `COLLEGE-MOODLE` with the name of the repository, i.e. `my-moodle` for mu for 'Maynooth University':

```bash
git clone https://wwww.github.com/USERNAME/COLLEGE-MOODLE.git
```

## Installation

To install the package, run the following command:

```bash
pip install my-moodle
```

You can then open [main.py](main.py) or [notebook-main.ipynb](notebook-main.ipynb) to start the program.

## Description

This package is a Python program to download data from Moodle. The program uses the Moodle API to download data from a Moodle server. The program is designed to download data from a specific course on a Moodle server. The program requires a token to access the Moodle server. The token is a secret key that is generated by the Moodle server.

## Sample Usage

The following is a sample usage of the package:

```python

%pip install my-moodle

from os import getcwd
from my_moodle import ConfigUtility, MoodleDataDownloader

def main() -> None:
    """Main function"""

    MoodleDataDownloader.display_version()
    program, server, token = ConfigUtility.check_and_read_config()
    moodle_data_downloader = MoodleDataDownloader(program, server, token, getcwd())
    moodle_data_downloader.download_my_data()

# Call the main function
if __name__ == "__main__":
    main()
```

## Get Moodle Token

Using <https://moodle.midwest.tus.ie/> as an example:

1. Open <https://moodle.midwest.tus.ie/user/managetoken.php>
2. Copy the key for 'Moodle mobile web service'.
3. The key is saved to a file [config.ini](config.ini)

```ini
[User]
program = Content Management Systems
server = https://moodle.midwest.tus.ie/
token = INSERT_YOUR_TOKEN
```

*Note: The token is a secret key, do not share it with anyone. Usually it is GUID like e.g. **63c1774a3eaf47db816c57ba1abafd40***

---
Copyright &copy; 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
