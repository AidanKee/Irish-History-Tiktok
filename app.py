# app.py




def main():
log = setup_logging()
tz = zoneinfo.ZoneInfo("Europe/Dublin")
now = datetime.now(tz)


log.info(f"Starting daily run for {now:%Y-%m-%d} (Europe/Dublin)")


settings = Settings.from_env()
ensure_dirs([settings.work_dir, settings.output_dir, settings.assets_dir])


# 1) Fetch events and pick the top one
event = get_top_irish_events(now.month, now.day, settings=settings)
if not event:
log.warning("No Irish-related events found today. Exiting.")
return


log.info(f"Selected event: {event['year']} — {event['text']}")


# 2) Generate script (voiceover text + on-screen captions + hashtags)
script = generate_script(event, settings=settings)
log.info("Script generated.")


# 3) TTS
voiceover_path = synthesize_speech(
text=script["voiceover_text"],
voice=settings.azure_voice,
settings=settings,
)
log.info(f"Voiceover synthesized: {voiceover_path}")


# 4) Video assembly
video_path = build_video(
event=event,
script=script,
voice_path=voiceover_path,
settings=settings,
)
log.info(f"Video built: {video_path}")


# 5) TikTok post
if settings.enable_posting:
post_id = tiktok_post(
video_path=video_path,
caption=script["caption"],
settings=settings,
)
log.info(f"Posted to TikTok. Post ID (if returned): {post_id}")
else:
log.info("Posting disabled (ENABLE_POSTING=false). Skipping upload.")




if __name__ == "__main__":
try:
main()
except Exception as e:
print("Fatal error:", e, file=sys.stderr)
traceback.print_exc()
sys.exit(1)
