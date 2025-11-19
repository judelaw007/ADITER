# Gemini 2.5 TTS Allowlist Access Request

## Status: ⏳ Waiting for Google Approval

Gemini 2.5 TTS models (`gemini-2.5-flash-preview-tts` and `gemini-2.5-pro-preview-tts`) are in **limited preview** and require allowlist access from Google.

## Configuration (Ready to Use)

✅ **API Key**: Configured in `.env`
✅ **Project ID**: `gen-lang-client-0281545330`
✅ **Script**: `generate_audio_gemini_tts.py` ready
✅ **Billing**: Configured (will activate when allowlisted)

## How to Request Access

### Google AI Developers Forum (Recommended)

1. Visit: https://discuss.ai.google.dev/t/request-allowlist-access-for-gemini-tts-preview/107235

2. Post this request:

```
Hello Google Gemini Team,

I would like to request allowlist access for Gemini 2.5 TTS preview.

Project Details:
- Project ID: gen-lang-client-0281545330
- Region: [Your region, e.g., us-central1]
- Models Needed: gemini-2.5-flash-preview-tts, gemini-2.5-pro-preview-tts

Use Case:
Creating professional educational audio narration for ADIT (Advanced Diploma in International Taxation) training presentations. We need high-quality TTS for 23 tax education modules.

Thank you!
```

3. Wait for Google team response (typically 2-5 business days)

### Alternative: Google AI Studio Support

1. Go to https://aistudio.google.com
2. Click Feedback/Support
3. Request TTS preview access with your project details

## What Happens After Approval

Once Google allowlists your project:

1. ✅ The 403 errors will stop
2. ✅ Run: `python3 generate_audio_gemini_tts.py`
3. ✅ All 23 audio files will be generated with Gemini 2.5 TTS
4. ✅ Audio will be higher quality than Google Cloud TTS

## Current Status

- **Presentations are live**: https://judelaw007.github.io/ADITER/generated_notes/01_Fundamental_tax_issues/presentations/
- **Audio currently using**: Google Cloud TTS (en-US-Neural2-D voice)
- **Ready to upgrade**: As soon as allowlist approved

## Testing After Approval

Run this command to test:
```bash
python3 test_gemini_tts.py
```

If successful, generate all audio:
```bash
python3 generate_audio_gemini_tts.py        # Uses Flash (faster, cheaper)
python3 generate_audio_gemini_tts.py --pro  # Uses Pro (higher quality)
```

---

**Last Updated**: 2025-11-19
