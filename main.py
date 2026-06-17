from ui import app

# Tried but couldn't get the openvpn to connect to KV server
# So i tried to use the local server of LM Studio instead which hosted a qwen3 4B model
# And made a gradio interface to interact with it

def main():
    app.launch(theme="ocean")

if __name__ == "__main__":
    main()