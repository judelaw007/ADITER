#!/usr/bin/env python3
"""
ADIT Energy Resources Note Generator
Automated overnight generation with resume capability
"""

import anthropic
import csv
import json
import time
from pathlib import Path
from datetime import datetime
import sys

# Configuration
API_KEY = "YOUR_ANTHROPIC_API_KEY_HERE"  # Replace with your actual key
MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 16000

# File paths
CSV_FILE = "ADIT_Energy_Resources_Syllabus (2).csv"
PROGRESS_FILE = "generation_progress.json"
OUTPUT_DIR = Path("generated_notes")
LOG_FILE = "generation_log.txt"

# Knowledge level to word count mapping
WORD_COUNTS = {
    "Broad": 3000,      # Level 1
    "Detailed": 4500,   # Level 2
    "Advanced": 6000    # Level 3
}

# Examples mapping
EXAMPLES_COUNT = {
    "1": 1,
    "2": 2,
    "3": 3
}

class ADITNoteGenerator:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=API_KEY)
        self.progress = self.load_progress()
        self.setup_directories()
        
    def setup_directories(self):
        """Create necessary directories"""
        OUTPUT_DIR.mkdir(exist_ok=True)
        
    def load_progress(self):
        """Load generation progress from file"""
        if Path(PROGRESS_FILE).exists():
            with open(PROGRESS_FILE, 'r') as f:
                return json.load(f)
        return {
            "completed": [],
            "failed": [],
            "last_index": -1,
            "started_at": None
        }
    
    def save_progress(self):
        """Save current progress"""
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def log(self, message):
        """Log message to file and console"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        with open(LOG_FILE, 'a') as f:
            f.write(log_message + "\n")
    
    def read_csv(self):
        """Read topics from CSV"""
        topics = []
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                topics.append({
                    'subject': row['Subject'],
                    'chapter': row['Chapter'],
                    'examples': row['Examples'],
                    'knowledge_level': row['Knowledge Level']
                })
        return topics
    
    def create_generation_prompt(self, topic):
        """Create the detailed prompt for generating a note"""
        
        word_count = WORD_COUNTS.get(topic['knowledge_level'], 4500)
        num_examples = int(topic['examples'])
        
        prompt = f"""# ADIT Energy Resources Note Generation

## Topic Specifications
- **Subject**: {topic['subject']}
- **Chapter**: {topic['chapter']}
- **Knowledge Level**: {topic['knowledge_level']}
- **Target Word Count**: {word_count} words (±10%)
- **Required Examples**: {num_examples} worked examples

## Your Task
Create a comprehensive study note following these EXACT specifications:

### RESEARCH PHASE (Complete This First)

You MUST perform web searches to:
1. Verify current statutory framework and regulations
2. Find recent case law and guidance (2023-2025)
3. Identify international standards (OECD, UN, World Bank where relevant)
4. Check for 2025 developments

**Use these search queries**:
- "[topic name] tax regulations 2025"
- "[topic name] OECD guidelines"
- "[topic name] international tax framework"
- "[topic name] recent case law"

### CONTENT STRUCTURE

Use numbered sections (1, 1.1, 1.2 style):

**1. Core Framework (20-25% of content)**
- Statutory basis with specific legislation references
- Key definitions (bold on first use)
- Fundamental principles

**2. Technical Rules (30-35%)**
- Rates, thresholds, conditions
- Exemptions and reliefs
- Use tables for rate comparisons
- Bullet points ONLY for statutory lists

**3. Analytical Depth (20-25%)**
- How provisions interact
- Cross-border implications
- Anti-avoidance considerations
- Compliance requirements

**4. Application Methodology (10-15%)**
- Step-by-step approach
- Decision frameworks
- Common scenarios

**5. Worked Examples ({num_examples} required)**
Each example MUST have:
- Clear fact pattern
- Complete technical analysis
- Calculations with full working
- Statutory references cited
- Definitive conclusion

### VISUAL ELEMENTS (20% of content - MANDATORY)
Include:
- Comparison tables
- Flowcharts for decision processes
- Rate/threshold tables
- Process diagrams
- Calculation templates

### WRITING STANDARDS
- **Bold**: Key terms, section numbers, rates, thresholds
- *Italicize*: Case names
- Define technical terms using authoritative sources
- Professional prose, not bullet-point lists
- Cite sources inline: [Source, Year]

