import os

high_value_topics = {
    1: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>Biological Anthropology Foundations:</b> Definition, scope, and key subfields (Human Genetics, Paleoanthropology).</li>
    <li><b>Human-Environment Linkages:</b> Holistic relationship between human biological adaptation and cultural environments.</li>
    <li><b>Society vs. Culture:</b> Fundamental characteristics, distinctions, and symbiotic evolution.</li>
    <li><b>Early Anthropological Theory:</b> Principles of Evolutionary, Psychological, and Marxist approaches to culture.</li>
</ul>
</div>
""",
    2: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>Primate Taxonomy:</b> Living primates classification, characteristics of Prosimians vs. Anthropoids.</li>
    <li><b>Primate Behavior:</b> Social organization, mating patterns, territoriality, and troop communication.</li>
    <li><b>Evolutionary Phylogeny:</b> Fossil record progression of early prosimians, pongids, and protohominids.</li>
    <li><b>Comparative Anatomy:</b> Detailed structural comparison of Humans vs. Great Apes (Cranial capacity, spine curvature, pelvic girdle).</li>
</ul>
</div>
""",
    3: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>Chronometric Dating:</b> Absolute methods (C-14, K-Ar) vs. Relative methods (Stratigraphy, Fluorine/FUN Analysis).</li>
    <li><b>Palaeolithic Industries:</b> Lower (Oldowan/Acheulian), Middle (Mousterian flake tools), and Upper (Prismatic core blades/bone tools).</li>
    <li><b>Pleistocene Epoch:</b> Glacial and interglacial sequences and human adaptation.</li>
    <li><b>Prehistoric Typology:</b> Evolution of stone tool technology, Microliths transition, and early ceramic characteristics.</li>
</ul>
</div>
""",
    4: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>Kinship & Descent:</b> Unilineal descent calculation, lineage vs. clan, and formal kinship terminology systems.</li>
    <li><b>Marriage & Alliance Theory:</b> Levi-Strauss complex structures, rules of exogamy, and incest taboos.</li>
    <li><b>Post-Marital Residence:</b> Predictors and consequences of Patrilocal, Matrilocal, and Neolocal residency.</li>
    <li><b>Religious Institutions:</b> Concepts of Animism, Totemism, Shamanism, witchcraft, and the sacred vs. profane division.</li>
    <li><b>Political Entities:</b> Evolution and power dynamics in Bands, Tribes, Chiefdoms, and State societies.</li>
</ul>
</div>
""",
    5: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>Human Genetics:</b> Biological basis of heredity, chromosomal organization, and formal genetics framework.</li>
    <li><b>Dermatoglyphics:</b> Fundamental identification principles, classification of Arches, Loops, and Whorls (Galton system).</li>
    <li><b>Somatotyping:</b> Methods of human physique assessment comparing Sheldon, Parnell, and Heath-Carter models.</li>
    <li><b>Human Growth Dynamics:</b> Prenatal/Postnatal stages, canalization, catch-up growth, and secular trends in modern populations.</li>
</ul>
</div>
""",
    6: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>Symbolic Anthropology:</b> The distinct frameworks and methodologies of Clifford Geertz vs. Victor Turner.</li>
    <li><b>Structural Functionalism:</b> Core dynamic theories bridging social organization and function.</li>
    <li><b>Classical Evolutionary Theories:</b> The 19th-century intellectual impact on defining culture and societal progression.</li>
    <li><b>Folklore & Anthropology:</b> Anthropological intersections in studying myth, folklore, and ritual symbolism.</li>
</ul>
</div>
""",
    9: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>History of Applied Anthropology:</b> Origins, development, and separation from purely academic frameworks.</li>
    <li><b>Practical Applications:</b> Role in colonial administration, healthcare interventions, and public policy formulation.</li>
    <li><b>Indian Context:</b> Utilization of anthropological data for post-independence tribal development and indigenous planning.</li>
    <li><b>Action Anthropology:</b> Sol Tax's methodology of integrating field research with community advocacy and problem-solving.</li>
</ul>
</div>
""",
    10: """
## 🎯 High-Yield Topics from Associated PDFs
<div class="smart-feature highlight-box" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
<ul>
    <li><b>Ethnographic Approach:</b> Core principles of participant observation and in-depth fieldwork strategies.</li>
    <li><b>Emic vs. Etic Frameworks:</b> Grasping the insider's (subjective) perspective versus the outsider's (objective) scientific classification.</li>
    <li><b>Holistic Research:</b> Recognizing the interconnectedness of cultural, economic, and political institutions.</li>
    <li><b>Research Design:</b> Structuring anthropological inquiry, hypotheses formulation, and comparative/historical methods.</li>
</ul>
</div>
"""
}

for unit_num, content in high_value_topics.items():
    summary_path = rf"C:\Users\ashis\Downloads\UGC_NET_Anthropology\Unit_{unit_num}\Summary.md"
    if os.path.exists(summary_path):
        with open(summary_path, 'r', encoding='utf-8') as f:
            old_content = f.read()
            
        # Ensure we don't duplicate
        if "## 🎯 High-Yield Topics from Associated PDFs" not in old_content:
            with open(summary_path, 'a', encoding='utf-8') as f:
                f.write("\n" + content)

print("Injected High-Yield Topics into Summary.md files!")
