checklist = []
completed_tasks = []
incomplete_tasks = []

print("===== Daily Checklist =====")

while True:
    task = input("Enter a task: ")
    checklist.append(task)

    choice = input("Do you want to add another task? (yes/no): ").lower()

    if choice == "no":
        break

print("\n===== End of the Day Review =====")

for task in checklist:
    status = input(f"Did you complete '{task}'? (yes/no): ").lower()

    if status == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)


print("\n========== Daily Report ==========")

print("\nChecklist:")
for task in checklist:
    print("-", task)

print("\nCompleted Tasks:")
if completed_tasks:
    for task in completed_tasks:
        print("✓", task)
else:
    print("No completed tasks.")

print("\nIncomplete Tasks:")
if incomplete_tasks:
    for task in incomplete_tasks:
        print("✗", task)
else:
    print("No incomplete tasks.")

print("\nThank you! Have a productive tomorrow!")