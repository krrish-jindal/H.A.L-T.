import http.server
import socketserver
from prometheus_client import start_http_server
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily, REGISTRY
import time
import random
import redis


PORT = 8030

Handler = http.server.SimpleHTTPRequestHandler

def get_vden_value():
    val = r.get("tlimit")
    return val

def get_tlimit_value():
    val = r.get("vden")
    return val
def get_eservice_value():
    val = r.get("eservice")
    return val


r = redis.Redis(
host='localhost',
port=6379,
)
