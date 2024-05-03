from itertools import zip_longest

import pytest


def create_version(version_string):
    parts = version_string.split(".")
    major = int(parts[0])
    minor = int(parts[1]) if len(parts) > 1 else 0
    patch = int(parts[2]) if len(parts) > 2 else 0
    bruh = int(parts[3]) if len(parts) > 3 else 0
    return Version(major, minor, patch, bruh)


class Version:
    def __init__(self, major=0, minor=0, patch=0, bruh=0):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.bruh = bruh

    def __gt__(self, other):
        if self.major > other.major:
            return True
        if self.minor > other.minor and other.major <= self.major:
            return True
        if (
            self.patch > other.patch
            and other.minor <= self.minor
            and other.major <= self.major
        ):
            return True
        if (
            self.bruh > other.bruh
            and other.patch <= self.patch
            and other.minor <= self.minor
            and other.major <= self.major
        ):
            return True
        return False

    def __eq__(self, other):
        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
            and self.bruh == other.bruh
        )

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        return self.compareVersion_mine(version1, version2)

    @staticmethod
    def compareVersion_theirs(version1: str, version2: str) -> int:
        def preprocess(version: str):
            return map(int, version.split("."))

        v1 = preprocess(version1)
        v2 = preprocess(version2)

        for x1, x2 in zip_longest(v1, v2, fillvalue=0):
            if x1 > x2:
                return 1
            if x1 < x2:
                return -1

        return 0

    @staticmethod
    def compareVersion_mine(version1: str, version2: str) -> int:
        my_version1 = create_version(version1)
        my_version2 = create_version(version2)
        if my_version1 == my_version2:
            return 0
        if my_version1 > my_version2:
            return 1
        else:
            return -1


@pytest.mark.parametrize(
    "version1,version2,expected",
    [
        ("1.0", "0.1", 1),
        ("0.1", "1.0", -1),
        ("1.0", "1", 0),
        ("1.1", "1", 1),
        ("1.01", "1.02.1", -1),
        ("1.02.2", "1.02.3", -1),
        ("1", "2", -1),
        ("3.0.4.10", "3.0.4.2", 1),
    ],
)
def test_version_numbers(version1, version2, expected):
    assert Solution().compareVersion(version1, version2) == expected
