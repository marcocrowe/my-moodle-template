"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Update template
"""

from os import getcwd
from my_moodle import update_my_moodle_template

CURRENT_VERSION = "1.0.5"


def main():
    """Update the My Moodle template."""
    update_my_moodle_template(getcwd(), CURRENT_VERSION)


if __name__ == "__main__":
    main()
