import os
import json
import subprocess

# 1. Run Mock Data Generator
result = subprocess.run(['python', r'Paper_I_Aptitude\Mock_Data_Generator.py'], capture_output=True, text=True)
mock_data_output = result.stdout

# 2. Collect all md files
content_dict = {}
for root, dirs, files in os.walk('.'):
    if '.git' in root or '__pycache__' in root:
        continue
    for f in files:
        if f.endswith('.md') or f.endswith('.txt') or f == 'Conquest_Plan.html':
            filepath = os.path.join(root, f)
            clean_path = filepath.replace('\\', '/').replace('./', '')
            with open(filepath, 'r', encoding='utf-8') as file:
                content_dict[clean_path] = file.read()

# 3. Create HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UGC NET Anthropology Portal</title>
    <!-- Custom Fonts for Concepts, Definitions, Formulas -->
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@500&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            /* Conquest Plan Dark Theme Default */
            --bg-base: #1a1208;
            --bg-surface: #20170c;
            --bg-elevated: rgba(245,237,214,0.04);
            --primary: #c8922a; /* gold */
            --primary-variant: #e8b84b; /* gold-light */
            --secondary: #2d4a2d; /* forest */
            --text-main: #f5edd6; /* parchment */
            --text-muted: #ede0c0; /* parchment-dark */
            --border: rgba(200,146,42,0.3);
            --studied: #5a9a5a;
            --warning: #7a1c2e; /* crimson */
            --font-headings: 'Playfair Display', serif;
            --font-body: 'Source Serif 4', Georgia, serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        .light-theme {
            --bg-base: #fdf6e3;
            --bg-surface: #f5edd6;
            --bg-elevated: #ede0c0;
            --primary: #8b3a1e; /* rust */
            --primary-variant: #c8922a; /* gold */
            --secondary: #3d4a5c; /* slate */
            --text-main: #1a1208;
            --text-muted: #4a3f32;
            --border: rgba(139,58,30,0.3);
            --studied: #2d4a2d;
            --warning: #c05030;
        }

        /* Scroll Progress */
        #scroll-progress {
            position: sticky; top: 0; left: 0; height: 4px; z-index: 1000; width: 0%;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            border-top-right-radius: 4px; border-bottom-right-radius: 4px; transition: width 0.15s ease-out;
        }

        /* Topbar tools */
        .topbar-tools { display: flex; align-items: center; gap: 15px; margin-left: auto; }
        .icon-btn {
            background: var(--bg-elevated); border: 1px solid var(--border); color: var(--text-main);
            width: 40px; height: 40px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center;
            font-size: 1.2rem; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .icon-btn:hover {
            transform: translateY(-2px) rotate(10deg); box-shadow: 0 4px 12px rgba(0,0,0,0.1); color: var(--primary); border-color: var(--primary);
        }

        /* Pomodoro Timer Widget */
        #pomodoro-widget {
            position: fixed; bottom: 30px; right: 30px; background: var(--bg-surface); border: 1px solid var(--primary);
            border-radius: 16px; padding: 15px 25px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            display: flex; align-items: center; gap: 20px; z-index: 1000; backdrop-filter: blur(10px);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        #pomodoro-widget:hover { transform: translateY(-5px) scale(1.02); box-shadow: 0 15px 35px rgba(0,0,0,0.15); border-color: var(--secondary); }
        #pomodoro-time { font-size: 1.8rem; font-weight: bold; color: var(--primary); font-variant-numeric: tabular-nums; letter-spacing: 1px; }
        .pomo-btn { background: none; border:none; color: var(--text-muted); cursor: pointer; font-size: 1.2rem; transition: all 0.2s; padding: 5px; border-radius: 8px;}
        .pomo-btn:hover { color: var(--primary); background: var(--bg-elevated); transform: scale(1.1); }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: var(--font-body);
            background-color: var(--bg-base);
            background-image: 
                radial-gradient(ellipse at 20% 10%, rgba(139,58,30,0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 90%, rgba(45,74,45,0.08) 0%, transparent 50%),
                url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23c8922a' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            color: var(--text-main);
            line-height: 1.7;
            display: flex;
            height: 100vh;
            overflow: hidden;
        }

        /* Sidebar */
        #sidebar {
            width: 300px;
            background-color: var(--bg-surface);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            transition: transform 0.3s ease;
            z-index: 10;
        }
        #sidebar-header { padding: 20px; border-bottom: 1px solid var(--border); }
        #sidebar-header h1 { font-size: 1.2rem; color: var(--primary); margin-bottom: 10px; border:none; padding:0;}
        #search-container { position: relative; }
        #search-bar {
            width: 100%; padding: 10px 10px 10px 35px; border-radius: 6px; border: 1px solid var(--border);
            background-color: var(--bg-elevated); color: var(--text-main); outline: none;
        }
        #search-icon { position: absolute; left: 10px; top: 50%; transform: translateY(-50%); color: var(--text-muted); }
        #nav-links { flex: 1; overflow-y: auto; padding: 15px 0; }
        .nav-section { padding: 10px 20px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-top: 10px; }
        .nav-item { display: block; padding: 10px 20px; color: var(--text-main); text-decoration: none; cursor: pointer; transition: background 0.2s; }
        .nav-item:hover, .nav-item.active { background-color: var(--bg-elevated); border-left: 4px solid var(--primary); }

        /* Main */
        #main-content { flex: 1; display: flex; flex-direction: column; overflow-y: auto; background-color: var(--bg-base); position: relative; }
        #topbar { display: none; background-color: var(--bg-surface); padding: 15px 20px; border-bottom: 1px solid var(--border); align-items: center; }
        #menu-toggle { background: none; border: none; color: var(--primary); font-size: 1.5rem; cursor: pointer; margin-right: 15px; }
        #content-area { padding: 40px; max-width: 900px; margin: 0 auto; width: 100%; }

        h1, h2, h3, h4 { color: var(--primary); margin-bottom: 15px; margin-top: 30px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap:10px; font-family: var(--font-headings); font-weight: 700;}
        h1 { border-bottom: 2px solid var(--border); padding-bottom: 10px; font-size: 2.2rem; text-shadow: 0 2px 10px rgba(200,146,42,0.1); }
        p, ul, ol { margin-bottom: 20px; font-size: 1.05rem; }
        ul, ol { padding-left: 20px; }
        li { margin-bottom: 8px; }

        .smart-feature { 
            background-color: var(--bg-elevated); padding: 20px; border-radius: 12px; border-left: 5px solid var(--secondary); margin: 25px 0; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: transform 0.3s, box-shadow 0.3s;
        }
        .smart-feature:hover { transform: translateX(5px); box-shadow: 0 8px 15px rgba(0,0,0,0.05); }
        .smart-feature.common-mistakes { border-left-color: var(--warning); }
        .smart-feature.cross-links { border-left-color: var(--primary); }

        /* Auto-Highlighted Content Elements */
        .highlight-concept {
            font-family: var(--font-mono);
            color: var(--primary-variant);
            background: rgba(200,146,42,0.1);
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }
        .light-theme .highlight-concept {
            color: var(--primary);
            background: rgba(139,58,30,0.1);
        }

        /* PDF Supplementary Content Styling */
        .pdf-supplementary-content {
            background: var(--bg-elevated);
            padding: 25px;
            border-left: 4px solid var(--primary);
            margin: 30px 0;
            border-radius: 6px;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.02);
        }
        .pdf-supplementary-content h3 {
            font-family: var(--font-mono);
            color: var(--text-muted);
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 0;
            border-bottom: 1px dashed var(--border);
            padding-bottom: 10px;
        }
        .pdf-supplementary-content h4 {
            font-family: var(--font-headings);
            color: var(--primary-variant);
            font-size: 1.25rem;
            margin-top: 25px;
            margin-bottom: 15px;
        }
        .pdf-supplementary-content p {
            font-family: 'Source Serif 4', Georgia, serif; /* Enforce textbook serif */
            color: var(--text-main);
            font-size: 1.05rem;
            line-height: 1.8;
            margin-bottom: 15px;
        }
        .pdf-highlight {
            font-weight: 700;
            color: var(--text-main);
            background: linear-gradient(120deg, rgba(200,146,42,0.15) 0%, rgba(200,146,42,0.15) 100%);
            padding: 0 4px;
            border-radius: 2px;
        }
        .light-theme .pdf-highlight {
            background: linear-gradient(120deg, rgba(139,58,30,0.1) 0%, rgba(139,58,30,0.1) 100%);
        }
        .pdf-keyword {
            font-weight: bold;
            color: var(--secondary);
        }
        .pdf-context-highlight {
            background: rgba(200,146,42,0.1);
            border-radius: 4px;
            padding: 2px 4px;
            box-shadow: -2px 0 0 var(--secondary);
            display: inline;
            line-height: 1.9;
        }

        .highlight-definition {
            font-family: var(--font-headings);
            font-style: italic;
            background: linear-gradient(120deg, rgba(200,146,42,0.2) 0%, rgba(200,146,42,0.2) 100%);
            background-repeat: no-repeat;
            background-size: 100% 40%;
            background-position: 0 88%;
            font-weight: 700;
            color: var(--text-main);
        }

        .light-theme .highlight-definition {
            background: linear-gradient(120deg, rgba(139,58,30,0.15) 0%, rgba(139,58,30,0.15) 100%);
            background-repeat: no-repeat;
            background-size: 100% 40%;
            background-position: 0 88%;
        }

        .highlight-formula {
            font-family: 'Fira Code', monospace;
            background: rgba(14, 165, 233, 0.1);
            color: var(--secondary);
            padding: 4px 8px;
            border-radius: 6px;
            border: 1px dashed var(--secondary);
            display: inline-block;
            margin: 5px 0;
            font-size: 0.9rem;
        }

        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid var(--border); padding: 10px; text-align: left; }
        th { background-color: var(--bg-elevated); color: var(--primary); }

        /* Buttons */
        .btn-mark-studied {
            background-color: var(--bg-elevated); border: 1px solid var(--border); color: var(--text-muted);
            padding: 5px 12px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; transition: all 0.2s;
        }
        .btn-mark-studied:hover { border-color: var(--studied); color: var(--studied); }
        .btn-mark-studied.studied { background-color: rgba(76, 175, 80, 0.1); border-color: var(--studied); color: var(--studied); }
        
        #toggle-revision {
            position: sticky; top: 10px; z-index: 100; float: right;
            background: linear-gradient(135deg, var(--primary), var(--primary-variant)); border: none;
            color: white; padding: 10px 20px; border-radius: 30px; cursor: pointer; font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: transform 0.2s;
        }
        #toggle-revision:hover { transform: scale(1.05); }

        /* Quick Revision Mode (Hides non-essentials) */
        body.quick-revision-mode p:not(.smart-feature p),
        body.quick-revision-mode table,
        body.quick-revision-mode .common-mistakes,
        body.quick-revision-mode .cross-links {
            display: none !important;
        }

        /* MCQ Section */
        .mcq-container { margin-top: 50px; border-top: 2px solid var(--border); padding-top: 30px; }
        .progress-box { background: var(--bg-surface); padding: 15px; border-radius: 8px; margin-bottom: 20px; position: sticky; top: 60px; z-index: 90; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border: 1px solid var(--border);}
        .progress-bar { width: 100%; height: 10px; background: var(--bg-elevated); border-radius: 5px; overflow: hidden; margin-top: 10px; }
        .progress-fill { height: 100%; background: var(--secondary); width: 0%; transition: width 0.3s; }
        
        .mcq-card { background: var(--bg-surface); padding: 20px; border-radius: 8px; border: 1px solid var(--border); margin-bottom: 20px; }
        .mcq-q { font-weight: bold; margin-bottom: 15px; font-size: 1.1rem; color: var(--text-main); }
        .mcq-opt { display: block; padding: 10px 15px; background: var(--bg-elevated); border: 1px solid var(--border); border-radius: 6px; margin-bottom: 8px; cursor: pointer; transition: all 0.2s; }
        .mcq-opt:hover { border-color: var(--primary); }
        .mcq-opt.selected { background: rgba(187, 134, 252, 0.2); border-color: var(--primary); }
        
        .mcq-ans-box { display: none; margin-top: 15px; padding: 15px; background: rgba(3, 218, 198, 0.1); border-left: 4px solid var(--secondary); border-radius: 4px; font-size: 0.95rem; }
        .mcq-ans-box.show { display: block; animation: fadeIn 0.3s; }
        .btn-reveal { background: var(--bg-elevated); border: 1px solid var(--border); color: var(--text-main); padding: 8px 15px; border-radius: 6px; cursor: pointer; margin-top: 10px; }
        .btn-reveal:hover { background: var(--border); }
        .meta-tags { display: flex; gap: 10px; margin-top: 10px; font-size: 0.8rem; }
        .meta-tag { background: var(--bg-elevated); padding: 3px 8px; border-radius: 4px; color: var(--text-muted); }

        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* Home grid */
        .home-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; margin-top: 30px; }
        .home-card { background-color: var(--bg-surface); border: 1px solid var(--border); border-radius: 8px; padding: 20px; cursor: pointer; transition: transform 0.2s; }
        .home-card:hover { transform: translateY(-5px); border-color: var(--primary); }
        
        @media (max-width: 768px) {
            body { flex-direction: column; }
            #sidebar { position: fixed; top: 0; left: -300px; height: 100vh; box-shadow: 2px 0 10px rgba(0,0,0,0.5); }
            #sidebar.open { transform: translateX(300px); }
            #topbar { display: flex; }
            #content-area { padding: 20px; }
        }
    </style>
