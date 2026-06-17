import gradio as gr
from utils import send_request, create_payload

def process_prompt(message, history, temperature) -> str:
    base_prompt = message
    system_prompt = "You are a helpful assistant Mr.Chatty Agent."

    payload = create_payload(base_prompt, system_prompt, temperature)
    response = send_request(payload)
    return response["choices"][0]["message"]["content"]

# Add a slider for temperature control

with gr.Blocks() as app:
    temperature = gr.Slider(
        minimum=0.0,
        maximum=2.0,
        value=0.7,
        step=0.05,
        label="Temperature"
    )

    gr.ChatInterface(
        fn=process_prompt,
        additional_inputs=[temperature],
        chatbot=gr.Chatbot(height=500),
        textbox=gr.Textbox(
            placeholder="I'm your chat agent, how can I help you?",
            container=False,
        ),
        title="Chatty Agent",
        description="Ask Chatty Agent any question",
    )
