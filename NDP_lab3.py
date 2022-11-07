def create_phonebook():
    """
    Function to create an empty dictionary
    """

    phonebook = dict()
    return phonebook

def add_new_number(phonebook, name, number):
    """
    Function to add a new number to the
    dictionary

    :param phonebook: dictionary with numbers
    :param name: new name to be added
    :param number: new number to be added
    """
    if name in phonebook:
        tmp = phonebook[name]
        tmp.append(number)
        phonebook[name] = tmp
        #print("Contact updated")
    else:
        phonebook[name] = [number]
        #print("New contact added")

def get_numbers(phonebook, name):
    """
    Function to get all numbers for 
    the given name in the phonebook

    :param phonebook: dictionary with numbers
    :param name: name of a person whose number is wanted
    """
    return ", ".join(phonebook[name])

def delete_number(phonebook, name, number):
    """
    Function to delete a number from the phonebook

    :param phonebook: dictionary with numbers
    :param name: a person's name whose number is about to be deleted
    "param number: number to be delated
    """
    if name in phonebook:
        if number in phonebook[name]:
            phonebook[name].remove(number)
            print("Number {} for {} deleted".format(number, name))
        else:
            print("Number {} does not exist for {}".format(number, name))
        if len(phonebook[name]) == 0:
            del phonebook[name]
            print("No number for {}. Deleting the contact".format(name))
    else:
        print("No contact under the given name {}".format(name))

def print_phonebook(phonebook):
    """
    Function to get all numbers in the phonebook

    :param phonebook: dictionary with numbers
    """
    for name in phonebook:
        numbers = ", ".join(phonebook[name])
        print(name+": "+numbers)

def main():
    phonebook = create_phonebook()
    add_new_number(phonebook, "Ala Wesołowska", "+048 513 056 121")
    add_new_number(phonebook, "Ala Wesołowska", "22-848-34-21")
    add_new_number(phonebook, "John Smith", "469-452-199")
    add_new_number(phonebook, "John Smith", "0800 241 6331")
    add_new_number(phonebook, "Susan Brown", "315-728-3639")
    print_phonebook(phonebook)
    print(get_numbers(phonebook, "Ala Wesołowska"))
    delete_number(phonebook, "Ala Wesołowska", "+048 513 056 121")
    print(get_numbers(phonebook, "Ala Wesołowska"))
    delete_number(phonebook, "Testowy kontakt", "0000")
    delete_number(phonebook, "Ala Wesołowska", "22-848-34-21")
    print_phonebook(phonebook)
    add_new_number(phonebook, "Ala Wesołowska", "+048 513 056 121")
    print(get_numbers(phonebook, "Ala Wesołowska"))
    print_phonebook(phonebook)


if __name__ == "__main__":
    main()