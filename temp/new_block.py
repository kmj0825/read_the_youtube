import gradio as gr


def update(name):
    out1 = f"Welcome to Gradio, {name}1!"
    out2 = f"Welcome to Gradio, {name}2!"
    out3 = f"Welcome to Gradio, {name}3!"
    return out1, out2, out3


with gr.Blocks() as demo:
    gr.Markdown("Start typing below and then click **Run** to see the output.")
    with gr.Column():
        inp1 = gr.Textbox(placeholder="What is your name?")
        inp2 = gr.Dropdown(["Option 1", "Option 2", "Option 3"])
    with gr.Row():
        out1 = gr.Textbox()
        out2 = gr.Textbox()
        out3 = gr.Textbox()
    with gr.Row():
        out3 = gr.Textbox()

    btn = gr.Button("Run")
    btn.click(fn=update, inputs=[inp1,inp2], outputs=[out1, out2, out3])

demo.launch()
