import random

# Dictionary of story templates with blanks
story_templates = {
    "1": "One [adjective] day, a [noun] [verb] [adverb] across the [place].",
    "2": "The [adjective] [noun] [verb] [adverb] while [verb] through the [place].",
    "3": "In the [adjective] [place], there was a [noun] who [verb] [adverb] every day."
}

# Dictionary of word types
word_types = {
    "adjective": ["red", "happy", "quick", "beautiful"],
    "noun": ["cat", "dog", "car", "tree"],
    "verb": ["ran", "jumped", "slept", "laughed"],
    "adverb": ["quickly", "happily", "slowly", "loudly"],
    "place": ["park", "forest", "city", "beach"]
}

def get_word(word_type):
    """
    Get a random word of given type.
    """
    return random.choice(word_types[word_type])

def generate_story(story_template):
    """ 
    Generate a Mad Libs story based on the selected template.
    """
    story = story_templates[story_template]
    words = {}

    for word_type in word_types:
        valid_input = False
        while not valid_input:
            word = input(f"Enter a {word_type}: ")
            if word not in word_types[word_type]:
                print(f"Invalid {word_type}: '{word}'. Please enter a valid {word_type}.")
                print()
            else:
                words[word_type] = word
                valid_input = True

    # Replace blanks with user input
    for word_type, word in words.items():
        story = story.replace(f"[{word_type}]", word)

    return story

def main():
    while True:
        print("\n========================== Welcome to MAD_LIBS Game ===========================\n")

        print("Choose a story template : ")

        for key, value in story_templates.items():
            print(f"{key}: {value}")

        print()    

        story_choice = input("Choose a story (1 or 2 or 3) : ")

        print()

        if story_choice not in story_templates:
            print("Invalid story choice, Please enter a valid story template.")
            return

        final_story = generate_story(story_choice)

        print("\nHere's your Mad Libs story:\n" + final_story)

        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() != 'y':
           print("Thanks for playing Mad Libs! Goodbye!")
           break

if __name__ == "__main__":
    main()
