import csv
import re
import json

def load_log_file(file_path):
    """Load the log file into memory."""
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_log_line(line):
    """Parse a single line of the log file."""
    log_pattern = re.compile(r'(?P<timestamp>\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}:\d{2} [APM]{2}): (?P<message>.+)')
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

def extract_json_from_message(message):
    """Extract JSON data from the log message if present."""
    try:
        json_part = re.search(r'POST DATA: ({.*})', message)
        if json_part:
            json_data = json.loads(json_part.group(1))
            return json.dumps(json_data)  # Return as a string or modify as needed
    except json.JSONDecodeError:
        pass
    return message

def convert_log_to_csv(log_file_path, csv_file_path):
    """Convert a log file to a CSV file."""
    log_data = load_log_file(log_file_path)
    
    # Parse each line in the log file
    parsed_data = [parse_log_line(line) for line in log_data]
    
    # Filter out None entries (lines that didn't match the log pattern)
    parsed_data = [entry for entry in parsed_data if entry]
    
    # Extract JSON data from messages if present
    for entry in parsed_data:
        entry['message'] = extract_json_from_message(entry['message'])
    
    # Define CSV column names (based on the log pattern)
    fieldnames = ['timestamp', 'message']
    
    # Write to CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(parsed_data)

# Example usage
log_file_path = '/Users/adivikra/OpenDNSAuditClient.log'
csv_file_path = 'output.csv'
convert_log_to_csv(log_file_path, csv_file_path)
