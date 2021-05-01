# Common Utilities
## 1. Covid Vaccination slot checker
### **File:** check.py
### **Requires:** Python (standard installation is sufficient)
Usage: 
```
usage: check.py [-h] [--district_id DISTRICT_ID] [--date DATE] [--min_age_limit MIN_AGE_LIMIT] [--every_n_minutes EVERY_N_MINUTES] [--exact_date]

Check the free slots

optional arguments:
  -h, --help            show this help message and exit
  --district_id DISTRICT_ID
                        Default: 294, (which is Bangalore, BBMP)
  --date DATE           Default: Today
  --min_age_limit MIN_AGE_LIMIT
                        Default: 18
  --every_n_minutes EVERY_N_MINUTES
                        Default: 60
  --exact_date          Check exact date
  ```
Sample usage:
Check for slots in `gurgaon` for exact date `6-5-2021` every `1` minutes
```
python check.py --district_id=188 --date="6-5-2021" --min_age_limit=18 --every_n_minutes=1 --exact_date
```