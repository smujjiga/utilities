# Common Utilities
# **1. Periodic Covid Vaccination slot checker**
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
                        Default: 45 (use 45 or 18)
  --every_n_minutes EVERY_N_MINUTES
                        Default: 60
  --exact_date          Check exact date
  ```
Sample usage: 
Check for slots in `gurgaon` for exact date `6-5-2021` every `1` minutes

(from windows command line or Unix/Mac cli)

```
python check.py --district_id=188 --date="6-5-2021" --min_age_limit=18 --every_n_minutes=1 --exact_date
```
### **How to find district id**
1. Get the state ID from the url:  [https://cdn-api.co-vin.in/api/v2/admin/location/states](https://cdn-api.co-vin.in/api/v2/admin/location/states)
2. Get the distrcit ID from the url : [https://cdn-api.co-vin.in/api/v2/admin/location/districts/16](https://cdn-api.co-vin.in/api/v2/admin/location/districts/16) by replace the digit **`16`** with the state ID in which the district falls in.
  
Few district IDs:

| Name            | IDs |
| --------------- | --- |
| Bangalore Rural | 276 |
| Bangalore Urban | 265 |
| Bangalore BBMP  | 294 |
| Central Delhi   | 141 |
| New Delhi       | 140 |
| Gurgaon         | 188 |
| Mumbai          | 395 |
| Hyderabad       | 581 |
| Chennai         | 571 |
