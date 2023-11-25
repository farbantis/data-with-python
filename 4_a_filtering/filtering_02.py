from filtering import skill_migration


def filter_skills(df, skill):
    df = df[df['skill_group_category'] == skill]
    return df['country_name'].mode()


tests = [
    {"id": 1, "actual": filter_skills(skill_migration, "Tech Skills")[0], "expected": "Australia"},
    {"id": 2, "actual": filter_skills(skill_migration, "Business Skills")[0], "expected": "Australia"},
    {"id": 3, "actual": filter_skills(skill_migration, "Specialized Industry Skills")[0], "expected": "United Kingdom"}
]

for test in tests:
    if test["actual"] == test["expected"]:
        print("Test {} passed!\nExpected: {}\nActual: {}\n".format(test["id"], test["expected"], test["actual"]))
    else:
        print("Test {} failed!\nExpected: {}\nActual: {}\n".format(test["id"], test["expected"], test["actual"]))


