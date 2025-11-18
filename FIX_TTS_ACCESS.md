# 🔧 QUICK FIX: Enable TTS for Your API Key

## ❌ Current Issue

Your API key: `sk-proj-TRBS8JqlBgZe...`
Error: **403 Forbidden - Access denied**

This is a **project-scoped key** without TTS permissions.

---

## ✅ Solution 1: Enable TTS for Your Project (2 minutes)

### **Steps:**

1. **Go to OpenAI Projects**: https://platform.openai.com/settings/organization/projects

2. **Find your project** (the one this API key belongs to)

3. **Click on the project** → **Settings** or **Permissions**

4. **Enable "Audio" or "TTS" capabilities**
   - Look for checkboxes or toggles for different API capabilities
   - Make sure **Audio**, **TTS**, or **Speech** is enabled

5. **Save changes**

6. **Try again**:
   ```bash
   python3 test_tts_detailed.py
   ```

---

## ✅ Solution 2: Create a New User-Level API Key (1 minute)

If you can't enable TTS on the project, create a user-level key instead:

### **Steps:**

1. **Go to API Keys**: https://platform.openai.com/api-keys

2. **Click "Create new secret key"**

3. **Important**:
   - Name it: "ADIT-TTS-Presentations"
   - **Don't select a specific project** (leave as "All projects" or your user account)
   - This creates a user-level key with full access

4. **Copy the key** (starts with `sk-...` not `sk-proj-...`)

5. **Use it**:
   ```bash
   export OPENAI_API_KEY='sk-your-new-key-here'
   python3 create_simple_presentation.py 02 --voice onyx --max-slides 5
   ```

---

## ✅ Solution 3: Check Billing (Just in Case)

Sometimes "Access denied" means no credits/billing:

1. **Go to Billing**: https://platform.openai.com/settings/organization/billing

2. **Check**:
   - Is a payment method added?
   - Do you have available credits?
   - Is there a spending limit blocking usage?

3. **Add credits** if needed (TTS is very cheap: ~$0.30 per presentation)

---

## 🧪 Test After Fixing

Once you fix the API key permissions, test it:

```bash
# Test TTS access
python3 test_tts_detailed.py

# If successful, create a presentation with voice!
python3 create_simple_presentation.py 02 --voice onyx --max-slides 5
```

You should see:
```
✓ SUCCESS! Generated audio file: 45000 bytes
✓ Generating voice for slide 1...
  ✓ Generated: slide_000.mp3 (45.2KB)
```

---

## 🎯 My Recommendation

**Try Solution 2** (create new user-level key) - it's the fastest and most reliable.

Project-scoped keys are often restricted by default. A user-level key will have full TTS access immediately.

---

## 📞 Still Having Issues?

If you still get "Access denied" after trying these:

1. Check OpenAI status: https://status.openai.com/
2. Contact OpenAI support: https://help.openai.com/
3. Verify your account has TTS access enabled

Your account might need TTS/Audio capability enabled at the organization level.

---

## 💡 Once It Works

You'll be able to create presentations with voice:

```bash
# Create with voice narration
python3 create_simple_presentation.py 02 --voice onyx --max-slides 10

# Encrypt it
python3 create_encrypted_presentation.py --password ADIT2025

# Share the link!
```

Cost: ~$0.20-0.30 per presentation with high-quality AI voice narration.

---

Let me know which solution you try and if you need help!
