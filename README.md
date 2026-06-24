# AnomX
A real-time anomaly detection system using machine learning and Ai models.

## Project Overview and Objectives

The project gives us a decent understading of -

- Synthetic financial activity datasets
- Feature engineering pipelines
- Classical anomaly detection models
- Deep learning sequence models
- Streaming data pipelines
- FastAPI inference APIs
- Explainable anomaly alerts

## Week 1-2

### Python
I used the a tutorial to brush up my python basics and to learn the python syntax. 
The tutorial gave me a recap of the following topics:
- Few basic syntaxes in python
- Data structures(lists,tuple,set,dictionary)
- Functions
- File handling
- OOPs
- Modules and packages 

The link to the tutorial is given below:

[Programiz - Python tutorial](https://www.programiz.com/python-programming)

### Numpy and Pandas

#### Numpy 

- Using numpy arrays and array manipulation
- aggregation and statistical funtions 
- linear algebra inn numpy
- random module

#### Pandas

- using pandas to read and write csv, excel and tab seperated text files
- slicing and indexing 
- sorting and filtering the data
- working with large datasets 

The resources used are -

- Official documetation
- [Pandas - youtube link](https://www.youtube.com/watch?v=vmEHCJofslg)
- [Numpy - youtube link](https://www.youtube.com/watch?v=GB9ByFAIAH4)

### Understanding Anomaly detection

- Anomalies are the events that deviate from the expected or the normal behaviour. 
- In this project we try to detect the anomalies in a synthetic finacial dataset.
- There could a variety of anomalies like - abnormal prices, large volume trade, suspicious logins etc

### Documentation and Learning Practices 

- Briefly document what all learnt throughout the project in README
- Understand the code rather than just using in my repo


## Week 3

Thoroughly understood the code for the generation of the synthetic financial data.

### The dataset is produced by `generate_events.py` in four stages:

1. **User profile generation** (`build_user_profiles()`) — creates synthetic users, each with a home country, IP address, preferred device, typical trade volume, typical deposit amount, and account creation date.
2. **Normal event generation** (`generate_normal_event()`) — generates everyday activity (logins, trades, deposits, withdrawals, sessions, KYC changes) consistent with each user's baseline profile.
3. **Anomaly injection** — a subset of users is deliberately flagged as anomalous and made to generate known suspicious behavior patterns.
4. **Export** (`generate_dataset()`) — everything is combined and written to `events.csv`.

### Events 

| Event Type | Count | Description |
|---|---|---|
| `trade` | 17,446 | Instrument, lot size, volume, P&L, margin used, trade duration |
| `login` | 11,014 | IP, country, device, success/failure, timezone gap |
| `deposit` | 7,565 | Amount, method |
| `session` | 6,021 | Duration, page clicks, click rate |
| `withdrawal` | 5,115 | Amount, whether immediate after a deposit |
| `kyc_change` | 2,839 | Type of KYC field changed |

### Dataset structure

The dataset contains the following features for each user event.

| Category | Features |
|-----------|----------|
| **Event Metadata** | `event_id`, `user_id`, `event_type`, `timestamp`, `hour_of_day`, `day_of_week`, `is_weekend` |
| **Anomaly Labels** | `is_anomalous`, `anomaly_type` |
| **Login Features** | `ip_address`, `country`, `device`, `login_success`, `failed_attempts`, `timezone_gap_hours` |
| **Trade Features** | `instrument`, `lot_size`, `trade_volume`, `pnl`, `margin_used`, `trade_duration_seconds`, `trade_volume_vs_baseline`, `is_night_trade` |
| **Deposit / Withdrawal Features** | `amount`, `method`, `is_immediate_withdrawal` |
| **Session Features** | `session_duration_mins`, `page_clicks`, `click_rate_per_min` |
| **KYC Features** | `kyc_change_type` |
| **Account Features** | `account_age_days` |

### Key insights

- creating visualizations and mathematics for the anomalous patterns
- The scalability of the code increases as we use the config directory to specify the configurations of the dataset rather than hard-coding. 

### Commands for generation of the data

```
python .\src\data_gen\generate_events.py 
```

## Week 4

### Features created from raw event logs

1. **Time-based features** — `time_since_last_event_sec`, `time_since_last_login_sec`, `time_since_last_deposit_sec`
2. **Rolling window statistics** — mean/std of trade volume and P&L over the last 5, 10, and 30 events (`roll_5_trade_vol_mean`, `roll_10_pnl_std`, etc.)
3. **Session activity** — rolling mean click rate (`roll_5_click_rate_mean`, `roll_10_click_rate_mean`, `roll_30_click_rate_mean`)
4. **Burst features** — `burst_count_5min`, `burst_count_30min` (event counts in short recent windows)
5. **Login behavior** — `unique_ips_last_10_logins`, `unique_countries_last_10_logins`, `unique_devices_last_10_logins`, `rolling_failed_attempts_5`
6. **Financial behavior** — `roll_5_deposit_sum`, `withdrawal_to_deposit_ratio`
7. **Statistical z-scores** — `trade_vol_zscore`, `pnl_zscore`, `amount_zscore`, `session_duration_zscore`, 

### Why these features are useful for anomaly detection

These feautures are important because raw data only gives us informationa about a single user event. It does not compare the certain event with the usual behaviour of the user.
These features are the comparitive measures that can be used to judge the deviatin of a user behaviour from the normal, thus helping in finding the anomalies.


### Key observations

- The raw data isnt solely useful to identify anomalies. We have to parse the raw data creating features that are the measures of the deviation of a user behaviour from norm.
- also a feature like burst cant be taken as a sure sign of an anomaly but can be considered as a strong sign of one 

### Commmands to generate the features.csv

```
python -m src.features.feature_enginnering.py
```

## Expectations from the submission

- The repo contains the code required for the generation of the data(`src\data_gen\generate_events.py`) 
- The repo contains the code required for the parsing of the raw data into features(`src\features\feature_engineering.py`)
- README contains the documentation, resources used and the commands required to run the code.
- Repo doesnot contain the data folder that can be generated using the commands in the README










