# Meraki-Api-Data-Retrieval
This project is a Python application that demonstrates how to use both the Python requests module and the Python Meraki module to access the Cisco Meraki API and retrieve information about administrators and inventory devices. The retrieved data is then saved into separate text files.

Table of Contents

    Requirements
    Usage
    Project Structure

Requirements

To run this project, you'll need:

    Python 3.x
    requests library (used for making HTTP requests, install it using pip install requests)
    meraki library (used for interacting with the Meraki API, install it using pip install meraki)
    A Cisco Meraki API key with the necessary permissions to access administrators and inventory devices within your organization.

Usage

    Clone the repository to your local machine using the following command:


git clone https://github.com/yourusername/meraki-api-retrieval.git

Navigate to the project directory:


cd meraki-api-retrieval

Replace the placeholders in the code (api_key and org_id) with your Meraki API key and organization ID.

Execute the script to retrieve data using the requests module:


python requests_module.py

    The script will access the Meraki API to retrieve data about administrators and inventory devices.
    The retrieved data is saved into PythonRequestModule.txt.

Execute the script to retrieve data using the Meraki module:

    python meraki_module.py

        This script uses the Meraki module to retrieve the same data.
        The retrieved data is saved into MerakiRequestModule.txt.

Project Structure

The project has the following structure:

    requests_module.py: This Python script uses the requests module to access the Meraki API and retrieve data.
    meraki_module.py: This Python script uses the meraki module to access the Meraki API and retrieve data.
    PythonRequestModule.txt: A text file that stores data retrieved using the requests module.
    MerakiRequestModule.txt: A text file that stores data retrieved using the Meraki module.
