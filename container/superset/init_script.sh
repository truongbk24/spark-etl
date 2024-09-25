#!/bin/bash

# init superset
superset run --host 0.0.0.0 --port 8088
# Wait for Superset to fully initialize
sleep 10
