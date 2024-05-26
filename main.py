"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Main module to run the program
"""

from os import getcwd
from my_moodle import ConfigUtility, CourseStatus, DataUtility, MoodleDataDownloader


def main() -> None:
    """Main function"""

    MoodleDataDownloader.display_version()
    program, server, token = ConfigUtility.check_and_read_config()
    moodle_data_downloader = MoodleDataDownloader(program, server, token, getcwd())

    courses = moodle_data_downloader.download_my_json_data()

    for course in courses:
        course["tiny-url"] = DataUtility.create_tiny_url(course["viewurl"])

    active_courses = DataUtility.get_courses_by_status(courses, CourseStatus.ACTIVE)
    favourite_courses: list = DataUtility.get_courses_favoured(courses)

    print("Courses: All")
    print(DataUtility.create_table(courses, url_column="tiny-url"))
    print()

    print("Courses: Active")
    print(DataUtility.create_table(active_courses, url_column="tiny-url"))
    print()

    print("Courses: Favourite")
    print(DataUtility.create_table(favourite_courses, url_column="tiny-url"))
    print()


# Call the main function
if __name__ == "__main__":
    main()
