import gradio as gr
from ktem.app import BasePage
from theflow.settings import settings as flowsettings

KH_DEMO_MODE = getattr(flowsettings, "KH_DEMO_MODE", False)

if not KH_DEMO_MODE:
    PLACEHOLDER_TEXT = (
        "This is the beginning of a new conversation.\n"
        "Start by uploading a file or a web URL. "
        "Visit Files tab for more options (e.g: GraphRAG)."
    )
else:
    PLACEHOLDER_TEXT = (
        "Welcome to Kido Assistant. "
        "Start by browsing preloaded conversations to get onboard.\n"
        "Check out Hint section for more tips."
    )


class ChatPanel(BasePage):
    def __init__(self, app):
        self._app = app
        self.on_building_ui()
        self.default_files = [
            "docs/data/ChinhSach.md",
            "docs/data/Dữ liệu AI - chính sách bán hàng Bánh.pdf",
            "docs/data/Dữ liệu AI - chính sách bán hàng Dầu.pdf",
            "docs/data/Dữ liệu AI - kiến thức bán hàng.pdf",
            "docs/data/Dữ liệu AI - kiến thức nền tảng.pdf",
            # Thêm các file mặc định khác
        ]

        self.chatbot = gr.Chatbot(
            label=self._app.app_name,
            placeholder=PLACEHOLDER_TEXT,
            show_label=False,
            elem_id="main-chat-bot",
            show_copy_button=True,
            likeable=True,
            bubble_full_width=False,
        )
        with gr.Row():
            self.text_input = gr.MultimodalTextbox(
                interactive=True,
                scale=20,
                file_count="multiple",
                placeholder=(
                    "Type a message, search the @web, or tag a file with @filename"
                ),
                container=False,
                show_label=False,
                elem_id="chat-input",
            )

    def submit_msg(self, chat_input, chat_history):
        """Submit a message to the chatbot"""
        return "", chat_history + [(chat_input, None)]

    def _on_app_created(self):
        """Set default light theme when app loads"""
        self._app.app.load(
            fn=lambda: None,
            inputs=None,
            outputs=None,
            js="""
                () => {
                    document.body.classList.remove('dark');
                    document.body.classList.add('light');
                }
            """
        )
