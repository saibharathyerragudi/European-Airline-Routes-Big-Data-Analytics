# Data Dictionary

## Route Identifiers

| Field | Description |
|---|---|
| `id` | Route identifier |
| `iata_from` | Departure airport IATA code |
| `iata_to` | Arrival airport IATA code |
| `departure_city` | Departure city |
| `departure_country` | Departure country |
| `arrival_airport_city_name` | Arrival airport city |
| `arrival_airport_country` | Arrival airport country |

## Pricing And Schedule

| Field | Description |
|---|---|
| `price` | Route price |
| `day1` to `day7` | Operating-day flags from source data |
| `flights_per_day` | Text field describing daily frequency |
| `flights_per_week` | Weekly flight frequency |
| `common_duration` | Common route duration |
| `first_flight` | First scheduled flight date |
| `last_flight` | Last scheduled flight date |

## Airport Metadata

| Field | Description |
|---|---|
| `departure_ICAO` | Departure airport ICAO code |
| `arrival_ICAO` | Arrival airport ICAO code |
| `arrival_airport_name` | Arrival airport name |
| `arrival_airport_no_routes` | Route count associated with the arrival airport |

## Geography

| Field | Description |
|---|---|
| `departure_latitude` | Departure airport latitude |
| `departure_longitude` | Departure airport longitude |
| `departure_altitude` | Departure airport altitude |
| `arrival_latitude` | Arrival airport latitude |
| `arrival_longitude` | Arrival airport longitude |
| `arrival_altitude` | Arrival airport altitude |

## Engineered Features

| Field | Description |
|---|---|
| `days_operated` | Number of days per week the route operates |
| `is_daily_route` | Flag for routes that operate all seven days |
| `distance_km` | Haversine distance between departure and arrival airports |
| `price_per_km` | Price divided by distance |
