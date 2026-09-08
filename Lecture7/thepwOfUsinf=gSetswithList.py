attendance_week = [
    {"Alice", "Bob", "Charlie","David"},
    {"Alice", "Charlie", "David"},
    {"Alice", "Bob", "David"},
    {"Alice", "David", "Eve"},
    {"Bob", "Charlie", "David"}
]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

attendance_set = [
    {"Alice", "Bob", "Charlie"},
    {"Alice", "David", "Charlie"},
    {"Bob", "David", "Eve"},
]