import os

# Allow online fallback when offline DB has no or weak matches
ALLOW_ONLINE = os.getenv('ALLOW_ONLINE', 'true').lower() in {'1', 'true', 'yes'}

# API key for accessing the service
API_KEY = os.getenv('FORMULA_API_KEY', 'your-default-api-key-here')

# Wolfram Alpha AppID (optional). Set environment variable WOLFRAM_APPID
WOLFRAM_APPID = os.getenv('WOLFRAM_APPID', '').strip()

# Gemini API Key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyBR-vd0xQLe0F16EzoAGQ3W97BIJp26DIk')

# Default online provider order
ONLINE_PROVIDERS = os.getenv('ONLINE_PROVIDERS', 'wolfram,newton,gemini').split(',')
