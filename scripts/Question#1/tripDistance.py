import sys
sys.path.append("/Users/skumar/Desktop/sample py")  # Adjust the path to your project directory
from functions.utils import * # Import necessary functions from the functions.utils module

# Check if the script is executed as the main program
if __name__ == "__main__":
    # Define the file path for reading/ writing the CSV data
    file_path = '/Users/skumar/Downloads/nyc_sample.csv'
    write_path = 'output/Question#1/out_tripDistance.csv'

    # Read and process the CSV data using the read_and_process_csv function
    # The calc_distance function is passed as an argument to perform the processing
    data = read_and_process_csv(file_path, calc_distance) 
    print("Data processed successfully.")

    # Define the headers for the output CSV file
    # The granularoty can be adjusted by adding more fields for the headers list
    # Example if you require date wise records then your row would looks as follows,
    #headers = ['date', 'hour', 'shortestDistance', 'longestDistance']

    headers = ['hour', 'shortestDistance', 'longestDistance']

    # Initialize an empty list to store the rows of the output CSV file
    rows = []

    # Iterate through the processed data, sorted by date and hour
    for (hour), distances in sorted(data.items()):
        # Calculate the shortest and longest distances for each date and hour
        shortest_distance = min(distances)
        longest_distance = max(distances)

        # Create a dictionary representing a row of the output CSV file
        # Adjust the keys based on the headers list 
        # Example if you require date wise records then your row would looks as follows,
        """
        row = {
            'date': date,
            'hour': hour,
            'shortestDistance': shortest_distance,
            'longestDistance': longest_distance
        }
        """
        row = {
            'hour': hour,
            'shortestDistance': shortest_distance,
            'longestDistance': longest_distance
        }

        # Append the row to the list of rows
        rows.append(row)

    # Write the processed data to the output CSV file using the write_data function
    write_data(write_path, headers, rows)
