import os

from theflow.settings import settings as flowsettings

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Kiểm tra xem key có được load không
api_key = os.getenv('GRAPHRAG_API_KEY')
print(os.getcwd())  # Kiểm tra current working directory
print(os.environ.get('GRAPHRAG_API_KEY'))
print(api_key)
if not api_key:
    raise ValueError("GRAPHRAG_API_KEY not found in environment variables")


KH_APP_DATA_DIR = getattr(flowsettings, "KH_APP_DATA_DIR", ".")
KH_GRADIO_SHARE = getattr(flowsettings, "KH_GRADIO_SHARE", False)
GRADIO_TEMP_DIR = os.getenv("GRADIO_TEMP_DIR", None)
# override GRADIO_TEMP_DIR if it's not set
if GRADIO_TEMP_DIR is None:
    GRADIO_TEMP_DIR = os.path.join(KH_APP_DATA_DIR, "gradio_tmp")
    os.environ["GRADIO_TEMP_DIR"] = GRADIO_TEMP_DIR


from ktem.main import App  # noqa

app = App()
demo = app.make()
demo.queue().launch(
    favicon_path=app._favicon,
    inbrowser=True,
    allowed_paths=[
        "libs/ktem/ktem/assets",
        GRADIO_TEMP_DIR,
    ],
    share=KH_GRADIO_SHARE,
    server_name="0.0.0.0",
    server_port=7860
)