### CRITICAL REQUIREMENTS
✓ Integrate 2025 developments naturally (if any exist)
✓ All statutory references must be accurate
✓ Technical depth appropriate for {topic['knowledge_level']} level
✓ No placeholders or incomplete sections
✓ No exam technique advice
✓ No separate "changes" section
✓ No bibliographies

### OUTPUT FORMAT
Provide the complete note in markdown format, ready for conversion to Word document.

Begin generation now."""

        return prompt
    
    def generate_note(self, topic, index, total):
        """Generate a single note using Claude API"""
        
        topic_name = f"{topic['subject']} - {topic['chapter']}"
        self.log(f"Starting generation {index+1}/{total}: {topic_name}")
        
        try:
            # Create the prompt
            prompt = self.create_generation_prompt(topic)
            
            # Make API call with extended thinking
            self.log(f"  → Sending to Claude API...")
            message = self.client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                temperature=1,
                thinking={
                    "type": "enabled",
                    "budget_tokens": 10000
                },
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Extract the generated content
            content = ""
            for block in message.content:
                if block.type == "text":
                    content += block.text
            
            if not content:
                raise ValueError("No content generated")
            
            # Save the markdown file
            safe_filename = f"{topic['subject']}_{topic['chapter']}".replace(" ", "_").replace("/", "_")
            md_file = OUTPUT_DIR / f"{safe_filename}.md"
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.log(f"  ✓ Generated and saved: {md_file.name}")
            
            # Update progress
            self.progress['completed'].append(topic_name)
            self.progress['last_index'] = index
            self.save_progress()
            
            return True, md_file
            
        except Exception as e:
            self.log(f"  ✗ Failed: {str(e)}")
            self.progress['failed'].append({
                'topic': topic_name,
                'error': str(e),
                'index': index
            })
            self.save_progress()
            return False, None
    
    def run(self, start_index=None, max_topics=None):
        """Run the generation process"""
        
        # Read topics
        topics = self.read_csv()
        total = len(topics)
        
        # Determine starting point
        if start_index is None:
            start_index = self.progress['last_index'] + 1
        
        if start_index >= total:
            self.log("All topics already completed!")
            return
        
        # Set end point
        end_index = total
        if max_topics:
            end_index = min(start_index + max_topics, total)
        
        # Start generation
        if not self.progress['started_at']:
            self.progress['started_at'] = datetime.now().isoformat()
            self.save_progress()
        
        self.log("=" * 60)
        self.log(f"ADIT Note Generation Started")
        self.log(f"Topics: {start_index + 1} to {end_index} (of {total})")
        self.log(f"Estimated time: {(end_index - start_index) * 25} minutes")
        self.log("=" * 60)
        
        successful = 0
        failed = 0
        
        for i in range(start_index, end_index):
            topic = topics[i]
            
            # Generate the note
            success, _ = self.generate_note(topic, i, total)
            
            if success:
                successful += 1
            else:
                failed += 1
            
            # Brief pause between generations (API courtesy)
            if i < end_index - 1:
                time.sleep(3)
        
        # Final summary
        self.log("=" * 60)
        self.log(f"Generation Complete!")
        self.log(f"Successful: {successful}")
        self.log(f"Failed: {failed}")
        self.log(f"Total completed so far: {len(self.progress['completed'])}/{total}")
        self.log("=" * 60)
        
        if failed > 0:
            self.log("\nFailed topics:")
            for fail in self.progress['failed']:
                self.log(f"  - {fail['topic']}: {fail['error']}")

def main():
    """Main entry point"""
    
    # Check for API key
    if API_KEY == "YOUR_ANTHROPIC_API_KEY_HERE":
        print("ERROR: Please set your Anthropic API key in the script!")
        print("Edit generate_adit_notes.py and replace YOUR_ANTHROPIC_API_KEY_HERE")
        sys.exit(1)
    
    generator = ADITNoteGenerator()
    
    # Parse command line arguments
    start_index = None
    max_topics = 10  # Default: 10 topics per run
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            max_topics = None
        elif sys.argv[1] == "--continue":
            start_index = None  # Resume from last
        else:
            try:
                max_topics = int(sys.argv[1])
            except:
                print(f"Usage: {sys.argv[0]} [number_of_topics|--all|--continue]")
                sys.exit(1)
    
    # Run generation
    generator.run(start_index=start_index, max_topics=max_topics)

if __name__ == "__main__":
    main()
