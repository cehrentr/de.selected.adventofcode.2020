import re

class AdventOfCodePuzzleDay04:
    """
    --- Day 4: Passport Processing ---
    You arrive at the airport only to realize that you grabbed your North Pole
    Credentials instead of your passport. While these documents are extremely
    similar, North Pole Credentials aren't issued by a country and therefore
    aren't actually valid documentation for travel in most of the world.

    It seems like you're not the only one having problems, though; a very long
    line has formed for the automatic passport scanners, and the delay could
    upset your travel itinerary.

    Due to some questionable network security, you realize you might be able to
    solve both of these problems at the same time.

    The automatic passport scanners are slow because they're having trouble detecting
    which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

    Passport data is validated in batch files (your puzzle input). Each passport
    is represented as a sequence of key:value pairs separated by spaces or newlines.
    Passports are separated by blank lines.

    Here is an example batch file containing four passports:

        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in

    The first passport is valid - all eight fields are present. The second passport
    is invalid - it is missing hgt (the Height field).

    The third passport is interesting; the only missing field is cid, so it looks
    like data from North Pole Credentials, not a passport at all! Surely, nobody
    would mind if you made the system temporarily ignore missing cid fields. Treat
    this "passport" as valid.

    The fourth passport is missing two fields, cid and byr. Missing cid is fine, but
    missing any other field is not, so this passport is invalid.

    According to the above rules, your improved system would report 2 valid passports.

    Count the number of valid passports - those that have all required fields. Treat
    cid as optional. In your batch file, how many passports are valid?
    """

    REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    FIELD_VALIDATORS = None

    def __init__(self, puzzle_input: str):
        self.passports = puzzle_input.replace("\n", " ").split("  ")
        self.FIELD_VALIDATORS = {
            "byr": self.__is_valid_birth_year,
            "iyr": self.__is_valid_issue_year,
            "eyr": self.__is_valid_expiration_year,
            "hgt": self.__is_valid_height,
            "hcl": self.__is_valid_hair_color,
            "ecl": self.__is_valid_eye_color,
            "pid": self.__is_valid_passport_id,
        }

    def solve_puzzle_1(self) -> int:
        result = 0

        for passport in self.passports:
            if self.__is_valid_passport(passport=passport):
                result += 1

        return result

    def solve_puzzle_2(self) -> int:
        result = 0

        for passport in self.passports:
            valid_passport = self.__is_valid_passport(passport=passport)

            valid_fields = True
            for field in self.__get_provided_fields(passport=passport):

                if field and field[:3] != "cid":
                    valid_field = self.__is_valid_field(field=field)
                    valid_fields = valid_fields and valid_field

            if valid_passport and valid_fields:
                result += 1

        return result

    def __is_valid_passport(self, passport: str) -> bool:
        provided_keys = self.__get_provided_keys(passport=passport)
        missing_fields = list(self.REQUIRED_KEYS - set(provided_keys))

        return not missing_fields

    def __is_valid_field(self, field: str) -> bool:
        key, value = field.split(":")
        # print(f"key={key}, value={value}")

        return self.FIELD_VALIDATORS[key](value)

    @staticmethod
    def __is_valid_birth_year(byr: str) -> bool:
        return len(byr) == 4 and (1920 <= int(byr) <= 2002)

    @staticmethod
    def __is_valid_issue_year(iyr: str) -> bool:
        return len(iyr) == 4 and (2010 <= int(iyr) <= 2020)

    @staticmethod
    def __is_valid_expiration_year(eyr: str) -> bool:
        return len(eyr) == 4 and (2020 <= int(eyr) <= 2030)

    @staticmethod
    def __is_valid_height(hgt: str) -> bool:
        measure = hgt[-2:]

        if measure not in ["cm", "in"]:
            return False

        height = int(hgt[:-2])
        rule = {
            "cm": {"min": 150, "max": 193},
            "in": {"min": 59, "max": 76}
        }

        return rule[measure]["min"] <= height <= rule[measure]["max"]

    @staticmethod
    def __is_valid_hair_color(hcl: str) -> bool:
        return bool(re.match(r"#[0-9a-f]{6}", hcl))

    @staticmethod
    def __is_valid_eye_color(ecl: str) -> bool:
        return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    @staticmethod
    def __is_valid_passport_id(pid: str) -> bool:
        return len(pid) == 9

    @staticmethod
    def __get_provided_keys(passport: str) -> list:
        return [pp.split(":")[0] for pp in passport.split(" ")]

    @staticmethod
    def __get_provided_fields(passport: str) -> list:
        return passport.split(" ")
