import json

def writeJSON(company, module1, module2, module3):
    # Read existing data from the file
    try:
        with open("sample.json", "r") as infile:
            data = json.load(infile)

            # Check if data is a dictionary, convert to list if needed
            if not isinstance(data, list):
                data = [data]
    except FileNotFoundError:
        # If the file doesn't exist yet, initialize data as an empty list
        data = []

    # Create a new dictionary for the current data
    new_data = {
        "company": company,
        "module 1": module1,
        "module 2": module2,
        "module 3": module3,
        "total": module1 + module2 + module3
    }

    # Append the new data to the existing data
    data.append(new_data)

    # Write the updated data back to the file
    with open("sample.json", "w") as outfile:
        json.dump(data, outfile, indent=2)

# Example usage:
# writeJSON("CompanyA", "ModuleA1", "ModuleA2", "ModuleA3")
