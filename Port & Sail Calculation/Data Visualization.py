# Plotting the timeline of events
plt.figure(figsize=(12, 6))
for idx, row in df.iterrows():
    plt.plot([row['event_datetime'], row['next_event_datetime']], [idx, idx], marker='o')
    plt.text(row['event_datetime'], idx, row['event'], verticalalignment='bottom')

plt.xlabel('Datetime')
plt.ylabel('Event Index')
plt.title('Voyage Timeline')
plt.grid(True)
plt.show()
