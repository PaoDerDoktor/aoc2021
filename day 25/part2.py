"""
It has been an incredible Journey.

This was the first time I woke up every morning to an AoC puzzle and a french translation
(see my other repo https://github.com/PaoDerDoktor/AoC2021FR if interested), and I managed - with a lot of
determination - to finish nearly all of them in less than 24 hours. Only exceptions are last 3 days' translations
and Day 24, but that's more of a family obligations matter than a lack of skills/dedication.

I'm incredibly proud of myself. I NEVER thought I would get past day 15. But I did it. This time I did it. And I'll keep going.

See ya next year peeps, and be proud of yourselves too <3
"""


def day25_part2_main() -> int:
    return int("".join([str(ord(_)) for _ in "<3 GGs <3"]))


if __name__ == "__main__":
    print(day25_part2_main())