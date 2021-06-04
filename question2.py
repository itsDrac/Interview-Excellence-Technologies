
def main():
    users = {
            "1": "name1",
            "2": "name2",
            "3": "name3",
            }
    score = {
            "1": 50,
            "5": 60,
            "3": 30
            }
    print(max_score(users, score))


def max_score(users, score):
    ids = list(score.keys())
    markes = list(score.values())
    max_value = max(markes)
    indx = markes.index(max_value)
    return { ids[indx]: max_value }

if __name__ == '__main__':
    main()
