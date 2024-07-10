from prometheus_client import start_http_server, Counter

# defining Prometheus metrics
packetCount = Counter('totalPackets', 'Total number of packets')
suspiciousPacketCount = Counter('suspiciousPackets', 'Number of suspicious packets')

def startMetricsServer():
    # starting Prometheus Server
    start_http_server(8000)