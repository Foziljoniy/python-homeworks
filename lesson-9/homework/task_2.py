import csv
from collections import defaultdict

def read_grades(filename):
    """Reads the grades from a CSV file and returns a list of dictionaries."""
    grades = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average(grades):
    """Calculates the average grade for each subject."""
    subject_totals = defaultdict(list)
    
    for entry in grades:
        subject_totals[entry['Subject']].append(entry['Grade'])
    
    subject_averages = {subject: sum(grades) / len(grades) for subject, grades in subject_totals.items()}
    return subject_averages

def write_averages(filename, averages):
    """Writes the subject averages to a new CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 1)])

# Main program
grades_file = 'grades.csv'
average_file = 'average_grades.csv'

grades = read_grades(grades_file)
subject_averages = calculate_average(grades)
write_averages(average_file, subject_averages)

print(f"Averages written to {average_file}")
