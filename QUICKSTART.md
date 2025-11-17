# 🚀 Quick Start: ADIT Voice Presentations

## What You Get

A complete system to create **Visme-quality interactive presentations** with:
- ✅ **Synchronized voice narration** (OpenAI TTS)
- ✅ **Forward/backward navigation** (like Visme, better than Google Slides)
- ✅ **Audio control** - starts/stops with each slide
- ✅ **Password encryption** for secure delivery
- ✅ **Git hosting** with public access links

---

## 📺 See It In Action

**DEMO (No API key needed):**
```bash
# Open the demo presentation in your browser:
open demo_presentation.html

# Or on Linux:
xdg-open demo_presentation.html
```

This shows the full interactive experience (without actual voice - simulated audio indicators).

---

## ⚡ Create Your First Real Presentation

### **Step 1: Get OpenAI API Key**

1. Go to https://platform.openai.com/api-keys
2. Create new API key
3. Copy it (starts with `sk-...`)

### **Step 2: Set API Key**

```bash
# Set environment variable:
export OPENAI_API_KEY='sk-your-key-here'

# Or add to your shell profile (~/.bashrc or ~/.zshrc):
echo "export OPENAI_API_KEY='sk-your-key-here'" >> ~/.bashrc
source ~/.bashrc
```

### **Step 3: Install Dependencies**

```bash
pip install openai python-docx cryptography
```

### **Step 4: Create Presentation**

```bash
# Simple - creates from first DOCX found:
python create_presentation.py

# For specific topic:
python create_presentation.py 03

# You'll be prompted for:
# - Voice selection (alloy, echo, fable, onyx, nova, shimmer)
# - Encryption password (or press Enter for default)
```

### **Step 5: View Your Presentation**

```bash
# Start local server:
cd presentation_output
python -m http.server 8000

# Open browser to:
# http://localhost:8000/presentation.html
# (or http://localhost:8000/index.html if encrypted)
```

---

## 🎯 What Makes This Special

### **Unlike Google Slides:**
- ✅ Voice starts automatically with each slide
- ✅ Navigate backward without losing audio sync
- ✅ Standalone HTML file (no Google account needed)
- ✅ Works offline once downloaded
- ✅ Password-protected encryption

### **Like Visme:**
- ✅ Professional gradient designs
- ✅ Smooth animations and transitions
- ✅ Audio perfectly synchronized
- ✅ Progress indicators
- ✅ Multiple navigation methods (mouse, keyboard, touch)

### **Better Than Both:**
- ✅ AI-generated voice narration (6 professional voices)
- ✅ Costs ~$0.30 for 20-slide presentation
- ✅ Can be hosted anywhere (GitHub, S3, your server)
- ✅ Open-source and customizable

---

## 📖 Full Documentation

For complete details, see: **PRESENTATION_README.md**

Topics covered:
- Advanced API usage
- Batch processing multiple topics
- Encryption details
- GitHub Pages deployment
- Voice selection guide
- Troubleshooting
- Cost breakdown

---

## 🎤 Voice Recommendations

**For ADIT Tax Content:**
- **`onyx`** - Deep, authoritative (recommended for technical content)
- **`echo`** - Clear, professional (great for explanations)
- **`shimmer`** - Calm, smooth (best for long presentations)

**For Engaging Delivery:**
- **`nova`** - Energetic, friendly
- **`fable`** - Warm, expressive

**General Purpose:**
- **`alloy`** - Neutral, balanced (default)

---

## 💰 Costs

**OpenAI TTS Pricing:**
- $0.030 per 1,000 characters
- Average slide: ~500 characters = $0.015
- **20-slide presentation: ~$0.30**
- **100-slide course: ~$1.50**

Very affordable for professional quality!

---

## 🌐 Sharing Your Presentation

### **Option 1: GitHub Pages (Recommended)**
```bash
git add presentation_output/
git commit -m "Add ADIT voice presentation"
git push origin your-branch

# Enable GitHub Pages in repo settings
# Access via: https://yourusername.github.io/ADITER/presentation_output/
```

### **Option 2: Direct Link**
```bash
# Push to GitHub
git add presentation_output/
git commit -m "Add encrypted presentation"
git push

# Share raw GitHub link:
# https://raw.githubusercontent.com/yourusername/ADITER/branch/presentation_output/index.html
```

### **Option 3: Download & Share**
```bash
# Zip the presentation
cd presentation_output
zip -r presentation.zip .

# Share the zip file
# Recipients: Extract, open index.html, enter password
```

---

## 🎮 Navigation Shortcuts

| Action | Method |
|--------|--------|
| Next slide | `→` arrow or `Space` or Click "Next" |
| Previous slide | `←` arrow or Click "Previous" |
| Toggle audio | `M` key or Click audio button |
| Touch navigation | Swipe left/right |

---

## ❓ Quick Troubleshooting

**"OPENAI_API_KEY not set"**
```bash
export OPENAI_API_KEY='sk-...'
```

**"No DOCX files found"**
```bash
# Check available topics:
ls generated_notes/

# Run with topic number:
python create_presentation.py 03
```

**Audio not playing in browser**
- Use local server instead of opening file directly
- Check browser console for errors
- Try different browser (Chrome/Firefox work best)

---

## 📊 Example Workflow

**Create presentations for all ADIT topics:**

```bash
# Set API key once
export OPENAI_API_KEY='sk-...'

# Create presentations for topics 1-15
for i in {01..15}; do
    echo "Processing topic $i..."
    python create_presentation.py $i
done

# All presentations will be in presentation_output/
```

---

## 🎓 Next Steps

1. ✅ Try the demo: `open demo_presentation.html`
2. ✅ Get OpenAI API key: https://platform.openai.com/api-keys
3. ✅ Create your first presentation: `python create_presentation.py`
4. ✅ Share via GitHub: `git add presentation_output && git commit && git push`
5. ✅ Read full docs: `PRESENTATION_README.md`

---

**Ready? Let's create professional voice presentations! 🚀**

Questions? Check PRESENTATION_README.md for detailed documentation.
