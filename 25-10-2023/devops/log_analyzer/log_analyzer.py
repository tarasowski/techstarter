# log_analyzer.py

# Step 1: Open and read the log file
log_path = "app_logs.log"

with open(log_path, "r") as log_file:
    log_entries = log_file.readlines()

# Initialize variables for log analysis
total_entries = len(log_entries)
info_count = 0
error_count = 0
warning_count = 0

# Step 2: Find and display the most recent log entry
most_recent_entry = log_entries[-1]

# Step 3: Analyze log entries
for entry in log_entries:
    if "ERROR" in entry:
        error_count += 1
    elif "WARNING" in entry:
        warning_count += 1
    elif "INFO" in entry:
        info_count += 1

# Step 4: Display log analysis results
print("Total log entries:", total_entries)
print("INFO entries:", info_count)
print("ERROR entries:", error_count)
print("WARNING entries:", warning_count)
print("\nMost recent log entry:")
print(most_recent_entry)
