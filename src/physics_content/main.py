#!/usr/bin/env python
import sys
import json
import os
import re
from pathlib import Path
from datetime import datetime

# Add src directory to Python path to allow importing physics_content
current_dir = Path(__file__).resolve().parent
src_dir = current_dir.parent
sys.path.insert(0, str(src_dir))

from physics_content.crew import PhysicsContentCrew

# Configuration
ARTIFACTS_DIR = Path("artifacts")
CONTENT_DIR = ARTIFACTS_DIR / "content"
INDEX_DIR = ARTIFACTS_DIR / "index"

def ensure_dirs(chapter_number):
    (CONTENT_DIR / str(chapter_number)).mkdir(parents=True, exist_ok=True)
    (INDEX_DIR / str(chapter_number)).mkdir(parents=True, exist_ok=True)

def parse_index_output(raw_output: str) -> list:
    """Robustly parse the JSON list from the agent output (Biology Reference Logic)"""
    try:
        # Try direct JSON parsing
        return json.loads(raw_output)
    except json.JSONDecodeError:
        pass
    
    # Clean markdown
    clean_str = raw_output
    if "```json" in raw_output:
        clean_str = raw_output.split("```json")[1].split("```")[0]
    elif "```" in raw_output:
        clean_str = raw_output.split("```")[1].split("```")[0]
        
    try:
        return json.loads(clean_str)
    except json.JSONDecodeError:
        # Fallback: Split by lines if it looks like a list
        print("⚠️ Direct JSON parse failed. Attempting line-based fallback.")
        lines = [line.strip().strip('"').strip(',') for line in clean_str.split('\n') if line.strip()]
        # Try to reconstruct basic objects if it's just lines? 
        # Actually, for Chemistry agents trained to output JSON, let's just log error
        # But Biology code had a fallback. Let's assume list of dicts is complex to regex.
        # We will return None to trigger error handling in caller.
        return None

def run_planning_phase(chapter_number, chapter_name):
    """Phase 1: Generate or Load the Index"""
    index_file = INDEX_DIR / str(chapter_number) / "chapter_index.json"
    
    # 1. Check Cache
    if index_file.exists():
        print(f"\n📝 PHASE 1: Loading cached index from {index_file}...")
        try:
            with open(index_file, "r", encoding="utf-8") as f:
                sections_list = json.load(f)
            print(f"✅ Loaded {len(sections_list)} sections from cache.")
            return sections_list
        except Exception as e:
            print(f"⚠️ Failed to load cached index: {e}. Regenerating...")

    # 2. Generate New
    print(f"\n🧠 STARTING PLANNING PHASE for Chapter {chapter_number}...")
    
    crew_builder = PhysicsContentCrew()
    planning_crew = crew_builder.planning_crew()
    
    inputs = {
        'chapter_number': chapter_number,
        'chapter_name': chapter_name
    }
    
    result = planning_crew.kickoff(inputs=inputs)
    raw_output = str(result)
    
    index_data = parse_index_output(raw_output)
    
    if index_data:
        try:
            with open(index_file, 'w') as f:
                json.dump(index_data, f, indent=2)
            print(f"✅ Plan created: {len(index_data)} sections defined.")
            return index_data
        except Exception as e:
            print(f"❌ Failed to save Index JSON: {e}")
            return None
    else:
        print(f"❌ Failed to parse Index JSON. Raw output:\n{raw_output}")
        return None

def run_manager_loop(chapter_number, chapter_name, index_data):
    """Phase 2: The Manager Loop"""
    print(f"\n🔄 STARTING MANAGER LOOP for {len(index_data)} sections...")
    
    crew_builder = PhysicsContentCrew()
    
    for i, section in enumerate(index_data):
        sec_num = section.get('section_number', f"{chapter_number}.{i+1}")
        sec_title = section.get('title', 'Untitled')
        subtopics = section.get('subtopics', [])
        
        # Ensure subtopics is a string for the written inputs
        if isinstance(subtopics, list):
            subtopics_str = ', '.join(subtopics)
        else:
            subtopics_str = str(subtopics)
            
        print(f"\n✍️  Writing Section {i+1}/{len(index_data)}: {sec_num} {sec_title}")
        
        # Check if section file already exists (Resume capability)
        safe_title = re.sub(r'[^\w\-_\. ]', '_', sec_title)
        filename = f"{sec_num}_{safe_title}.md".replace(' ', '_')
        file_path = CONTENT_DIR / str(chapter_number) / filename
        
        if file_path.exists():
            print(f"⏩ Skipping existing section: {filename}")
            continue
        
        # Fresh crew for each section (The Secret Sauce)
        writer_crew = crew_builder.writing_crew()
        
        inputs = {
            'chapter_number': chapter_number,
            'chapter_name': chapter_name,
            'section_number': sec_num,
            'section_title': sec_title,
            'subtopics': subtopics_str
        }
        
        result = writer_crew.kickoff(inputs=inputs)
        
        # Clean Output
        content = str(result)
        # Remove markdown code blocks if present
        if content.startswith("```markdown"):
            content = content.replace("```markdown", "", 1)
        if content.startswith("```"):
             content = content.replace("```", "", 1)
        if content.endswith("```"):
            content = content[:-3]
            
        content = content.strip()

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ Saved section to {file_path}")

