# All the function for the example person.py
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person.
       This function takes in simple textual information and puts it into a more meaningful
       data structure that lets you work with the information beyond just printing it. """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
