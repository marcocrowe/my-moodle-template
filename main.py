"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Main module to run the program
"""

from my_moodle import (
    __version__,
    ConfigUtility,
    CourseStatus,
    MoodleDataDownloader,
    MoodleDataUtility,
)


def main() -> None:
    """Main function"""

    print(f"Using my_moodle version: {__version__}\n")

    program, server, token = ConfigUtility.check_and_read_config()

    moodle_data_downloader = MoodleDataDownloader(program, server, token, data_dir="")

    courses: list = moodle_data_downloader.download_courses()
    for course in courses:
        course["tiny-url"] = MoodleDataUtility.create_tiny_url(course["viewurl"])

    print("Courses: All")
    print(MoodleDataUtility.create_data_frame(courses, url_column="tiny-url"))
    print()

    active_courses: list = MoodleDataUtility.get_courses_by_status(
        courses, CourseStatus.ACTIVE
    )

    print("Courses: Active")
    print(MoodleDataUtility.create_data_frame(active_courses, url_column="tiny-url"))
    print()

    favourite_courses: list = MoodleDataUtility.get_courses_favoured(courses)

    print("Courses: Favourite")
    print(MoodleDataUtility.create_data_frame(favourite_courses, url_column="tiny-url"))
    print()


# Call the main function
if __name__ == "__main__":
    main()
