# Fundamental Tax Issues - Interactive Presentation Suite

## 📚 Overview

Complete HTML5 presentation suite for ADIT Fundamental Tax Issues module with voice-over narration.

## 📂 Structure

```
presentations/
├── index.html              # Subject welcome page
├── curriculum.html         # Course curriculum overview
├── 01-income-flows-*.html  # Chapter 1: International Income Flows (9 files)
├── 02-investment-*.html    # Chapter 2: International Investment (8 files)
├── 03-treaties-*.html      # Chapter 3: Tax Treaties (9 files)
├── 04-transfer-*.html      # Chapter 4: Transfer Pricing (9 files)
├── voiceover_scripts/      # TTS scripts (3500-7000 chars each)
│   ├── ch01_sec01_*.txt    # Individual scripts per section
│   ├── ch01_sec02_*.txt
│   └── ALL_SCRIPTS.txt     # Master script file
└── audio/                  # Generated MP3 audio files (to be created)
    ├── ch01_sec01_*.mp3
    ├── ch01_sec02_*.mp3
    └── ...
```

## 🎯 Files

- **Total HTML files**: 37 (index + curriculum + 35 chapter files)
- **Total chapters**: 4
- **Total sections**: 23
- **Voice-over scripts**: 23 (one per section)

## 🎙️ Generating Audio Files

### Step 1: Get Google API Key

Choose one of these options:

#### Option A: Google Cloud Text-to-Speech (Recommended)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable "Cloud Text-to-Speech API"
4. Go to APIs & Services → Credentials
5. Create API Key
6. Copy the key (starts with `AIza...`)

**Cost**: ~$0.30 per 1 million characters (~$0.08 for all 23 scripts)

#### Option B: Gemini API (Experimental)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create API Key
3. Copy the key

### Step 2: Generate Audio

From the ADITER root directory:

```bash
# Set your API key
export GOOGLE_API_KEY='your-api-key-here'

# Generate all audio files using Google Cloud TTS
python3 generate_audio_files.py

# Or use Gemini API (if supported)
python3 generate_audio_files.py --gemini
```

This will:
- Read all 23 voice-over scripts
- Generate professional audio narration
- Save MP3 files to `audio/` directory
- Show progress and summary

### Step 3: Verify Audio

```bash
# Check generated audio files
ls -lh generated_notes/01_Fundamental_tax_issues/presentations/audio/

# Play a sample (on systems with afplay/mpg123)
afplay generated_notes/01_Fundamental_tax_issues/presentations/audio/ch01_sec01_*.mp3
```

## 🌐 Viewing Presentations

### Local Server

```bash
cd generated_notes/01_Fundamental_tax_issues/presentations
python3 -m http.server 8000
```

Then open: http://localhost:8000

### Navigation

- **Welcome Page** (`index.html`) → Start here
- **Curriculum** → View all 4 chapters
- **Chapter Pages**:
  - Topic introduction
  - Sequential content pages (one per main section)
  - Assessment quiz
  - Completion page

### Controls

- Click "Next" buttons to progress
- Use browser back button to return
- Progress bars show completion
- Responsive design works on mobile/tablet

## 📝 Voice-Over Scripts

All scripts follow these specifications:

- **Length**: 3500-7000 characters per script
- **Tone**: Natural, conversational academic voice
- **Style**: Direct explanation with no introductions
- **Format**: Paragraphs for natural breathing pauses
- **Content**: Only from original study notes

### Script Files

```
voiceover_scripts/
├── ch01_sec01_Core_Framework_for_Tax_Analysis.txt
├── ch01_sec02_Principal_Categories_of_Inco.txt
├── ...
└── ALL_SCRIPTS.txt (master file with all scripts)
```

## 🎨 Design

Professional HTML5 templates with:

- **Colors**:
  - Primary: #003F87 (Navy Blue)
  - Secondary: #0066CC (Blue)
  - Accent: #FF6B35 (Orange)
- **Typography**: System fonts (SF Pro, Segoe UI, Roboto)
- **Layout**: Responsive grid, mobile-first
- **Animations**: Smooth transitions, hover effects
- **Gradients**: Professional blue-to-blue gradients

## 📊 Content Summary

### Chapter 1: International Income Flows (6 sections)
- Core Framework for Tax Analysis
- Principal Categories of Income
- Source and Residence Principles
- Tax Considerations in Energy & Resources
- Taxation of Financial Instruments
- Advanced Topics in Cross-Border Income

### Chapter 2: International Investment (5 sections)
- Investment Structure Fundamentals
- Direct vs Portfolio Investment
- Branch vs Subsidiary Structures
- Holding Company Structures
- Practical Considerations

### Chapter 3: Tax Treaties (6 sections)
- Purpose and Structure
- Key Treaty Provisions
- Business Profits Article
- Dividend, Interest, and Royalty Articles
- Capital Gains and Other Income
- Treaty Interpretation and Application

### Chapter 4: Transfer Pricing (6 sections)
- Fundamental Concepts
- Arm's Length Principle
- Transfer Pricing Methods
- Documentation Requirements
- Practical Application Issues
- Dispute Resolution Mechanisms

## 🔧 Troubleshooting

### Audio Generation Issues

**Error: "No API key found"**
- Ensure `GOOGLE_API_KEY` is set in environment
- Check key starts with `AIza` (Google Cloud) or valid Gemini format

**Error: "403 Forbidden"**
- Enable Text-to-Speech API in Google Cloud Console
- Check API key has correct permissions
- Verify billing is enabled (for Google Cloud)

**Error: "Quota exceeded"**
- Google Cloud has free tier limits
- Upgrade to paid tier or wait for quota reset

### Presentation Issues

**Audio not playing**
- Ensure audio files exist in `audio/` directory
- Check browser console for errors
- Try different browser (Chrome/Firefox recommended)

**Layout issues**
- Clear browser cache
- Check viewport on mobile devices
- Ensure JavaScript is enabled

## 📈 Statistics

- **Total HTML pages**: 37
- **Total sections**: 23
- **Average script length**: 3,643 characters
- **Estimated total audio duration**: ~45-50 minutes
- **File size (HTML only)**: 577KB
- **Expected audio size**: ~40-50MB

## 🚀 Next Steps

1. ✅ Generate audio files (see Step 2 above)
2. ✅ Review presentation in browser
3. ✅ Test audio playback
4. ✅ Share presentation URL or files
5. ✅ Create additional chapters if needed

## 📞 Support

For issues:
- Check Google Cloud TTS documentation: https://cloud.google.com/text-to-speech/docs
- Review Gemini API docs: https://ai.google.dev/docs
- Verify all files are present and properly named

---

**Created**: 2025-11-19
**Generator**: ADIT Presentation Suite Builder
**Source**: Enhanced DOCX study notes from quality_checked folder
