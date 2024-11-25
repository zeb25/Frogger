import csv
HIGH_SCORES = "highscores.csv"


def read_highscores():
    """Reads highscores from csv file.

    This function attempts to open and read the CSV file containing the high scores.
    If the file exists, it will parse the scores and return them as a list of integers.
    If the file is empty, it returns an empty list. If the file doesn't exist, it catches
    the FileNotFoundError and returns an empty list.
    """
    try:
        # Open the CSV file in read mode
        with open(HIGH_SCORES, mode="r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)  # Convert the CSV rows into a list
            if not rows:  # If the file is empty, return an empty list
                return []
            # Convert the scores from string to integer and return them
            return [int(row[0]) for row in rows]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []


def update_highscores(new_score):
    """Updates the highscores file with a new score.

    This function reads the current high scores, adds a new score to the list,
    sorts the scores in descending order (highest score first), and then saves
    the top scores back to the CSV file. It overwrites the entire file with
    the sorted top scores.
    """
    scores = read_highscores()  # Read the current high scores from the file
    scores.append(new_score)  # Add the new score to the list of scores
    scores = sorted(scores, reverse=True)  # Sort the scores in descending order (highest first)

    # Open the CSV file in write mode to overwrite with the updated scores
    with open(HIGH_SCORES, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write each score back into the CSV file
        for score in scores:
            writer.writerow([score])


def get_top_highscores():
    """Get the top 3 high scores.

    This function reads the high scores from the CSV file, sorts them in descending order,
    and returns the top 3 highest scores. If there are fewer than 3 scores, it will return
    whatever is available. If the file is empty, it returns an empty list.
    """
    scores = read_highscores()  # Read the current high scores from the file
    if not scores:  # If there are no scores, return an empty list
        return []
    else:
        # Sort the scores in descending order and return the top 3
        return sorted(scores, reverse=True)[:3]
