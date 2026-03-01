"""
Topic: The Flashcard App (Task 1.10)

Scenario:
    Build a simple CLI flashcard tool. 
    1. A dictionary stores "Question": "Answer".
    2. Loop through and quiz the user.
    3. Use a set to track which questions the user gets wrong.

Requirements:
    - Use .items() to iterate.
    - Use input() to get user answers.
    - Track incorrect questions in a set.
    - Print the final list of "Needs Review" questions.
"""

# TODO: Create a dictionary of 3+ flashcards.
# TODO: Initialize an empty set for wrong answers.
# TODO: Quiz user, check answer, and add key to set if wrong.
# TODO: Print the final set of incorrect keys.


def ask_questions(flashcards: dict[str, str]) -> set[str]:
    """Use for loop to ask questions to user and record wrong answers and return them
    
    Args: 
        flashcards: set of questions and answers to ask the user
    
    Returns:
        set of all wrong answers with question number/id
    """
    wrong_answers: set[str] = set()
    for question, answer in flashcards.items(): 
        user_answer: str = input(f"{question}: ")
        if answer.lower() != user_answer.lower():
            print("Wrong Answer")
            wrong_answers.add(question)
        else:
            print("Correct Answer")
    return wrong_answers

def solutions() -> None:
    """Create a Q&A dict and wrong answer set. Then Ask user questions and record wrong answers. At the end print the incorrect questions"""
    flashcards: dict[str, str] = {
        "The pointer type used for heap-allocated memory": "Box",
        "Trait used for types that can be safely shared between threads": "Sync",
        "The keyword used to handle errors by returning them early": "question",
        "Rust's version of a 'catch-all' or 'default' match arm": "underscore",
        "The type of memory safety error prevented by the borrow checker": "Data-race",
        "Keyword to define a function that may be executed concurrently": "async",
        "The primitive type representing an empty tuple or no return": "unit",
        "A type that can be one of several variants": "enum",
        "Keyword used to bring a path into the current scope": "use",
        "The macro used to print text with a newline": "println",
    }
    wrong_answers = ask_questions(flashcards)
    print(wrong_answers)



if __name__ == "__main__":
    solutions()