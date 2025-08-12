# https://leetcode.com/problems/integer-to-english-words
import pytest

INT_NAMES = {
    1000000000: "Billion",
    1000000: "Million",
    1000: "Thousand",
    100: "Hundred",
    90: "Ninety",
    80: "Eighty",
    70: "Seventy",
    60: "Sixty",
    50: "Fifty",
    40: "Forty",
    30: "Thirty",
    20: "Twenty",
    19: "Nineteen",
    18: "Eighteen",
    17: "Seventeen",
    16: "Sixteen",
    15: "Fifteen",
    14: "Fourteen",
    13: "Thirteen",
    12: "Twelve",
    11: "Eleven",
    10: "Ten",
    9: "Nine",
    8: "Eight",
    7: "Seven",
    6: "Six",
    5: "Five",
    4: "Four",
    3: "Three",
    2: "Two",
    1: "One",
    0: "Zero",
}

PHASES = (
    INT_NAMES[100],
    INT_NAMES[1_000],
    INT_NAMES[1_000_000],
    INT_NAMES[1_000_000_000],
)


class Solution:
    def numberToWords(self, num: int) -> str:
        return self.numberToWords_pair(num)

    def numberToWords_pair(self, num: int) -> str:
        if num == 0:
            return "Zero"

        for value, word in INT_NAMES.items():
            # Check if the number is greater than or equal to the current unit
            if num >= value:
                # Convert the quotient to words if the current unit is 100 or greater
                prefix = (
                    (self.numberToWords_pair(num // value) + " ") if num >= 100 else ""
                )

                # Get the word for the current unit
                unit = word

                # Convert the remainder to words if it's not zero
                suffix = (
                    "" if num % value == 0 else " " + self.numberToWords(num % value)
                )

                return prefix + unit + suffix

        return ""

    @staticmethod
    def numberToWords_rec(num: int) -> str:
        # Recursive function to convert numbers to words
        # Handles numbers based on their ranges: <10, <20, <100, <1000, <1000000, <1000000000, and >=1000000000
        def _convert_to_words(my_num: int) -> str:
            if my_num < 10:
                return below_ten[my_num]
            if my_num < 20:
                return below_twenty[my_num - 10]
            if my_num < 100:
                return below_hundred[my_num // 10] + (
                    " " + _convert_to_words(my_num % 10) if my_num % 10 != 0 else ""
                )
            if my_num < 1000:
                return (
                        _convert_to_words(my_num // 100)
                        + " Hundred"
                        + (
                            " " + _convert_to_words(my_num % 100)
                            if my_num % 100 != 0
                            else ""
                        )
                )
            if my_num < 1000000:
                return (
                        _convert_to_words(my_num // 1000)
                        + " Thousand"
                        + (
                            " " + _convert_to_words(my_num % 1000)
                            if my_num % 1000 != 0
                            else ""
                        )
                )
            if my_num < 1000000000:
                return (
                        _convert_to_words(my_num // 1000000)
                        + " Million"
                        + (
                            " " + _convert_to_words(my_num % 1000000)
                            if my_num % 1000000 != 0
                            else ""
                        )
                )
            return (
                    _convert_to_words(my_num // 1000000000)
                    + " Billion"
                    + (
                        " " + _convert_to_words(my_num % 1000000000)
                        if my_num % 1000000000 != 0
                        else ""
                    )
            )

        # Arrays to store words for numbers less than 10, 20, and 100
        below_ten = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        below_twenty = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        below_hundred = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"
        # Call the helper function to start the conversion
        return _convert_to_words(num)

    @staticmethod
    def numberToWords_iter(num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"

        # Arrays to store words for single digits, tens, and thousands
        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        # StringBuilder to accumulate the result
        result = ""
        group_index = 0

        # Process the number in chunks of 1000
        while num > 0:
            # Process the last three digits
            if num % 1000 != 0:
                group_result = ""
                part = num % 1000

                # Handle hundreds
                if part >= 100:
                    group_result += ones[part // 100] + " Hundred "
                    part %= 100

                # Handle tens and units
                if part >= 20:
                    group_result += tens[part // 10] + " "
                    part %= 10

                # Handle units
                if part > 0:
                    group_result += ones[part] + " "

                # Append the scale (thousand, million, billion) for the current group
                group_result += thousands[group_index] + " "
                # Insert the group result at the beginning of the final result
                result = group_result + result
            # Move to the next chunk of 1000
            num //= 1000
            group_index += 1

        return result.strip()

    @staticmethod
    def numberToWords_mine(num: int) -> str:
        def generate_name_from_three_digits(chunk):
            if chunk == 0:
                return ""
            if chunk % 100 in INT_NAMES and chunk > 100 and 10 < chunk % 100 < 20:
                return f"{INT_NAMES[chunk // 100]} Hundred {INT_NAMES[chunk % 100]} "

            final_str = ""
            if INT_NAMES.get(chunk):
                final_str += (
                    f"{INT_NAMES[chunk]} "
                    if chunk < 100
                    else f"One {INT_NAMES[chunk]} "
                )
            else:
                curr_place = 1
                while chunk > 0:
                    chunk, val = divmod(chunk, 10)
                    if val == 0:
                        curr_place *= 10
                        continue
                    if curr_place == 1:
                        final_str = INT_NAMES[val] + " " + final_str
                    elif curr_place == 100:
                        final_str = (
                                INT_NAMES[val] + " " + INT_NAMES[100] + " " + final_str
                        )
                    else:
                        final_str = INT_NAMES[val * curr_place] + " " + final_str
                    curr_place *= 10
            return final_str

        def parse_chunks(chunked_num: list[int]):
            curr_places = len(chunked_num) - 1
            phase = PHASES[curr_places]
            all_strs = []

            for chunk in chunked_num:
                created_str = generate_name_from_three_digits(chunk)

                # add the qualifier at the end if it is over 1000
                if curr_places > 0 and created_str:
                    created_str = created_str + phase
                if created_str:
                    all_strs.append(created_str)
                curr_places -= 1
                phase = PHASES[curr_places]
            return " ".join(all_strs).strip()

        if INT_NAMES.get(num):
            return INT_NAMES[num] if num < 100 else "One " + INT_NAMES[num]

        chunks = []
        while num > 0:
            num, remainder = divmod(num, 1000)
            chunks.insert(0, remainder)
        return parse_chunks(chunks)


@pytest.mark.parametrize(
    "num,expected",
    [
        (1_000_010, "One Million Ten"),
        (0, "Zero"),
        (1, "One"),
        (16, "Sixteen"),
        (30, "Thirty"),
        (31, "Thirty One"),
        (100, "One Hundred"),
        (101, "One Hundred One"),
        (111, "One Hundred Eleven"),
        (119, "One Hundred Nineteen"),
        (123, "One Hundred Twenty Three"),
        (223, "Two Hundred Twenty Three"),
        (211, "Two Hundred Eleven"),
        (1_100, "One Thousand One Hundred"),
        (1_101, "One Thousand One Hundred One"),
        (2_100, "Two Thousand One Hundred"),
        (2_200, "Two Thousand Two Hundred"),
        (2_345, "Two Thousand Three Hundred Forty Five"),
        (12_345, "Twelve Thousand Three Hundred Forty Five"),
        (16_000, "Sixteen Thousand"),
        (16_013, "Sixteen Thousand Thirteen"),
        (23_000, "Twenty Three Thousand"),
        (119_000, "One Hundred Nineteen Thousand"),
        (123_345, "One Hundred Twenty Three Thousand Three Hundred Forty Five"),
        (
                1_234_567,
                "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        ),
    ],
)
def test_int_to_words(num: int, expected: str) -> None:
    assert Solution().numberToWords(num) == expected
