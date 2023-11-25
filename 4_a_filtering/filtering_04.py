import pandas as pd

from filtering import country_migration


def filter_net_per_10k(df, amount):
    result = df[df['net_per_10K_2019'] < amount]
    return result['net_per_10K_2019'].count()


tests = [
    {"id": 1, "actual": filter_net_per_10k(country_migration, 100), "expected": 4148},
    {"id": 2, "actual": filter_net_per_10k(country_migration, 0), "expected": 1980},
    {"id": 3, "actual": filter_net_per_10k(country_migration, -100), "expected": 0}
]

for test in tests:
    if test["actual"] == test["expected"]:
        print("Test {} passed!\nExpected: {}\nActual: {}\n".format(test["id"], test["expected"], test["actual"]))
    else:
        print("Test {} failed!\nExpected: {}\nActual: {}\n".format(test["id"], test["expected"], test["actual"]))
