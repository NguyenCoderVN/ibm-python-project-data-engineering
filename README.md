<details>
  <summary><h2>Install Python 3.13 and pandas</h2></summary>

  ```bash
  echo "Updating package lists and installing Python 3.13..."
  sudo apt update
  sudo apt install software-properties-common -y
  sudo add-apt-repository ppa:deadsnakes/ppa -y
  sudo apt update
  sudo apt install python3.13 -y

  echo "Installing pandas library for Python 3.13..."
  sudo python3.13 -m pip install pandas
</details>


# 1-ETL Example
```bash
# --- 1. Download and Extract Data ---
echo "Downloading and extracting source data..."
wget [https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip)
unzip source.zip

  
