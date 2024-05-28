# Instructions for Executing the Python Script

These instructions will guide you through the process of executing the Python script in your environment.

## Prerequisites

Before running the script, ensure that you have the following installed:

- Python 3.x
- Required dependencies (specified in requirements.txt)

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/SubhamBhagat/python.git

2. Navigate to the project directory:
cd your-repository


3. Install the dependencies using pip:
pip install -r requirements.txt

## About the Dataset

- This is an open dataset and can be found at: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- The purpose of the project is to utilize python standard libraries and perform transformation as required
- Thus, the core python scrips are only meant to transform once the data is in place (such as a local storage in CSV format)
- With respect to the extraction, it is not in the scope of this document
- The extraction was made using Databricks via azureml.opendatasets. Refer here for more details: [azureml.opendatasets](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-taxi-yellow?tabs=azureml-opendatasets#azure-databricks)

## Usage

1. Open a terminal or command prompt.

2. Navigate to the project directory:
cd zeiss-assignment

3. Execute the Python script:
python script_name.py

## Testing

1. Open a terminal or command prompt.
   
2. Navigate to the project directory:
cd zeiss-assignment

3. Execute the Python script:
python script_name.py
- This will be followed by an input prompt 'Enter the path to the CSV file:'
- Consider you want to test your output under the directory output/
- Provide the CSV path as follows in the command line:  output/Question#2/out_amountPaid.csv

## Results

1. The output dataset relies heavily on the cleanzed inputs. There are cases where the are no passenger in the input dataset and yet the values for totalAmount is observed.

2. There are also cases where there is a negative amount and negative tripDistance covered.

3. These are few of the outliers identified and removed during the analysis

4. To enrich the resultset further, one can eliminate the extreme outliers and try to scope the input dataset within an interval range
- Example: Extract only the records that have a min tripDistance of 0.5 miles and have a tripDuration of at least 3 minutes or greater.
- Note: trip_duration_minutes can be calculated using round("tpepDropoffDateTime"-"tpepPickupDateTime",2)/60)


## Configuration

- Modify the script as needed to customize its behavior.
- Adjust the file paths, input parameters, or function calls according to your requirements.

## Additional Information

- For more details on the script's functionality, refer to the script's source code and comments.
- If you encounter any issues or have questions, feel free to open an issue in the repository.
