"""
AWS SSM Parameter Retrieval Script

This script allows you to retrieve parameter values from AWS Systems Manager Parameter Store (SSM) and optionally decrypt them.

Usage:
  python ssm_parameter_retrieval.py --parameter <parameter_name> [--decrypt <True/False>]

Options:
  --parameter <parameter_name>  Name of the parameter to retrieve from AWS SSM (required).
  --decrypt <True/False>        Specify 'True' to attempt decryption of the parameter value (optional).
"""

import boto3
import argparse

# Create an AWS SSM client
ssm = boto3.client('ssm')

# Initialize the argument parser
parser = argparse.ArgumentParser()

# Define command-line arguments
parser.add_argument("--parameter", type=str, required=True,
                    help="Name of the parameter to retrieve from AWS SSM")
parser.add_argument("--decrypt", type=str, required=False,
                    help="Specify 'True' to attempt decryption of the parameter value")

# Parse the command-line arguments
args = parser.parse_args()

# Function to get an SSM parameter
def get_parameter(name, decrypt):
    # Convert the 'decrypt' flag to a boolean
    if decrypt == 'True':
        decrypt = True
    else:
        decrypt = False
    # Retrieve the parameter from AWS SSM
    parameter = ssm.get_parameter(Name=name, WithDecryption=decrypt)
    return parameter['Parameter']['Value']

# Main function
def main():
    # Extract the parameter and decrypt values from command-line arguments
    parameter_name = args.parameter
    decrypt = args.decrypt
    # Call the get_parameter function to retrieve the specified parameter
    parameter = get_parameter(parameter_name, decrypt)
    # Print the result with a prefix for identification
    print("@@Result=" + str(parameter))

# Check if the script is being run as the main program
if __name__ == '__main__':
    main()
