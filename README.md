# Portfolio Exporter

A portfolio exporter utility for Robinhood and any other brokers I may be interested in the future.

## Running the Exporter

```
python main.py
```

## Running the Server

Launch the server.

```
FLASK_APP=Exporter_Server.py flask run
```

Export credentials as env variables.

```
export rh_user="your username/email"
export rh_pass="your pass"
export rh_code="your 2 factor code if you have one"
```

Send an export request.

```
curl -d "{\"rh_user\" : \"${rh_user}\", \"rh_pass\": \"${rh_pass}\", \"code\" : \"${rh_code}\" }" \
  -H "Content-Type: application/json" \
  -X POST http://127.0.0.1:5000/
```

## TODO

- [ ] [Review] Setup end-of-day ticker price caching.

- [x] Export Robinhood portfolio to csv.
- [x] Export Robinhood portfolio to json.
- [x] Create a Robinhood Exporter microservice.
- [ ] Create a GUI for post-processing fields before they are exported.
