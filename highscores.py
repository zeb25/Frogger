import csv
HIGH_SCORES = "highscores.csv"


def read_highscores():
    """Reads highscores from csv file"""
    try:
        with open(HIGH_SCORES, mode="r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            if not rows:
                return []
            return [int(row[0]) for row in rows]
    except FileNotFoundError:
        return []


def update_highscores(new_score):
    """Updates highscores file"""
    scores = read_highscores()
    scores.append(new_score)
    scores = sorted(scores, reverse=True)
    with open(HIGH_SCORES, mode="w", newline="") as file:
        writer = csv.writer(file)
        for score in scores:
            writer.writerow([score])


def get_top_highscores():
    """Get the top 3 high scores"""
    scores = read_highscores()
    if not scores:
        return []
    else:
        return sorted(scores, reverse=True)[:3]
