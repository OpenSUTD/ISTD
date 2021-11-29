from collections import Counter

import pandas as pd


def read_csv(filename: str) -> list:
    """
    Reads an Excel file and returns a list of rows.
    """
    df = pd.read_csv(filename)
    header = df.columns.tolist()
    data = df.values.tolist()
    data.insert(0, header)
    return data


def parse_votes(data: list) -> list:
    """
    Parses the data from the list of rows.
    """
    header = data.pop(0)
    vote_1_idx = header.index("Your Favorite Design")
    vote_2_idx = header.index("Your Second-favorite Design")
    vote_3_idx = header.index("Your Third-favorite Design")

    vote_1_counter = Counter([i[vote_1_idx] for i in data])
    vote_2_counter = Counter([i[vote_2_idx] for i in data])
    vote_3_counter = Counter([i[vote_3_idx] for i in data])

    result = dict()

    for i in vote_1_counter.most_common():
        result[i[0]] = result.get(i[0], 0) + i[1] * 2
    for i in vote_2_counter.most_common():
        result[i[0]] = result.get(i[0], 0) + i[1] * 1.5
    for i in vote_3_counter.most_common():
        result[i[0]] = result.get(i[0], 0) + i[1] * 1

    return result


def print_ranking(result: dict):
    for i in sorted(result.keys(), key=lambda x: result[x], reverse=True)[:10]:
        print(f"{i}: {result[i]}")


def main():
    filename = "voting_data.csv"
    data = read_csv(filename)
    result = parse_votes(data)
    print_ranking(result)

    # x = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0}
    # for i in result.keys():
    #     x[i[0]] += result[i]
    # print(x)


if __name__ == "__main__":
    main()