</head>
<body>
    <div id="sidebar">
        <div id="sidebar-header">
            <h1>UGC NET Study Portal</h1>
            <div id="search-container">
                <input type="text" id="search-bar" placeholder="Search topics...">
            </div>
        </div>
        <div id="nav-links">
            <div class="nav-item active" data-target="home">🏠 Home</div>
            <div class="nav-section">Core</div>
            <div class="nav-item" data-target="conquest" style="color: var(--primary-variant); font-weight: bold;">🔥 4-Month Conquest Plan</div>
            <div class="nav-item" data-target="syllabus">Syllabus Master</div>
            <div class="nav-section">Anthropology Units</div>
            <div class="nav-item" data-target="unit_1">Unit 1 (Detailed Notes)</div>
            <div class="nav-item" data-target="unit_2">Unit 2</div>
            <div class="nav-item" data-target="unit_3">Unit 3</div>
            <div class="nav-item" data-target="unit_4">Unit 4</div>
            <div class="nav-item" data-target="unit_5">Unit 5</div>
            <div class="nav-item" data-target="unit_6">Unit 6</div>
            <div class="nav-item" data-target="unit_7">Unit 7</div>
            <div class="nav-item" data-target="unit_8">Unit 8</div>
            <div class="nav-item" data-target="unit_9">Unit 9</div>
            <div class="nav-item" data-target="unit_10">Unit 10</div>
            <div class="nav-section">Shortcuts</div>
            <div class="nav-item" data-target="cheatsheets">Cheat Sheets</div>
        </div>
    </div>

    <div id="main-content">
        <div id="scroll-progress"></div>
        <div id="topbar">
            <button id="menu-toggle">☰</button>
            <h2 style="margin: 0; font-size: 1.2rem; font-weight: 600;">Study Portal</h2>
            <div class="topbar-tools">
                <button class="icon-btn" id="theme-toggle" title="Toggle Dark/Light Mode">🌓</button>
            </div>
        </div>
        <div id="content-area"></div>
    </div>
    
    <div id="pomodoro-widget" class="dragging-disabled">
        <div>
            <div style="font-size: 0.75rem; color: var(--text-muted); text-transform:uppercase; letter-spacing:1px; font-weight:bold;">Focus Timer</div>
            <div id="pomodoro-time">25:00</div>
        </div>
        <div style="display:flex; flex-direction:column; gap:5px;">
            <button class="pomo-btn" id="pomo-play" title="Start/Pause">▶️</button>
            <button class="pomo-btn" id="pomo-reset" title="Reset">🔄</button>
        </div>
    </div>

    <script>
        const dbContent = /*CONTENT_JSON_REPLACE*/;
        const mockData = /*MOCK_DATA_REPLACE*/;

        function markStudied(btn) {
            btn.classList.toggle('studied');
            if(btn.classList.contains('studied')) btn.innerText = '✓ Studied';
            else btn.innerText = 'Mark as Studied';
        }

        function parseMarkdown(md) {
            if(!md) return "<i>No content available.</i>";
            let html = md;
            
            // Smart features tags to divs
            html = html.replace(/<div class="smart-feature(.*?)">/g, '<div class="smart-feature$1">');
            
            // Auto-Highlight Definitions (Sentences containing "is defined as", "refers to", etc)
            html = html.replace(/([^.]*?\\b(is defined as|refers to|known as|means|can be defined as|called)\\b[^.]*\\.)/gi, function(match) {
                if(match.includes('<') || match.includes('>')) return match; // skip if it contains HTML (like headers)
                return '<span class="highlight-definition">' + match + '</span>';
            });
            
            // Auto-Highlight Formulas
            html = html.replace(/(Formula:|Equation:)([^\\n]+)/gi, function(match) {
                return '<span class="highlight-formula">' + match + '</span>';
            });

            // List tags & bold (Concepts)
            html = html.replace(/\\*\\*(.*?)\\*\\*/g, '<strong class="highlight-concept">$1</strong>');
            html = html.replace(/\\*(.*?)\\*/g, '<em>$1</em>');
            html = html.replace(/^\\* (.*$)/gim, '<ul><li>$1</li></ul>');
            html = html.replace(/^\\- (.*$)/gim, '<ul><li>$1</li></ul>');
            html = html.replace(/<\\/ul>\\s*<ul>/g, ''); 
            
            // Tables
            html = html.replace(/\\|(.*?)\\|/g, function(match, inner) {
                if(inner.includes('---')) return '';
                let cells = inner.split('|').map(c => '<td>' + c.trim() + '</td>').join('');
                return '<tr>' + cells + '</tr>';
            });
            html = html.replace(/(<tr>.*<\\/tr>)/gsi, function(match) {
                return '<table><tbody>' + match + '</tbody></table>';
            });
            html = html.replace(/<\\/table>\\s*<table>/g, '');

            // Paragraphs
            html = html.split('\\n\\n').map(p => {
                if(p.trim().startsWith('<h') || p.trim().startsWith('<ul') || p.trim().startsWith('<div') || p.trim().startsWith('<table') || p.trim().startsWith('<span')) return p;
                return '<p>' + p.replace(/\\n/g, '<br>') + '</p>';
            }).join('\\n');
            
            // Headers with Mark Studied
            html = html.replace(/^(##+)\\s+(.*)$/gim, function(match, hashes, title) {
                let level = hashes.length;
                let btn = `<button class="btn-mark-studied" onclick="markStudied(this)">Mark as Studied</button>`;
                return `<h${level}>${title} ${btn}</h${level}>`;
            });

            // Target the PDF Supplementary Content specifically injected by extract_refined.py
            html = html.replace(/<div style='background: rgba\\(187, 134, 252, 0\\.05\\);[^>]*>/g, '<div class="pdf-supplementary-content">');
            
            // Aggressive Trimming & Auto-Highlighting Logic
            let tempDiv = document.createElement('div');
            tempDiv.innerHTML = html;
            
            // Define core high-yield Anthropology terminology
            const keywords = ['theory', 'evolution', 'kinship', 'society', 'culture', 'fossil', 'hominin', 'primate', 'archaeology', 'palaeolithic', 'lineage', 'genetics', 'methodology', 'ethnography', 'functionalism', 'structuralism', 'caste', 'tribe', 'marriage', 'family', 'descent', 'mutation', 'adaptation'];
            const keywordRegex = new RegExp(`\\\\b(${keywords.join('|')})\\\\b`, 'gi');
            
            let pdfSections = tempDiv.querySelectorAll('.pdf-supplementary-content');
            pdfSections.forEach(section => {
                let pTags = Array.from(section.querySelectorAll('p'));
                pTags.forEach(p => {
                    let text = p.innerHTML;
                    
                    // Trimming Logic: If it's a long paragraph but lacks BOTH keywords and scholarly names, delete it!
                    let capsRegex = /\\b([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)+)\\b/g;
                    let hasCaps = capsRegex.test(text);
                    let hasKeyword = keywordRegex.test(text);
                    
                    if (!hasCaps && !hasKeyword && text.split(' ').length > 15) {
                        p.remove();
                        return; // skip further processing
                    }
                    
                    // Contextual Sentence Highlighting Logic
                    // Split paragraph into sentences (basic regex: period followed by space or end of string)
                    let sentences = text.match(/[^.!?]+[.!?]+(?:\\s+|$)|[^.!?]+$/g) || [text];
                    let processedSentences = [];
                    
                    sentences.forEach(sentence => {
                        let isHighlighted = false;
                        let processedSentence = sentence;
                        
                        // If sentence contains a keyword, mark it for contextual highlighting
                        if (keywordRegex.test(sentence)) {
                            isHighlighted = true;
                            // Still bold the specific keywords within the highlighted sentence
                            processedSentence = processedSentence.replace(keywordRegex, function(match) {
                                if(match.includes('span') || match.includes('class')) return match; 
                                return '<strong class="pdf-keyword">' + match + '</strong>';
                            });
                        }
                        
                        // Always highlight capitalized phrases (Scholars/Theories) regardless
                        if (capsRegex.test(processedSentence)) {
                            processedSentence = processedSentence.replace(capsRegex, '<span class="pdf-highlight">$1</span>');
                        }
                        
                        // Wrap the entire sentence if it contained a keyword
                        if (isHighlighted) {
                            processedSentence = `<span class="pdf-context-highlight">${processedSentence.trim()}</span> `;
                        }
                        
                        processedSentences.push(processedSentence);
                    });
                    
                    p.innerHTML = processedSentences.join(' ');
                });
            });
            html = tempDiv.innerHTML;

            return html;
        }

        let attemptedMCQs = new Set();
        let totalMCQs = 0;

        function renderMCQs(mcqText) {
            if(!mcqText) return '';
            
            let blocks = mcqText.split(/Q\\d+\\./);
            let html = `<div class="mcq-container">
                <h2>Interactive MCQ Quiz</h2>
                <div class="progress-box">
                    <div style="display:flex; justify-content:space-between;">
                        <strong>Quiz Progress</strong>
                        <span id="mcq-score">0 / 0</span>
                    </div>
                    <div class="progress-bar"><div class="progress-fill" id="mcq-progress"></div></div>
                </div>
                <div id="mcq-list">
            `;
            
            blocks.shift(); // remove empty first split
            totalMCQs = blocks.length;
            attemptedMCQs.clear();

            blocks.forEach((block, index) => {
                let lines = block.trim().split('\\n').filter(l => l.trim().length > 0);
                let qText = lines[0];
                let opts = [];
                let ans = '', exp = '', diff = '', src = '';
                
                for(let i=1; i<lines.length; i++){
                    let line = lines[i];
                    if(line.startsWith('A)') || line.startsWith('B)') || line.startsWith('C)') || line.startsWith('D)')) opts.push(line);
                    else if(line.startsWith('Answer:')) ans = line.replace('Answer:', '').trim();
                    else if(line.startsWith('Explanation:')) exp = line.replace('Explanation:', '').trim();
                    else if(line.startsWith('Difficulty:')) diff = line.replace('Difficulty:', '').trim();
                    else if(line.startsWith('Source:')) src = line.replace('Source:', '').trim();
                }

                html += `<div class="mcq-card" id="q-${index}">
                    <div class="mcq-q">Q${index+1}. ${qText}</div>`;
                
                opts.forEach((opt, optIdx) => {
                    let optLetter = opt.substring(0, 1);
                    html += `<div class="mcq-opt" onclick="selectOpt(${index}, '${optLetter}', '${ans}')">${opt}</div>`;
                });

                html += `<button class="btn-reveal" onclick="revealAns(${index})">Reveal Answer</button>
                    <div class="mcq-ans-box" id="ans-${index}">
                        <strong>Correct Answer: ${ans}</strong>
                        <p style="margin:10px 0;">${exp}</p>
                        <div class="meta-tags">
                            <span class="meta-tag">Diff: ${diff}</span>
                            <span class="meta-tag">Src: ${src}</span>
                        </div>
                    </div>
                </div>`;
            });
            html += `</div></div>`;
            return html;
        }

        window.selectOpt = function(qIndex, selected, correct) {
            let card = document.getElementById(`q-${qIndex}`);
            // visually select
            let opts = card.querySelectorAll('.mcq-opt');
            opts.forEach(o => o.classList.remove('selected'));
            event.target.classList.add('selected');

            if(!attemptedMCQs.has(qIndex)) {
                attemptedMCQs.add(qIndex);
                updateProgress();
            }
        };

        window.revealAns = function(qIndex) {
            document.getElementById(`ans-${qIndex}`).classList.add('show');
            if(!attemptedMCQs.has(qIndex)) {
                attemptedMCQs.add(qIndex);
                updateProgress();
            }
        };

        function updateProgress() {
            let count = attemptedMCQs.size;
            document.getElementById('mcq-score').innerText = `${count} / ${totalMCQs} Attempted`;
            document.getElementById('mcq-progress').style.width = `${(count/totalMCQs)*100}%`;
        }

        const area = document.getElementById('content-area');

        function loadContent(target) {
            // Unset toggle state
            document.body.classList.remove('quick-revision-mode');

            let html = '';
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            const activeEl = document.querySelector(`.nav-item[data-target="${target}"]`);
            if(activeEl) activeEl.classList.add('active');

            if (target === 'home') {
                html = `
                    <h1>Welcome to UGC NET Study Portal</h1>
                    <div class="home-grid">
                        <div class="home-card" onclick="loadContent('conquest')" style="border-color: var(--primary); background: rgba(200,146,42,0.05);">
                            <h3>🔥 Conquest Plan</h3><p>Complete 4-Month Road Map</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_1')">
                            <h3>Unit 1</h3><p>Meaning & Scope of Anthropology</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_2')">
                            <h3>Unit 2</h3><p>Evolution & Primatology Notes</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_3')">
                            <h3>Unit 3</h3><p>Archaeological Anthropology</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_4')">
                            <h3>Unit 4</h3><p>Social/Cultural Anthropology</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_5')">
                            <h3>Unit 5</h3><p>Human Genetics</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_6')">
                            <h3>Unit 6</h3><p>Anthropological Theories</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_7')">
                            <h3>Unit 7</h3><p>Indian Society and Culture</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_8')">
                            <h3>Unit 8</h3><p>Tribal Situation in India</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_9')">
                            <h3>Unit 9</h3><p>Applied and Action Anthropology</p>
                        </div>
                        <div class="home-card" onclick="loadContent('unit_10')">
                            <h3>Unit 10</h3><p>Research Methods</p>
                        </div>
                        <div class="home-card" onclick="loadContent('cheatsheets')">
                            <h3>Cheat Sheets</h3><p>Quick reference for vital topics</p>
                        </div>
                    </div>
                `;
            } else if (target === 'syllabus') {
                html = '<div class="syllabus-master-container" style="animation: fadeIn 0.3s ease-out;">';
                if(dbContent['Syllabus_Master.md']) html += parseMarkdown(dbContent['Syllabus_Master.md']);
                else html += '<i>Syllabus_Master.md not found in the database.</i>';
                html += '</div>';
            } else if (target === 'cheatsheets') {
                html = '<h1>Cheat Sheets</h1>';
                if(dbContent['Research_Methodology_CheatSheet.md']) html += parseMarkdown(dbContent['Research_Methodology_CheatSheet.md']);
            } else if (target === 'conquest') {
                let p = dbContent['Conquest_Plan.html'] || '<i>Plan not found. Please ensure Conquest_Plan.html is present.</i>';
                let bodyMatch = p.match(/<body[^>]*>([\s\S]*)<\/body>/i);
                
                html = '<div class="conquest-container">' + (bodyMatch ? bodyMatch[1] : p) + '</div>';
                
                // Add the specific styles scoped so they don't break the rest of the app
                let styleMatch = p.match(/<style>([\s\S]*?)<\/style>/i);
                if (styleMatch) {
                    let styles = styleMatch[1];
                    // Scope global resets and body styles to our container
                    styles = styles.replace(/\*\s*{([^}]*)}/g, '.conquest-container * { $1 }');
                    styles = styles.replace(/body\s*{([^}]*)}/g, '.conquest-container { $1 }');
                    styles = styles.replace(/:root\s*{([^}]*)}/g, '.conquest-container { $1 }');
                    
                    // Fix horizontal scrolling and stickiness
                    styles += `
                    .conquest-container {
                        overflow-x: hidden;
                        padding-top: 10px;
                        margin: -40px; /* Counteract #content-area padding */
                    }
                    .conquest-container .sticky-nav {
                        position: sticky;
                        top: 0;
                        z-index: 100;
                    }
                    .conquest-container .nav-inner {
                        padding-bottom: 5px; /* prevent scrollbar clipping */
                        -webkit-mask-image: linear-gradient(to right, black 90%, transparent);
                        mask-image: linear-gradient(to right, black 90%, transparent);
                    }
                    `;
                    html = '<style>' + styles + '</style>' + html;
                }
            } else if (target.startsWith('unit_')) {
                const unitNum = target.split('_')[1];
                html = '<button id="toggle-revision" onclick="document.body.classList.toggle(\\'quick-revision-mode\\')">⚡ Toggle Quick Revision</button>';
                
                // Content
                const sumKey = `Unit_${unitNum}/Summary.md`;
                if(dbContent[sumKey]) {
                    html += parseMarkdown(dbContent[sumKey]);
                } else {
                    html += `<h1>Unit ${unitNum}</h1><i>No Summary.md found.</i>`;
                }
                
                // MCQs
                const mcqKey = `Unit_${unitNum}/Unit${unitNum}_MCQs.txt`;
                if(dbContent[mcqKey]) {
                    html += renderMCQs(dbContent[mcqKey]);
                }
            }

            area.innerHTML = html;
            document.getElementById('main-content').scrollTop = 0;
            if(window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        loadContent('unit_1'); // default to unit 1 to show off new features

        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', () => loadContent(item.getAttribute('data-target')));
        });
        document.getElementById('menu-toggle').addEventListener('click', () => {
             document.getElementById('sidebar').classList.toggle('open');
        });

        // Theme Toggle
        document.getElementById('theme-toggle').addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
            localStorage.setItem('theme', document.body.classList.contains('light-theme') ? 'light' : 'dark');
        });
        if(localStorage.getItem('theme') === 'light') {
            document.body.classList.add('light-theme');
        }

        // Scroll Progress
        const mainContentEl = document.getElementById('main-content');
        const scrollBar = document.getElementById('scroll-progress');
        mainContentEl.addEventListener('scroll', () => {
            let scrollTop = mainContentEl.scrollTop;
            let scrollHeight = mainContentEl.scrollHeight - mainContentEl.clientHeight;
            let progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
            scrollBar.style.width = progress + '%';
        });

        // Pomodoro Timer
        let pomoTime = 25 * 60;
        let pomoInterval = null;
        let pomoRunning = false;
        const pomoTimeEl = document.getElementById('pomodoro-time');
        const pomoPlayBtn = document.getElementById('pomo-play');

        function updatePomoDisplay() {
            let m = Math.floor(pomoTime / 60).toString().padStart(2, '0');
            let s = (pomoTime % 60).toString().padStart(2, '0');
            pomoTimeEl.innerText = `${m}:${s}`;
            document.title = `${m}:${s} - FocusTimer`;
        }
        
        document.getElementById('pomo-play').addEventListener('click', () => {
            if(pomoRunning) {
                clearInterval(pomoInterval);
                pomoRunning = false;
                pomoPlayBtn.innerText = '▶️';
                document.title = `UGC NET Anthropology Portal`;
            } else {
                pomoRunning = true;
                pomoPlayBtn.innerText = '⏸️';
                pomoInterval = setInterval(() => {
                    if(pomoTime > 0) {
                        pomoTime--;
                        updatePomoDisplay();
                    } else {
                        clearInterval(pomoInterval);
                        pomoRunning = false;
                        pomoPlayBtn.innerText = '▶️';
                        pomoTime = 5 * 60; // 5 min break
                        updatePomoDisplay();
                        alert('Focus session complete! Taking a 5 minute break.');
                    }
                }, 1000);
            }
        });
        
        document.getElementById('pomo-reset').addEventListener('click', () => {
            clearInterval(pomoInterval);
            pomoRunning = false;
            pomoTime = 25 * 60;
            pomoPlayBtn.innerText = '▶️';
            document.title = `UGC NET Anthropology Portal`;
            updatePomoDisplay();
        });

    </script>
</body>
</html>
"""

# Replace placeholders
# Need to escape </script> to prevent the browser from closing the script tag early when parsing JSON
content_json = json.dumps(content_dict).replace('</script>', '<\\/script>')
mock_data_json = json.dumps(mock_data_output).replace('</script>', '<\\/script>')

final_html = html_template.replace('/*CONTENT_JSON_REPLACE*/', content_json)
final_html = final_html.replace('/*MOCK_DATA_REPLACE*/', mock_data_json)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html generated successfully!")
