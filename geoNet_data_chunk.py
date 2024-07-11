from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import matplotlib.pyplot as plt
import seisbench.models as sbm

# Initialize the FDSN client for GeoNet
client = Client("GEONET")

# Define the time window for the data

client = Client("GEONET")
time = UTCDateTime("2024-05-03T22:05:30")
stream = client.get_waveforms(network="NZ", station="WEL", location="*", channel="HH?", starttime=time-100, endtime=time+100)

# Plot the waveform data
fig = plt.figure(figsize=(15, 5))
ax = fig.add_subplot(111)
for tr in stream:
    ax.plot(tr.times(), tr.data, label=tr.stats.channel)
ax.legend()
plt.show()