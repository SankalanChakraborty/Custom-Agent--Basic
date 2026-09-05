import json


def create_note(note):
    try:
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
            return json.dumps({
            "message": "Note created successfully.", "note": note
            })
    except Exception as e:
        print(f"An error occurred while creating the note: {e}")
        return json.dumps({
            "message": "An error occurred while creating the note.", "error": str(e)
        })

# invoke the function
# create_note("I need to buy groceries tomorrow.")
# create_note("Remember to call the dentist for an appointment.")
# create_note("Finish reading the book by the end of the week.")