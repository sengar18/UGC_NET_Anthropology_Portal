import os

pdf_mappings = {
    1: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">BLOCK 1.pdf & Unit-1.pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Defines the fundamental scope and applications of biological anthropology. It explores the holistic relationship between human biology and cultural environments. Investigates the core definitions and elements of human society and culture establishing foundational sociological concepts.</p>
</div>
""",
    2: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">MANI-002B3E.pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Details the classification, anatomy, and behavior of living primates. It traces their phylogenetic relationships to understand early human evolutionary pathways.</p>
</div>
""",
    3: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">MAN-002B5E.pdf, Unit-4 (1).pdf & Unit-8.pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Chronicles the progression of Palaeolithic cultures and examines prehistoric art. Compares relative and absolute chronometric dating methods. It categorizes prehistoric stone tools across periods and examines early ceramic typologies.</p>
</div>
""",
    4: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">residence-and-kinship.pdf, Unit-3.pdf, Unit-5.pdf, BLOCK 2.pdf, Unit-1 (1).pdf & Unit7.pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Cross-culturally analyzes rules of descent, kinship terminology, and post-marital residence patterns. It explores complex kin relations including moieties and clans, alongside Levi-Strauss's alliance theory. Breaks down anthropological approaches to understanding religion, magic, and political institutions like bands and chiefdoms.</p>
</div>
""",
    5: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">MANE-001-B1.pdf, Unit--3.pdf, Unit-11.pdf & Unit-2.pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Outlines the biological basis of human heredity and formal genetics. Analyzes fingerprint classification (dermatoglyphics) for personal identification. Evaluates Sheldon and Heath-Carter's methods of tracking human growth and body shape across human populations.</p>
</div>
""",
    6: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">112.pdf & Block-3.pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Compares the approaches of Clifford Geertz and Victor Turner in interpreting cultural symbols. Surveys classical evolutionary theories alongside functionalism, highlighting shifting paradigms.</p>
</div>
""",
    9: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">Unit-1 (2).pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Analyzes the historical divergence of applied anthropology from pure theory. It explores how anthropological knowledge is practically utilized in administration and development policy.</p>
</div>
""",
    10: """
<div class="pdf-summary-container" style="background: rgba(30,41,59,0.5); border-left: 4px solid var(--secondary); padding: 15px; margin: 20px 0; border-radius: 6px;">
    <h2 style="font-size: 1.2rem; margin-top: 0; color: var(--text-main); border-bottom: none;">📚 Associated PDF Resources</h2>
    <h3 style="margin-top: 10px; margin-bottom: 5px; color: var(--primary-variant);">Block-4.pdf</h3>
    <p class="unit-description" style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0;">Details fundamental ethnographic methodologies including holistic, emic, and etic approaches. Emphasizes the importance of comparative and historical frameworks in fieldwork.</p>
</div>
"""
}

for unit_num, html_block in pdf_mappings.items():
    filepath = rf"Unit_{unit_num}\Summary.md"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        injected = False
        for line in lines:
            new_lines.append(line)
            if line.startswith('# Unit ') and not injected:
                new_lines.append("\n" + html_block + "\n")
                injected = True
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

print("PDF summaries successfully injected into Summary.md files!")
