# Calculate event date-times
df['event_datetime'] = pd.to_datetime(df['dateStamp'], origin='1899-12-30', unit='D') + pd.to_timedelta(df['timeStamp'], unit='D')

# Sort by event_datetime
df = df.sort_values('event_datetime').reset_index(drop=True)

# Calculate previous and next events
df['prev_event_datetime'] = df['event_datetime'].shift(1)
df['next_event_datetime'] = df['event_datetime'].shift(-1)
df['prev_lat'] = df['lat'].shift(1)
df['prev_lon'] = df['lon'].shift(1)
df['next_lat'] = df['lat'].shift(-1)
df['next_lon'] = df['lon'].shift(-1)

# Calculate durations
df['port_stay_duration'] = np.where(df['event'] == 'SOSP', (df['event_datetime'] - df['prev_event_datetime']).dt.total_seconds() / 60, None)
df['sailing_time'] = np.where(df['event'] == 'EOSP', (df['next_event_datetime'] - df['event_datetime']).dt.total_seconds() / 60, None)

# Calculate distances
def calculate_distance(row):
    if pd.notnull(row['next_lat']) and pd.notnull(row['next_lon']):
        return geodesic((row['lat'], row['lon']), (row['next_lat'], row['next_lon'])).nautical
    return None

df['distance_travelled'] = df.apply(calculate_distance, axis=1)
