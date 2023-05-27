# ECI-Webscrapping
The repository uses Automation to extract the voter information for each District and Assembly Constituency for the state of Maharashtra. 

This Python-based web scraping project allows you to the voter information for each District and Assembly Constituency for the state of Maharashtra. 
It consists of two parts: 
    a) Automating the part of District and Assembly Constituency selection.
    b) Downloading the PDFs for voter information for each Assembly Constituency.
## Features

The automation script takes district name as input from user and then uses Selenium to automate the process of selecting the District and Assembly Constituency. The script then downloads the PDFs for each Assembly Constituency and stores them in a folder named "PDFs" in the same directory. 

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You will also need the following packages:

- requests
- BeautifulSoup
- pandas
- selenium

You can install the required packages by running the following command:
pip install -r requirements.txt

### Running the Script

1. Clone the repository
2. Navigate to the project directory
3. Run the script


The script will ask for the input from the user after that the PDF containing voter list information will be downloaded in a Folder named 'PDFs' from 'https://ceoelection.maharashtra.gov.in/searchlist/'.

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to submit a pull request.

## Contact

For any questions or inquiries, please contact shahilpatel809@gmail.com.
