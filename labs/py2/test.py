student_joe = {'gpa': 3.7, 'major':'physics', 'name':'Joe Smit'}
student_jane = {'gpa': 3.8, 'major':'chemistry', 'name':'Jane Jones'}
student_zoe = {'gpa': 3.6, 'major':'literature', 'name':'Zoe Grimwald'}

students = [student_joe, student_jane, student_zoe]


def max_by_gpa(items):
    biggest = items[0]
    for item in items[1:]:
        if item['gpa'] > biggest['gpa']:
            biggest = item

    return biggest

def get_gpa(item):
    return item['gpa']

# print(sorted(students, key=get_gpa))
from operator import itemgetter
print(sorted(students, key=itemgetter('gpa')))
