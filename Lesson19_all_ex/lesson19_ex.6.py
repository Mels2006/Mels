#  Tuple Exercise:
# Create a tuple of student names and their corresponding scores. Write a function to find
# the student with the highest score.
def find_highest_scorer(students):
    highest_scorer_name = ""
    highest_scorer_score = 0

    for name, score in students:
        if score > highest_scorer_score:
            highest_scorer_name = name
            highest_scorer_score = score

    return highest_scorer_name

scores = (("Alice", 90), ("Bob", 85), ("Charlie", 95), ("David", 88))

highest_scorer_name = find_highest_scorer(scores)

if highest_scorer_name:
    print(f"{highest_scorer_name}")





