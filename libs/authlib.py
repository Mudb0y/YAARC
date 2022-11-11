import random
import socket
import os
import webbrowser
import sys
import praw

reddit = praw.Reddit(
    client_id="WRnvoABCPNMo9XugPFUDrg",
    client_secret="",
    refresh_token=None,
    redirect_uri="http://localhost:8080",
    user_agent="YAARC/V0.1.0 by u/stas-prze",
    )

# This sets up the token if it's not already there.
def get_token():
    global reddit
    scopes = "*"
    state = str(random.randint(0, 65000))
    url = reddit.auth.url(duration="permanent", scopes=scopes, state=state)

    webbrowser.open (url)

    client = receive_connection()
    data = client.recv(1024).decode("utf-8")
    param_tokens = data.split(" ", 2)[1].split("?", 1)[1].split("&")
    params = {
        key: value for (key, value) in [token.split("=") for token in param_tokens]
    }

    if state != params["state"]:
        send_message(
            client,
            f"State mismatch. Expected: {state} Received: {params['state']}",
        )
        return 1
    elif "error" in params:
        send_message(client, params["error"])
        return 1

    refresh_token = reddit.auth.authorize(params["code"])
    with open ("token.auth", "w") as f:
        f.write (refresh_token)
    send_message(client, f"YAARC successfully authorised! You may now close this window and return to the app.")
    return 0

def receive_connection():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 8080))
    server.listen(1)
    client = server.accept()[0]
    server.close()
    return client

def send_message(client, message):
    client.send(f"HTTP/1.1 200 OK\r\n\r\n{message}".encode("utf-8"))
    client.close()

def authorise():
    if os.path.exists("token.auth"):
        with open ("token.auth", "r") as f:
            refresh_token = f.read()
        reddit.auth.refresh_token = refresh_token
    else:
        get_token()
