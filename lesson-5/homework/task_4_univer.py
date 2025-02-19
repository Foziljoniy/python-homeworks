import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    """Returns two lists: student enrollments and tuition fees."""
    enrollments = [univ[1] for univ in universities]
    tuitions = [univ[2] for univ in universities]
    return enrollments, tuitions

def mean(data):
    """Returns the mean of a list of numbers."""
    return sum(data) / len(data)

def median(data):
    """Returns the median of a list of numbers."""
    return statistics.median(data)

enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean(enrollments):,.2f}")
print(f"Student median: {median(enrollments):,}\n")
print(f"Tuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,}")