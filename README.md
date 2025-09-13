# ETL Pipeline with Python

This project demonstrates a simple **Extract, Transform, Load (ETL)** process using Python and Pandas.  
The script (`etl_code.py`) extracts data from CSV, JSON, and XML files, transforms it into metric units, and loads the results into a CSV file.  
Progress is logged in a text file.

---

## 📦 Prerequisites

- Ubuntu / Debian-based system  
- Python **3.13**  
- `pip` for Python 3.13  
- `pandas` library  

---

<details>
  <summary><h2>1️⃣ Download and Extract Data</h2></summary>

  ```bash
  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip
  unzip source.zip

</details> <details> <summary><h2>2️⃣ Install Python 3.13 and pandas</h2></summary>

sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.13 -y

sudo python3.13 -m pip install pandas

</details> <details> <summary><h2>3️⃣ Run ETL Script</h2></summary>

# Run the ETL job
python3.13 etl_code.py

# Preview only first 5 lines of the output
python3.13 etl_code.py | head -5

</details>
