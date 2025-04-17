#!/bin/bash

# --------------------------------------------
# Path Setup
# --------------------------------------------
PROMETHEUS_DIR="/opt/prometheus"
ALERTMANAGER_DIR="/opt/alertmanager"
GRAFANA_BIN="/usr/sbin/grafana-server"
GRAFANA_HOME="/usr/share/grafana"
GRAFANA_CONF="/etc/grafana/grafana.ini"

PORT1=9090
PORT2=9093
PORT3=3000
MAX_WAIT=120
COUNT=0
# --------------------------------------------
# Log directories
# --------------------------------------------
rm -rf /var/log/monitoring
mkdir -p /var/log/monitoring

PROMETHEUS_LOG="/var/log/monitoring/prometheus.log"
ALERTMANAGER_LOG="/var/log/monitoring/alertmanager.log"
GRAFANA_LOG="/var/log/monitoring/grafana.log"

echo "start monitoring services"
set -e

# --------------------------------------------
# Start Prometheus
# --------------------------------------------
echo "start prometheus services"
if [ -d "$PROMETHEUS_DIR" ]; then
  echo "Starting Prometheus..."
  nohup "$PROMETHEUS_DIR/prometheus" \
    --config.file="$PROMETHEUS_DIR/prometheus.yml" \
    > "$PROMETHEUS_LOG" 2>&1 &
else
  echo "Prometheus directory not found: $PROMETHEUS_DIR"
fi

# listening whether port 9090 is open or not
while true; do
  if nc -z localhost $PORT1; then
    echo "monitoring container: port 9090 is open and listening"
    echo "monitoring container: successful to launch prometheus"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "monitoring container: Timeout: port $PORT1 not open"
    echo "monitoring container: FAILED to launch prometheus"
    exit 1
  fi
done

# --------------------------------------------
# Start Alertmanager
# --------------------------------------------
if [ -d "$ALERTMANAGER_DIR" ]; then
  echo "Starting Alertmanager..."
  nohup "$ALERTMANAGER_DIR/alertmanager" \
    --config.file="$ALERTMANAGER_DIR/alertmanager.yml" \
    > "$ALERTMANAGER_LOG" 2>&1 &
else
  echo "Alertmanager directory not found: $ALERTMANAGER_DIR"
fi

while true; do
  if nc -z localhost $PORT2; then
    echo "monitoring container: port 9093 is open and listening"
    echo "monitoring container: successful to launch Alertmanager"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "monitoring container: Timeout: port $PORT2 not open"
    echo "monitoring container: FAILED to launch Alertmanager"
    exit 1
  fi
done

# --------------------------------------------
# Start Grafana
# --------------------------------------------
if [ -f "$GRAFANA_BIN" ]; then
  echo "Starting Grafana..."
  nohup "$GRAFANA_BIN" \
    --homepath="$GRAFANA_HOME" \
    --config="$GRAFANA_CONF" \
    > "$GRAFANA_LOG" 2>&1 &
else
  echo "Grafana server not found at: $GRAFANA_BIN"
fi

while true; do
  if nc -z localhost $PORT3; then
    echo "monitoring container: port 3000 is open and listening"
    echo "monitoring container: successful to launch Grafana"
    break
  fi
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_WAIT ]; then
    echo "monitoring container: Timeout: port $PORT3 not open"
    echo "monitoring container: FAILED to launch Grafana"
    exit 1
  fi
done

echo "FINISHED: start monitoring services. Logs in /var/log/monitoring"