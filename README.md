# 1-ETL
## --- 1. Download and Extract Data ---
echo "Downloading and extracting source data..."
wget [https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip)
unzip source.zip

## --- 2. Install Python 3.13 ---
echo "Updating package lists and installing Python 3.13..."
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.13 -y

## --- 3. Install Required Libraries ---
echo "Installing pandas library for Python 3.13..."
sudo python3.13 -m pip install pandas

## --- 4. Run the Code ---
echo "Running the ETL script and showing the first 5 lines of output..."
python3.13 etl_code.py | head -5

echo "Script finished."
