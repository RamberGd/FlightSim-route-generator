# FlightSim Route Generator


**FlightSim Route Generator** is a desktop app built with PyQt5 that helps generate realistic flight routes for flight simulators. You can set constraints such as minimum/maximum distance and number of results, and choose whether to fix a departure airport or an arrival airport. The app calculates valid airport combinations and outputs them with distances.


> ⚠️ Note: This is an old project I built a few years ago. It is no longer maintained or supported, and I do not plan to update it in the future. The repository is kept online for reference and educational purposes.


## Features

🛫 **Custom Routes**: Generate routes based on distance range and departure/arrival constraints.

📍 **Airport Selector**: Enter an ICAO airport code and fix it as departure, arrival, or none.

📊 **Distance Calculation**: Outputs each route with the exact distance.

⚠️ **Error Handling**: Detects invalid input (e.g. letters in distance fields) and shows helpful error messages.

🖥️ **Simple Interface**: Clean PyQt5 UI designed for ease of use.



## Screenshots

Main interface (empty input):

<img width="459" height="633" alt="cf1b8eb2-3d1f-468e-945e-dc533e29b986" src="https://github.com/user-attachments/assets/4b836c93-bb4f-49df-95c5-336f9ce2a32d" />

Generated results:

<img width="471" height="625" alt="1a5ba3da-844b-44de-8716-dc6aaf5786f6" src="https://github.com/user-attachments/assets/ae39ca6e-2a80-4c3f-9fc1-6ded8f659a04" />


Error handling (invalid input):

<img width="463" height="635" alt="d4b46bd4-0a16-49af-928f-86429e05534e" src="https://github.com/user-attachments/assets/c9a5d89a-6e93-42cd-8fed-79c8c5fbdf03" />

## Getting Started

### Prerequisites

- Python 3.9+

- PyQt5

- pandas

### Installation & Run

**Clone the repository:**

```git clone https://github.com/yourusername/flightsim-route-generator.git```

```cd flightsim-route-generator```

**Install dependencies:**



```pip install pyqt5 pandas```

**Run the app:**

```python main.py```

### Usage

1. Enter minimum distance, maximum distance, and number of results.
2. Specify an ICAO airport code (optional).
3.Select whether the airport is Departure, Arrival, or None.
4. Click Generate.
5. View the generated routes with distances in the output box.

License
This project is licensed under the MIT License.
