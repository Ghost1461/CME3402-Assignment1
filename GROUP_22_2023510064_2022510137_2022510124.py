import csv
import math
import tkinter as tk
from tkinter import messagebox

CSV_FILE = "diabetes.csv"
PREPROCESSED_FILE = "diabetes_preprocessed.csv"

columns = []
data = []
mins = []
maxs = []
preprocessed_data = []


# Read diabetes.csv
with open(CSV_FILE, "r") as file:
    reader = csv.reader(file)

    columns = next(reader)

    for row in reader:
        numeric_row = []

        for value in row:
            numeric_row.append(float(value))

        data.append(numeric_row)


# Find min and max values
column_count = len(data[0])

for i in range(column_count):
    column_values = []

    for row in data:
        column_values.append(row[i])

    mins.append(min(column_values))
    maxs.append(max(column_values))


print("MIN VALUES:")
for i in range(column_count):
    print(columns[i], "=", mins[i])

print("\nMAX VALUES:")
for i in range(column_count):
    print(columns[i], "=", maxs[i])


# Preprocess dataset
for row in data:
    new_row = []

    for i in range(column_count):
        normalized_value = (row[i] - mins[i]) / (maxs[i] - mins[i])
        new_row.append(normalized_value)

    preprocessed_data.append(new_row)


# Save preprocessed dataset
with open(PREPROCESSED_FILE, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(columns)
    writer.writerows(preprocessed_data)

print("\nPreprocessed dataset created successfully.")
print("Created file:", PREPROCESSED_FILE)


def calculate():
    input_values = []

    # Check 8 patient inputs
    for i in range(8):
        value = entries[i].get().strip()

        if value == "":
            messagebox.showerror("Input Error", "All 8 patient fields must be filled.")
            return

        try:
            value = float(value)
        except ValueError:
            messagebox.showerror("Input Error", f"{columns[i]} must be a number.")
            return

        if value < mins[i] or value > maxs[i]:
            messagebox.showerror(
                "Range Error",
                f"{columns[i]} must be between {mins[i]} and {maxs[i]}."
            )
            return

        input_values.append(value)

    # Check k value
    k_value = k_entry.get().strip()

    if k_value == "":
        messagebox.showerror("Input Error", "Closest record count must be filled.")
        return

    try:
        k = int(k_value)
    except ValueError:
        messagebox.showerror("Input Error", "Closest record count must be an integer.")
        return

    if k < 1 or k > len(data):
        messagebox.showerror(
            "Range Error",
            f"Closest record count must be between 1 and {len(data)}."
        )
        return

    # Normalize user input
    normalized_inputs = []

    for i in range(8):
        normalized_value = (input_values[i] - mins[i]) / (maxs[i] - mins[i])
        normalized_inputs.append(normalized_value)

    print("\nNORMALIZED USER INPUT VALUES:")
    for i in range(8):
        print(columns[i], "=", normalized_inputs[i])

    # Calculate Euclidean Distance
    distances = []

    for row_index, row in enumerate(preprocessed_data):
        total = 0

        for i in range(8):
            total += (normalized_inputs[i] - row[i]) ** 2

        distance = math.sqrt(total)
        outcome = int(row[8])

        # row_index + 2 because CSV row 1 is header
        csv_row_number = row_index + 2

        distances.append((distance, outcome, csv_row_number))

    # Sort distances from smallest to largest
    distances.sort(key=lambda x: x[0])

    # Get closest k records
    closest_records = distances[:k]

    print("\nCLOSEST RECORDS:")
    for index, record in enumerate(closest_records, start=1):
        print(
            f"{index}. CSV Row = {record[2]}, "
            f"Distance = {record[0]:.6f}, "
            f"Outcome = {record[1]}"
        )

    # Calculate probability
    diabetic_count = 0

    for record in closest_records:
        diabetic_count += record[1]

    probability = (diabetic_count / k) * 100

    print("\nRESULT:")
    print("Closest Records:", k)
    print("Diabetic Records:", diabetic_count)
    print(f"Diabetes Probability: {probability:.2f}%")

    result_label.config(
        text=f"Closest Records: {k}\n"
             f"Diabetic Records: {diabetic_count}\n"
             f"Diabetes Probability: {probability:.2f}%"
    )


# Create GUI
root = tk.Tk()
root.title("Diabetes Probability Checker")
root.geometry("500x560")

title_label = tk.Label(
    root,
    text="Diabetes Probability Checker",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

entries = []

for i in range(8):
    frame = tk.Frame(root)
    frame.pack(pady=5)

    label = tk.Label(frame, text=columns[i], width=28, anchor="w")
    label.pack(side=tk.LEFT)

    entry = tk.Entry(frame, width=22)
    entry.pack(side=tk.LEFT)

    entries.append(entry)

k_frame = tk.Frame(root)
k_frame.pack(pady=10)

k_label = tk.Label(k_frame, text="Closest Record Count (k)", width=28, anchor="w")
k_label.pack(side=tk.LEFT)

k_entry = tk.Entry(k_frame, width=22)
k_entry.pack(side=tk.LEFT)
k_entry.insert(0, "5")

calculate_button = tk.Button(
    root,
    text="Calculate Diabetes Probability",
    command=calculate
)
calculate_button.pack(pady=15)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    justify="center"
)
result_label.pack(pady=10)

root.mainloop()