def stitch_chapter(chapter_number, chapter_name):
    """Phase 3: Assembly"""
    print("\n🧵 ASSEMBLING CHAPTER...")
    
    chapter_dir = CONTENT_DIR / str(chapter_number)
    output_file = f"class_11_math_chapter_{chapter_number}_{chapter_name}_Full.md"
    
    # Robust sorting: Natural Sort (1.2 before 1.10)
    import re
    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', str(s))]
    
    # Post-processing: Fix math syntax (convert \[...\] to $$...$$)
    def cleanup_math_syntax(content):
        # Convert \[...\] to $$...$$
        content = re.sub(r'\\\[', '$$', content)
        content = re.sub(r'\\\]', '$$', content)
        # Convert \(...\) to $...$
        content = re.sub(r'\\\(', '$', content)
        content = re.sub(r'\\\)', '$', content)
        return content
    
    files = sorted(chapter_dir.glob("*.md"), key=lambda f: natural_sort_key(f.name))
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(f"# Chapter {chapter_number}: {chapter_name}\n\n")
        
        for f in files:
            with open(f, 'r', encoding='utf-8') as infile:
                section_content = infile.read()
                section_content = cleanup_math_syntax(section_content)  # <-- Post-process
                outfile.write(section_content)
                outfile.write("\n\n---\n\n")
    
    print(f"🎉 Chapter Complete! Saved to {output_file}")

# Define Class 11 Mathematics Chapters
CHAPTERS_TO_GENERATE = [
    {"chapter_number": "1", "chapter_name": "Sets"},
    {"chapter_number": "2", "chapter_name": "Relations_and_Functions"},
    {"chapter_number": "3", "chapter_name": "Trigonometric_Functions"},
    {"chapter_number": "4", "chapter_name": "Complex_Numbers_and_Quadratic_Equations"},
    {"chapter_number": "5", "chapter_name": "Linear_Inequalities"},
    {"chapter_number": "6", "chapter_name": "Permutations_and_Combinations"},
    {"chapter_number": "7", "chapter_name": "Binomial_Theorem"},
    {"chapter_number": "8", "chapter_name": "Sequences_and_Series"},
    {"chapter_number": "9", "chapter_name": "Straight_Lines"},
    {"chapter_number": "10", "chapter_name": "Conic_Sections"},
    {"chapter_number": "11", "chapter_name": "Introduction_to_Three_Dimensional_Geometry"},
    {"chapter_number": "12", "chapter_name": "Limits_and_Derivatives"},
    {"chapter_number": "13", "chapter_name": "Statistics"},
    {"chapter_number": "14", "chapter_name": "Probability"}
]

def main():
    if len(sys.argv) >= 3:
        # CLI Mode
        chapter_number = sys.argv[1]
        chapter_name = sys.argv[2]
        ensure_dirs(chapter_number)
        
        index_data = run_planning_phase(chapter_number, chapter_name)
        if index_data:
            run_manager_loop(chapter_number, chapter_name, index_data)
            stitch_chapter(chapter_number, chapter_name)
    else:
        # Interactive Mode
        print("\n📐 CLASS 11 MATHEMATICS GENERATOR 📐")
        print("======================================")
        print("Available Chapters:")
        for ch in CHAPTERS_TO_GENERATE:
            print(f" {ch['chapter_number']}. {ch['chapter_name'].replace('_', ' ')}")
        print("======================================")
        
        try:
            raw_input = input("\nEnter Chapter Number to Generate: ").strip()
            
            # Find selected chapter
            selected = next((c for c in CHAPTERS_TO_GENERATE if c['chapter_number'] == raw_input), None)
            
            if selected:
                print(f"\n✅ Selected: {selected['chapter_name']}")
                chapter_number = selected['chapter_number']
                chapter_name = selected['chapter_name']
                
                ensure_dirs(chapter_number)
                
                # 1. Plan
                index_data = run_planning_phase(chapter_number, chapter_name)
                
                if index_data:
                    # 2. Executing Loop
                    run_manager_loop(chapter_number, chapter_name, index_data)
                    
                    # 3. Stitch
                    stitch_chapter(chapter_number, chapter_name)
                else:
                    print("❌ Aborted due to planning failure.")
            else:
                print("❌ Invalid Chapter Number!")
                
        except KeyboardInterrupt:
            print("\n👋 Exiting...")

if __name__ == "__main__":
    main()
