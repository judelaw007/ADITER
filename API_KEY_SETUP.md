# 🔑 OpenAI API Key Setup Guide

## ⚠️ Issue: "Access Denied" Error

If you're getting "Access denied" errors when generating voice, your API key needs proper permissions.

---

## ✅ Solution: Enable TTS Access

### **Step 1: Check Your API Key Type**

Go to: https://platform.openai.com/api-keys

Your API key shows as: `sk-proj-...`

This is a **project-scoped key**. You need to ensure:
1. ✅ TTS (Text-to-Speech) is enabled for your project
2. ✅ Billing is set up with available credits
3. ✅ Usage limits allow TTS calls

---

### **Step 2: Enable TTS for Your Project**

1. Go to: https://platform.openai.com/settings/organization/projects
2. Select your project
3. Under **"Capabilities"** or **"Permissions"**:
   - Enable **Audio/TTS**
   - Enable **TTS-1-HD** model access

---

### **Step 3: Verify Billing**

1. Go to: https://platform.openai.com/settings/organization/billing
2. Add payment method if needed
3. Check you have available credits
4. TTS costs: **$0.030 per 1,000 characters**
   - 5-slide presentation: ~$0.10
   - 20-slide presentation: ~$0.30

---

### **Step 4: Create a New API Key (If Needed)**

If project-scoped keys are limited, create a **user-level key**:

1. Go to: https://platform.openai.com/api-keys
2. Click **"Create new secret key"**
3. Name it: "ADIT Presentations"
4. **Don't** select a specific project (for full access)
5. Copy the key (starts with `sk-...`)
6. Use this key instead

---

## 🧪 Test Your New Key

```bash
export OPENAI_API_KEY='sk-your-new-key-here'
python3 create_simple_presentation.py 02 --voice onyx --max-slides 3
```

You should see:
```
✓ Generating voice for slide 1...
  ✓ Generated: slide_000.mp3 (45.2KB)
```

---

## 🔧 Alternative: Use Different OpenAI Account

If you can't enable TTS on your current project:

1. Create new OpenAI account (free trial gives $5 credit)
2. Get API key from new account
3. Use that for testing:

```bash
export OPENAI_API_KEY='sk-new-account-key'
python3 create_simple_presentation.py 02 --max-slides 5
```

---

## 📊 Current Status

✅ **What's Working:**
- Interactive HTML5 presentation framework
- Navigation (forward/backward, keyboard, touch)
- Professional Visme-quality design
- Slide parsing from DOCX
- Audio synchronization system

⚠️ **What Needs API Key Fix:**
- OpenAI TTS voice generation
- MP3 audio file creation

---

## 🎯 Once API Key is Fixed

You'll be able to run:

```bash
# Create full presentation with voice
python3 create_simple_presentation.py 02 --voice onyx --max-slides 10

# Or all 15 topics
for i in {01..15}; do
    python3 create_simple_presentation.py $i --voice onyx --max-slides 10
done
```

**Expected cost**: ~$0.15-0.30 per presentation

---

## 💡 What You Have Now

Even without voice, you have:

1. ✅ **Interactive presentation** at `presentation_output/presentation.html`
2. ✅ **Full navigation system** (arrows, buttons, touch)
3. ✅ **Professional design** (gradients, animations)
4. ✅ **Complete framework** ready for voice

Try it now:
```bash
cd presentation_output
python -m http.server 8000
# Open: http://localhost:8000/presentation.html
```

Navigate with ← → arrows!

---

## 📞 Need Help?

1. **OpenAI Support**: https://help.openai.com/
2. **API Key Issues**: https://platform.openai.com/docs/guides/authentication
3. **Check API Status**: https://status.openai.com/

---

## 🚀 Next Steps

1. ✅ Fix API key permissions (enable TTS)
2. ✅ Add credits to account
3. ✅ Re-run: `python3 create_simple_presentation.py 02`
4. ✅ Enjoy voice-enabled presentations!

Your presentation system is fully built and ready - just needs the API key permissions fixed!
