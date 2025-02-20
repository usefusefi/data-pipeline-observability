from opentelemetry import metrics
from prometheus_client import start_http_server

start_http_server(8000)

metrics.get_meter_provider().create_counter(
    "records_processed",
    description="Number of records processed"
)
