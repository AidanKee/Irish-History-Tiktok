# config.py
class Settings:
work_dir: str
output_dir: str
assets_dir: str


# Wikimedia
wiki_lang: str
min_year: int


# LLM / script gen
use_openai: bool
openai_api_key: str | None
openai_model: str


# Azure TTS
azure_key: str | None
azure_region: str | None
azure_voice: str


# TikTok API
tiktok_access_token: str | None
tiktok_open_id: str | None
tiktok_publish_mode: str # "public" | "private"


# Video
width: int
height: int
font_file: str
brand_hex: str


# Control
enable_posting: bool


@classmethod
def from_env(cls):
return cls(
work_dir=os.getenv("WORK_DIR", "./work"),
output_dir=os.getenv("OUTPUT_DIR", "./output"),
assets_dir=os.getenv("ASSETS_DIR", "./assets"),
wiki_lang=os.getenv("WIKI_LANG", "en"),
min_year=int(os.getenv("MIN_YEAR", "1600")),
use_openai=os.getenv("USE_OPENAI", "false").lower() == "true",
openai_api_key=os.getenv("OPENAI_API_KEY"),
openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
azure_key=os.getenv("AZURE_TTS_KEY"),
azure_region=os.getenv("AZURE_TTS_REGION"),
azure_voice=os.getenv("AZURE_TTS_VOICE", "en-IE-EmilyNeural"),
tiktok_access_token=os.getenv("TIKTOK_ACCESS_TOKEN"),
tiktok_open_id=os.getenv("TIKTOK_OPEN_ID"),
tiktok_publish_mode=os.getenv("TIKTOK_PUBLISH_MODE", "public"),
width=int(os.getenv("VIDEO_WIDTH", "1080")),
height=int(os.getenv("VIDEO_HEIGHT", "1920")),
font_file=os.getenv("FONT_FILE", "./assets/Inter-Regular.ttf"),
brand_hex=os.getenv("BRAND_HEX", "#0ea5e9"),
enable_posting=os.getenv("ENABLE_POSTING", "true").lower() == "true",
)
