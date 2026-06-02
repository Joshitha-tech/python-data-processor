
""" PROJECT: Automated Python Data Processor
 DESCRIPTION: Cleans messy string records,
              handles missing data dynamically,
             and exports a structural text report."""


students_list = []


with open("raw_grades.txt", "r") as file:
    for line in file:
        if not line.strip():
            continue  # Skip any blank lines
        
        # Break line into distinct key-value segments
        parts = line.strip().split(", ")
        student_data = {}
        
        for part in parts:
            key, value = part.split(":")
            student_data[key] = value
        
        # 2. Data Cleaning: Check for missing/corrupt values
        for subject in ["Math", "Physics", "Coding"]:
            val = student_data[subject]
            if val.isdigit():
                student_data[subject] = int(val)
            else:
                student_data[subject] = 0  # Safe default substitution for "NA" or "missing"
        
        # 3. Analytics & Computations
        total = student_data["Math"] + student_data["Physics"] + student_data["Coding"]
        average = round(total / 3, 2)
        
        student_data["Total"] = total
        student_data["Average"] = average
        student_data["Status"] = "Passed" if average >= 50 else "Failed"
        
        students_list.append(student_data)

# 4. Generate the structured executive report
with open("performance_report.txt", "w") as out_file:
    out_file.write("==================================================\n")
    out_file.write("           ACADEMIC PERFORMANCE REPORT            \n")
    out_file.write("==================================================\n\n")
    
    for s in students_list:
        out_file.write(f"Roll No: {s['Roll_No']} | Name: {s['Name']}\n")
        out_file.write(f"Scores  -> Math: {s['Math']}, Physics: {s['Physics']}, Coding: {s['Coding']}\n")
        out_file.write(f"Result  -> Total: {s['Total']} | Avg: {s['Average']}% | Status: {s['Status']}\n")
        out_file.write("-" * 50 + "\n")

print("Success! 'performance_report.txt' has been compiled successfully.")
