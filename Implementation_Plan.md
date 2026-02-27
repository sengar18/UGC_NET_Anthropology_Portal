# PDF Integration Implementation Plan

## 📌 Overview
This plan outlines how the 20+ anthropological PDF files discovered in `Folder_1` and `Folder_2` will be mapped and integrated into the `anthropology.html` (or `index.html`) study portal. 
*Note: Folder_1 and Folder_2 contain identical sets of PDFs. One non-anthropology PDF (Indium selenides) has been excluded.*

## 🗺️ Mapping Strategy

### 🟢 Unit 1: Meaning and Scope of Anthropology
1. **BLOCK 1.pdf**
   * *Theme*: Introduction to Biological Anthropology.
   * *Summary*: Defines the fundamental scope and applications of biological anthropology. It explores the holistic relationship between human biology and cultural environments.
2. **Unit-1.pdf**
   * *Theme*: Concept of Society and Culture.
   * *Summary*: Investigates the core definitions and elements of human society and culture. It establishes the foundational sociological concepts necessary for anthropological study.

### 🟢 Unit 2: Evolution and Primatology
3. **MANI-002B3E.pdf**
   * *Theme*: Primate Study and Phylogeny.
   * *Summary*: Details the classification, anatomy, and behavior of living primates. It traces their phylogenetic relationships to understand early human evolutionary pathways.

### 🟢 Unit 3: Archaeological Anthropology
4. **MAN-002B5E.pdf**
   * *Theme*: Palaeolithic Cultures.
   * *Summary*: Chronicles the progression of Lower, Middle, and Upper Palaeolithic cultures. It analyzes the development of prehistoric art and early human survival strategies.
5. **Unit-4 (1).pdf**
   * *Theme*: Dating Methods.
   * *Summary*: Compares relative and absolute chronometric dating methods. It covers critical techniques like stratigraphy, radiocarbon, and potassium-argon dating utilized in archaeology.
6. **Unit-8.pdf**
   * *Theme*: Prehistoric Typology.
   * *Summary*: Categorizes prehistoric stone tools across the Palaeolithic, Mesolithic, and Neolithic periods. It also examines early ceramic typologies and firing techniques.

### 🟢 Unit 4: Social and Cultural Anthropology
7. **BLOCK 2.pdf**
   * *Theme*: Introduction to Social and Cultural Anthropology.
   * *Summary*: Introduces the foundational concepts governing human social organization. It provides a broad overview of cultural dynamics and social structures.
8. **residence-and-kinship.pdf**
   * *Theme*: Marital Residence and Kinship by Ember.
   * *Summary*: Cross-culturally analyzes rules of descent, kinship terminology, and post-marital residence patterns. It explores the predictors and consequences of living arrangements like patrilocality and matrilocality.
9. **Unit-3.pdf**
   * *Theme*: Kinship Systems.
   * *Summary*: Explores complex kin relations including moieties, phratries, and clans. It details specific kinship usages like avoidance relationships and the avunculate.
10. **Unit-5.pdf**
   * *Theme*: Alliance Theory.
   * *Summary*: Discusses marriage as a systematic form of exchange across cultures. It heavily references Levi-Strauss's structuralist interpretations of elementary kinship and Dravidian marriage rules.
11. **Unit-1 (1).pdf**
   * *Theme*: Concepts of Religion.
   * *Summary*: Categorizes early religious beliefs such as animism, animatism, and totemism. It breaks down anthropological approaches to understanding magic, witchcraft, and religious symbolism.
12. **Unit7.pdf**
   * *Theme*: Economic and Political Institutions.
   * *Summary*: Reviews the functioning of bands, tribes, chiefdoms, and state-level societies. It bridges these political structures with their corresponding systems of economic production and exchange.

### 🟢 Unit 5: Human Genetics and Physical Anthropology
13. **MANE-001-B1.pdf**
   * *Theme*: Introduction to Human Genetics.
   * *Summary*: Outlines the biological basis of human heredity and formal genetics. It establishes the cellular mechanisms bridging genetic inheritance to physical variability.
14. **Unit--3.pdf**
   * *Theme*: Dermatoglyphics.
   * *Summary*: Analyzes the fundamental principles of fingerprint classification, including loops, whorls, and arches. It discusses the utility of palmar dermatoglyphics for personal identification.
15. **Unit-11.pdf**
   * *Theme*: Somatotyping and Human Physique.
   * *Summary*: Evaluates historical methods of body classification such as those developed by Sheldon, Kretschmer, and Heath-Carter. It examines how phenotypic expressions of body shape vary across human populations.
16. **Unit-2.pdf**
   * *Theme*: Stages of Human Growth.
   * *Summary*: Tracks the biological progression from prenatal development through senescence. It discusses normal growth variations and secular trends in human physical maturation.

### 🟢 Unit 6: Anthropological Theories
17. **112.pdf**
   * *Theme*: Symbolic Functionalism.
   * *Summary*: Compares the approaches of Clifford Geertz and Victor Turner in interpreting cultural symbols. It explores how symbolic interactionism and folklore construct communal meaning.
18. **Block-3.pdf**
   * *Theme*: Anthropological Theories I.
   * *Summary*: Surveys classical evolutionary theories alongside functionalism and structural-functionalism. It highlights the shifting paradigms of analyzing social organization dynamically.

### 🟢 Unit 9: Applied and Action Anthropology
19. **Unit-1 (2).pdf**
   * *Theme*: History of Applied Anthropology.
   * *Summary*: Analyzes the historical divergence of applied anthropology from pure theory. It explores how anthropological knowledge is practically utilized in administration and development, particularly in India.

### 🟢 Unit 10: Research Methods
20. **Block-4.pdf**
   * *Theme*: Approaches to Anthropological Research.
   * *Summary*: Details fundamental ethnographic methodologies including holistic, emic, and etic approaches. It emphasizes the importance of comparative and historical frameworks in fieldwork.

## ⚙️ Execution Plan
1. I will parse `generate_html.py`.
2. For each Unit section in the Python script's `units_data` (and Unit 1-3's separate text blocks), I will dynamically insert the formatted HTML blocks containing the `<h3>` titles and `<p class="unit-description">` summaries exactly where the relevant unit content begins.
3. I will regenerate `index.html` to apply the updates visually.

**Please review this plan. If you approve, I will proceed with updating the code!**
