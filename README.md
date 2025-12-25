
# Computer Control Remotely   

This project demonstrates a Python-based client–server system for remote control and monitoring in a local network, where a server sends keyboard commands to a client and receives screenshots in response. The purpose is to explore network communication, input automation, and screen capture in a controlled environment. The scope includes real-time keyboard events and image data transmitted over sockets, intended for educational and experimental use.

## Requirements

- Python 3.10+
- Network connection between server and client machines
- Required Python libraries (see requirements.txt)
## Configuration

Edit
```
  constants.py
```
to match your network setup
## Project Structure 

ControlTakingProject/

├── main_server.py # Server entry point

├── main_client.py # Client entry point

├── keyboard_sending_server.py # Server keyboard logic

├── keyboard_getting_client.py # Client keyboard receiver

├── server_screenshots.py # Server screenshot handling

├── client_screenshots.py # Client screenshot capture

├── constants.py # Shared configuration

└── README.md # Project documentation
## Run Locally

Clone the project

```bash
  git clone https://github.com/samTop123/ControlTakingProject.git
```

Go to the project directory

```bash
  cd ControlTakingProject
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server - From The Server Side

```bash
  python main_server.py
```

Start the client - From The Client Side

```bash
  python main_client.py
```



## Authors

- [@samTop123](https://www.github.com/samTop123)

