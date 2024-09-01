def sort_by_age(tuples_list):
    tuples_list.sort(key=get_age)
    return tuples_list

def get_age(person_tuple):
    return person_tuple[1]

people = [('Rose', 30), ('Sera', 25), ('John', 35), ('Thiga', 28)]

sorted_people = sort_by_age(people)

print("Sorted by age:", sorted_people)
