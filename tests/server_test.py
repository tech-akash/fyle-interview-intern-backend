import json
from flask import jsonify
from datetime import datetime,timezone
from core.libs import helpers
def test_ready_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'ready'
    assert 'time' in data
    dt_str = data['time']
    dt_format = '%a, %d %b %Y %H:%M:%S %Z'
    dt_utc = datetime.strptime(dt_str, dt_format).replace(tzinfo=timezone.utc)
    dt_now = datetime.utcnow().replace(microsecond=0,tzinfo=timezone.utc)
    assert dt_utc == dt_now