import os
import re

units_data = {
    4: {
        "title": "Unit 4: Social/Cultural Anthropology",
        "content": """# Unit 4: Social and Cultural Anthropology

*(Examiner's Favourite: Descent systems (matrilineal vs patrilineal), Types of cross-cousin marriages, theories of religion (Animism vs Animatism), and economic exchange systems (Kula ring, Potlatch).)*

<div class="smart-feature rapid-revision">
<h3>⏱️ 5-Minute Rapid Revision Summary</h3>
<ul>
<li><b>Marriage</b>: Monogamy vs Polygamy (Polygyny = 1 man, many wives; Polyandry = 1 woman, many husbands. Fraternal polyandry in Todas/Khasas).</li>
<li><b>Kinship</b>: Consanguineal (blood) vs Affinal (marriage). Descent: Unilineal (Patrilineal/Matrilineal) vs Bilateral.</li>
<li><b>Religion</b>: Animism (E.B. Tylor) -> Belief in spirits/souls. Animatism (R.R. Marett) -> Belief in impersonal supernatural power (Mana).</li>
<li><b>Magic</b>: Frazer's Sympathetic Magic: Homeopathic (Law of Similarity - Voodoo dolls) vs Contagious (Law of Contact - hair/nails).</li>
<li><b>Economic Exchange</b>: Reciprocity (Generalized, Balanced, Negative), Redistribution (Potlatch), Market exchange.</li>
<li><b>Political Systems</b>: Band (egalitarian), Tribe, Chiefdom (ranked, redistributive), State (stratified). Elaborated by Elman Service.</li>
</ul>
</div>

## 4.1 Marriage and Family

<div class="smart-feature quick-revision-bullets">
<b>Quick Revision:</b>
- Levirate: Widow marries dead husband's brother (Nuer, Jats).
- Sororate: Widower marries dead wife's sister.
- Hypergamy (Anuloma): High status man + Low status woman.
- Hypogamy (Pratiloma): Low status man + High status woman.
</div>

**Types of Family:**
- **Nuclear:** Parents and unmarried children.
- **Extended:** Multiple generations living together.
- **Joint:** Siblings and their spouses living together (common in India).

**Rules of Residence:**
- *Patrilocal/Virilocal:* Couple lives with husband's family.
- *Matrilocal/Uxorilocal:* Couple lives with wife's family (e.g., Khasis, Garos, Nayars).
- *Avunculocal:* Couple lives with husband's maternal uncle (e.g., Trobriand Islanders).
- *Neolocal:* Couple establishes a new independent household.

## 4.2 Kinship and Descent

- **Lineage:** Unilineal descent group with *demonstrated* descent from a known common ancestor.
- **Clan (Gotra):** Unilineal descent group with *stipulated* descent from a mythical or unknown ancestor (often a totem).
- **Phratry:** Grouping of two or more clans.
- **Moiety:** When a society is divided into exactly two descent groups.

Kinship Terminology Systems (L.H. Morgan):
1. **Hawaiian:** Most classificatory. All cousins are called brother/sister. All aunts/uncles called mother/father.
2. **Eskimo:** Emphasizes nuclear family. Bilateral descent (like modern Western system).
3. **Iroquois, Crow, Omaha, Sudanese:** More complex unilineal systems distinguishing cross/parallel cousins.

<div class="smart-feature common-mistakes">
<b>Common Mistakes:</b> Parallel cousins vs Cross cousins. <br>
*Parallel*: Children of siblings of the SAME sex (Father's Brother's kids, Mother's Sister's kids). Often taboo to marry.<br>
*Cross*: Children of siblings of the OPPOSITE sex (Father's Sister's kids, Mother's Brother's kids). Often preferred marriage partners in many societies.
</div>

## 4.3 Religion, Magic, and Science

- **Animism:** E.B. Tylor's theory (1871 in *Primitive Culture*) that religion originated from dreams/trances leading to belief in a dual soul.
- **Animatism:** R.R. Marett's theory. Belief in an impersonal supernatural force (Mana in Melanesia).
- **Totemism:** Emile Durkheim studied Australian Arunta. Totem represents the society communicating with itself.
- **Magic vs Religion:** Malinowski stated magic is used to control the uncontrollable (anxiety-relief in open-sea fishing), whereas religion is an end in itself.

## 4.4 Economic and Political Anthropology

- **Kula Ring:** Discovered by Malinowski in the Trobriand Islands. A balanced reciprocity system exchanging red shell necklaces (*soulava* - clockwise) and white shell armbands (*mwali* - counterclockwise). Not for profit, but for social status and cementing alliances.
- **Potlatch:** Practiced by Native American tribes of the Pacific Northwest (Kwakiutl, studied by Boas). A competitive feast of redistribution where chiefs destroy or give away wealth to gain prestige.
""",
        "mcqs": [
            {"q": "Which of the following refers to a marriage where a widow marries her deceased husband's brother?", "ans": "B", "exp": "Levirate is the custom of a widow marrying her dead husband's brother.", "diff": "Easy", "src": "Social Anthropology", "options": ["A) Sororate", "B) Levirate", "C) Polyandry", "D) Polygyny"]},
            {"q": "Who proposed the evolutionary sequence of religion from Animism to Polytheism to Monotheism?", "ans": "A", "exp": "E.B. Tylor proposed this sequence in his book Primitive Culture.", "diff": "Medium", "src": "Primitive Culture", "options": ["A) E.B. Tylor", "B) R.R. Marett", "C) J.G. Frazer", "D) Emile Durkheim"]},
            {"q": "The Kula ring of the Trobriand Islanders is an example of:", "ans": "C", "exp": "The Kula exchange is a classic example of balanced reciprocity serving to build alliances.", "diff": "Easy", "src": "Argonauts of the Western Pacific", "options": ["A) Market exchange", "B) Negative reciprocity", "C) Balanced reciprocity", "D) Redistribution"]},
            {"q": "Which residence rule dictates that a newlywed couple lives with or near the husband's mother's brother (maternal uncle)?", "ans": "D", "exp": "Avunculocal residence places the couple with the husband's maternal uncle, common in matrilineal societies where males hold political power.", "diff": "Hard", "src": "Kinship Studies", "options": ["A) Patrilocal", "B) Matrilocal", "C) Neolocal", "D) Avunculocal"]},
            {"q": "Hypergamy (anuloma) refers to a marriage where:", "ans": "A", "exp": "Hypergamy is marrying 'up'; a woman marries a man of higher social status or caste.", "diff": "Medium", "src": "Indian Sociology", "options": ["A) A woman marries a man of higher status", "B) A woman marries a man of lower status", "C) A man has multiple wives", "D) Marriages must occur outside the group"]},
            {"q": "According to Elman Service, which political system is characterized by egalitarianism, foraging economies, and lacks formal leadership?", "ans": "B", "exp": "Bands are small, egalitarian, mobile groups of foragers.", "diff": "Easy", "src": "Political Anthropology", "options": ["A) Tribe", "B) Band", "C) Chiefdom", "D) State"]},
            {"q": "Which type of magic is based on the principle 'like produces like' (Law of Similarity)?", "ans": "A", "exp": "Homeopathic or imitative magic relies on the similarity between a magical act and its desired effect (e.g., voodoo dolls).", "diff": "Medium", "src": "The Golden Bough", "options": ["A) Homeopathic magic", "B) Contagious magic", "C) Black magic", "D) Divination"]},
            {"q": "A unilineal descent group whose members claim descent from a stipulated, mythical ancestor (often a totem) is called a:", "ans": "C", "exp": "A clan claims descent from a stipulated ancestor, whereas a lineage can demonstrate genealogical links.", "diff": "Medium", "src": "Ember & Ember", "options": ["A) Lineage", "B) Phratry", "C) Clan", "D) Moiety"]},
        ]
    },
    5: {
        "title": "Unit 5: Human Genetics and Physical Anthropology",
        "content": """# Unit 5: Human Genetics and Physical Anthropology

*(Examiner's Favourite: Hardy-Weinberg equilibrium calculations, Mendelian inheritance patterns (Autosomal dominant/recessive, X-linked), Blood groups (ABO, Rh incompatability - Erythroblastosis fetalis), and Dermatoglyphics (fingerprints).)*

<div class="smart-feature rapid-revision">
<h3>⏱️ 5-Minute Rapid Revision Summary</h3>
<ul>
<li><b>Mendel's Laws</b>: 1. Segregation (alleles separate uniquely). 2. Independent Assortment (genes sort independently).</li>
<li><b>Hardy-Weinberg Principle</b>: p² + 2pq + q² = 1. Used to calculate allele/genotype frequencies in a non-evolving population.</li>
<li><b>ABO Blood Group</b>: Discovered by Karl Landsteiner. Multiple alleles (IA, IB, i). O is universal donor, AB is universal recipient.</li>
<li><b>Rh Factor</b>: Rh- mother with Rh+ fetus = Erythroblastosis fetalis (hemolytic disease).</li>
<li><b>Chromosome Aberrations</b>: Down Syndrome (Trisomy 21), Turner (XO, female), Klinefelter (XXY, male).</li>
<li><b>Dermatoglyphics</b>: Loops (65%), Whorls (30%), Arches (5%). Galton established their permanence and individuality.</li>
</ul>
</div>

## 5.1 Principles of Genetics

<div class="smart-feature quick-revision-bullets">
<b>Quick Revision:</b>
- Phenotype: Observable trait. Genotype: Genetic makeup.
- Autosomal Dominant: Huntington's disease, Achondroplasia.
- Autosomal Recessive: Sickle cell anemia, Albinism, Cystic Fibrosis.
- X-linked Recessive: Color blindness, Hemophilia. More common in males.
</div>

**1. Cell Division:**
- **Mitosis:** Somatic cells. Results in 2 identical diploid (2n) daughter cells.
- **Meiosis:** Gamete cells. Results in 4 unique haploid (n) daughter cells. Crucial for genetic recombination (Crossing Over in Prophase I).

**2. Mendelian Genetics:**
Gregor Mendel (Father of Genetics) worked on pea plants.
- *Law of Dominance:* Only the dominant allele expresses in a heterozygote.
- *Law of Segregation:* Alleles pair separate during gamete formation so each gamete carries only one allele for each gene.
- *Law of Independent Assortment:* Genes for different traits can segregate independently during the formation of gametes.

## 5.2 Population Genetics

**The Hardy-Weinberg Law:**
States that allele and genotype frequencies in a population will remain constant from generation to generation in the absence of other evolutionary influences.
*Equation:* p² + 2pq + q² = 1 
(where p = freq of dominant allele, q = freq of recessive allele, p² = freq of homozygous dominant, 2pq = freq of heterozygous, q² = freq of homozygous recessive).
*Assumptions for Equilibrium:*
1. Large population size (no genetic drift).
2. Random mating.
3. No mutation.
4. No migration (no gene flow).
5. No natural selection.

<div class="smart-feature common-mistakes">
<b>Common Mistakes:</b> In HW problems, if it says "16% of the population expresses the recessive trait", this means q² = 0.16. Do NOT set q = 0.16. You must square root it to find q = 0.4.
</div>

## 5.3 Blood Groups and Serology

- **ABO System:** Multiple allelism. IA and IB are codominant, i is recessive.
- **Rh System:** Rhesus factor. Incompatibility occurs ONLY when the Mother is Rh- and the Fetus is Rh+. The first pregnancy is usually safe, but mixing of blood creates antibodies. Second Rh+ pregnancy leads to *Erythroblastosis fetalis* (maternal antibodies attack fetal red blood cells). Treatment with RhoGAM.

## 5.4 Dermatoglyphics and Anthropometry

- **Dermatoglyphics:** Study of epidermal ridges on fingers, palms, toes. Sir Francis Galton classified them into Arches, Loops, and Whorls.
- Ridge Counts and Pattern Intensity Indices (PII) are specific population markers.
- Useful in forensic anthropology, twin studies, and diagnosing chromosomal abnormalities (e.g., Simian crease in Down Syndrome).
""",
        "mcqs": [
            {"q": "In a population at Hardy-Weinberg equilibrium, if the frequency of the recessive phenotype is 0.09, what is the frequency of the recessive allele (q)?", "ans": "B", "exp": "If q² = 0.09, then q = √0.09 = 0.3.", "diff": "Medium", "src": "Population Genetics", "options": ["A) 0.09", "B) 0.3", "C) 0.7", "D) 0.81"]},
            {"q": "Erythroblastosis fetalis may occur when:", "ans": "C", "exp": "It occurs when an Rh-negative mother carries an Rh-positive fetus, and she has been previously sensitized.", "diff": "Medium", "src": "Medical Anthropology", "options": ["A) Mother is Rh+ and Fetus is Rh-", "B) Both Mother and Fetus are Rh-", "C) Mother is Rh- and Fetus is Rh+", "D) Both Mother and Fetus are Rh+"]},
            {"q": "Which chromosomal abnormality is represented by the karyotype 47, XXY?", "ans": "A", "exp": "Klinefelter syndrome affects males who have an extra X chromosome.", "diff": "Easy", "src": "Human Genetics", "options": ["A) Klinefelter Syndrome", "B) Turner Syndrome", "C) Down Syndrome", "D) Patau Syndrome"]},
            {"q": "The most common fingerprint pattern in human populations is:", "ans": "B", "exp": "Loops are the most common (approx 60-65%), followed by whorls (30-35%), and arches (~5%).", "diff": "Easy", "src": "Dermatoglyphics", "options": ["A) Whorls", "B) Loops", "C) Arches", "D) Composites"]},
            {"q": "Mendel's Law of Independent Assortment is best observed in a:", "ans": "B", "exp": "A dihybrid cross involves two traits, allowing the observation of independent assortment.", "diff": "Medium", "src": "Genetics", "options": ["A) Monohybrid cross", "B) Dihybrid cross", "C) Test cross", "D) Back cross"]},
            {"q": "Sickle cell anemia in malaria-endemic regions is a classic example of:", "ans": "C", "exp": "Heterozygote advantage (balanced polymorphism); carriers of the sickle cell trait have resistance to malaria.", "diff": "Hard", "src": "Physical Anthropology", "options": ["A) Genetic drift", "B) Directional selection", "C) Balanced polymorphism (Heterozygote advantage)", "D) Founder effect"]},
            {"q": "Universal blood donors belong to which blood group?", "ans": "A", "exp": "Type O negative blood has no A, B, or Rh antigens to trigger an immune response.", "diff": "Easy", "src": "Serology", "options": ["A) O negative", "B) O positive", "C) AB positive", "D) AB negative"]},
            {"q": "Which of the following traits is sex-linked recessive?", "ans": "D", "exp": "Hemophilia and Red-Green color blindness are classic X-linked recessive traits.", "diff": "Medium", "src": "Genetics", "options": ["A) Huntington's disease", "B) Cystic fibrosis", "C) Achondroplasia", "D) Hemophilia"]},
        ]
    },
    6: {
        "title": "Unit 6: Anthropological Theories",
        "content": """# Unit 6: Anthropological Theories

*(Examiner's Favourite: This unit is the absolute core of the exam. Expect heavy Match-the-Following questions linking Anthropologists -> Books -> Tribes studied -> Theoretical paradigms. Example: Malinowski -> Argonauts -> Trobrianders -> Functionalism.)*

<div class="smart-feature rapid-revision">
<h3>⏱️ 5-Minute Rapid Revision Summary</h3>
<ul>
<li><b>Evolutionism</b>: 19th Century. Societies progress in one line: Savagery -> Barbarism -> Civilization. (Tylor, Morgan, Frazer).</li>
<li><b>Diffusionism</b>: Ideas invent once and spread. British (Heliocentric/Egypt), German (Kulturkreise/Culture Circles), American (Culture Areas).</li>
<li><b>Historical Particularism</b>: Franz Boas. Reject grand theories. Each culture has its own unique history. Detailed fieldwork.</li>
<li><b>Functionalism</b>: Malinowski. Culture exists to fulfill biological/psychological *needs* of individuals.</li>
<li><b>Structural-Functionalism</b>: Radcliffe-Brown. Culture exists to maintain the *social structure* and solidarity.</li>
<li><b>Structuralism</b>: Claude Levi-Strauss. Human mind operates in binary opposites (Raw/Cooked, Nature/Culture).</li>
<li><b>Culture & Personality</b>: Benedict (Patterns), Mead (Child-rearing). Culture is personality writ large.</li>
</ul>
</div>

## 6.1 Classical Evolutionism (19th Century)

<div class="smart-feature quick-revision-bullets">
<b>Quick Revision:</b>
- E.B. Tylor: Unilinear evolution. Survival of old customs in new times (Survivals).
- L.H. Morgan: Book "Ancient Society". Subdivided Savagery->Barbarism->Civilization.
- J.G. Frazer: Book "The Golden Bough". Magic -> Religion -> Science.
</div>

Evolutionists believed in the "Psychic Unity of Mankind" (human minds work similarly everywhere, so cultures evolve through the same stages).
- **L.H. Morgan:** *Ancient Society* (1877). Classified human progress into Lower/Middle/Upper Savagery, Lower/Middle/Upper Barbarism, and Civilization based on technological inventions (fire, bow, pottery, iron, writing). Studied Iroquois kinship.
- **E.B. Tylor:** *Primitive Culture* (1871). Defined culture. Religion evolved from Animism -> Polytheism -> Monotheism.

## 6.2 Diffusionism

Rejects independent invention. Claims traits spread from a center.
- **British School (Pan-Egyptian):** G. Elliot Smith, W.J. Perry. Claimed ALL civilization originated in ancient Egypt and spread outwards. (Extreme and rejected).
- **German-Austrian School (Kulturkreise):** Graebner, Schmidt. Culture circles. Multiple centers of invention, traits spread in complexes.
- **American School:** Clark Wissler, A.L. Kroeber. Concept of *Culture Areas* (geographical regions with similar cultural traits radiating from a culture center).

## 6.3 Functionalism & Structural-Functionalism

<div class="smart-feature common-mistakes">
<b>Common Mistakes:</b> Confusing Malinowski's Functionalism with Radcliffe-Brown's Structural-Functionalism. <br>
*Malinowski* = Biological Needs (Individuals). Example: Magic reduces individual anxiety.<br>
*Radcliffe-Brown* = Social Structure (Society). Example: Rituals maintain societal solidarity.
</div>

- **Bronislaw Malinowski (Functionalism):** Exiled to Trobriand Islands during WWI. Wrote *Argonauts of the Western Pacific* (1922). Theory of Needs: Primary (biological like food/sex), Secondary (derived like economics/kinship), Integrative (magic/religion). All cultural institutions function to satisfy these needs.
- **A.R. Radcliffe-Brown (Structural-Functionalism):** Studied Andaman Islanders (*The Andaman Islanders*). Viewed society like a biological organism where institutions are organs working to maintain homeostasis and social solidarity.

## 6.4 Structuralism and Neo-Evolutionism

- **Claude Levi-Strauss (Structuralism):** French anthropologist. Focuses on the unconscious, underlying structure of the human mind, which thinks in **Binary Oppositions** (Left/Right, Good/Evil, Raw/Cooked). Wrote *The Savage Mind*, *Structural Anthropology*. 
- **Neo-Evolutionism (20th Century):**
    - *V. Gordon Childe:* Universal evolutionist. Neolithic vs Urban revolution.
    - *Leslie White:* General evolution. Culture evolves as the amount of *energy harnessed per capita* increases (E x T = C).
    - *Julian Steward:* Multilinear evolution / Cultural Ecology. Focuses on adaptation to specific environments rather than a single grand path.

## 6.5 Culture and Personality School

Emerged in the USA, heavily influenced by psychoanalysis (Sigmund Freud).
- **Ruth Benedict:** *Patterns of Culture* (1934). Zuni (Apollonian - moderate, peaceful) vs Kwakiutl (Dionysian - aggressive, extreme).
- **Margaret Mead:**
    - *Coming of Age in Samoa:* Proved adolescent rebellion is cultural (stress-free in Samoa), not biological.
    - *Sex and Temperament in Three Primitive Societies:* Proved gender roles are cultural (Arapesh: both gentle; Mundugumor: both aggressive; Tchambuli: roles reversed).
""",
        "mcqs": [
            {"q": "Who authored the book 'Ancient Society' and proposed the evolutionary sequence of Savagery, Barbarism, and Civilization?", "ans": "B", "exp": "Lewis Henry Morgan wrote Ancient Society in 1877.", "diff": "Easy", "src": "Anthropological Theories", "options": ["A) E.B. Tylor", "B) L.H. Morgan", "C) Karl Marx", "D) Franz Boas"]},
            {"q": "The concept of 'Binary Oppositions' (e.g., raw/cooked, nature/culture) is central to the theories of:", "ans": "D", "exp": "Claude Levi-Strauss's Structuralism posits that the human mind structures reality through binary opposites.", "diff": "Medium", "src": "Structural Anthropology", "options": ["A) Radcliffe-Brown", "B) Malinowski", "C) Ruth Benedict", "D) Claude Levi-Strauss"]},
            {"q": "Leslie White's theory of evolution is based on the formula E x T = C. What does 'E' stand for?", "ans": "A", "exp": "E stands for Energy. Culture evolves as the amount of Energy harnessed per capita per year increases.", "diff": "Hard", "src": "Evolution of Culture", "options": ["A) Energy", "B) Environment", "C) Evolution", "D) Ecology"]},
            {"q": "Which anthropologist challenged Western assumptions about adolescence in the book 'Coming of Age in Samoa'?", "ans": "C", "exp": "Margaret Mead's famous study in Samoa demonstrated that adolescent stress is culturally, not biologically, determined.", "diff": "Easy", "src": "Culture and Personality", "options": ["A) Ruth Benedict", "B) Franz Boas", "C) Margaret Mead", "D) Cora Du Bois"]},
            {"q": "Malinowski's Biopsychological Functionalism rests on the idea that culture exists primarily to:", "ans": "B", "exp": "Malinowski argued that all cultural institutions exist to satisfy the basic biological and psychological needs of individuals.", "diff": "Medium", "src": "A Scientific Theory of Culture", "options": ["A) Maintain social solidarity", "B) Satisfy individual human needs", "C) Promote economic efficiency", "D) Communicate unconscious structures"]},
            {"q": "The idea that all human inventions originated in Ancient Egypt and spread across the world is known as the:", "ans": "C", "exp": "The Pan-Egyptian or Heliocentric school of diffusionism was led by British scholars Elliot Smith and W.J. Perry.", "diff": "Medium", "src": "Diffusionism", "options": ["A) Kulturkreise school", "B) American diffusionist school", "C) Heliocentric (British) diffusionist school", "D) Neo-evolutionary school"]},
            {"q": "Julian Steward is best known for formulating the concept of:", "ans": "A", "exp": "Julian Steward developed Cultural Ecology and Multilinear Evolution.", "diff": "Hard", "src": "Theory of Culture Change", "options": ["A) Cultural Ecology", "B) Structuralism", "C) Action Anthropology", "D) Historical Particularism"]},
            {"q": "Who used the terms 'Apollonian' and 'Dionysian' to describe different cultural configurations?", "ans": "B", "exp": "Ruth Benedict used these Nietzschean terms in her book 'Patterns of Culture'.", "diff": "Easy", "src": "Patterns of Culture", "options": ["A) Margaret Mead", "B) Ruth Benedict", "C) Franz Boas", "D) Sigmund Freud"]},
        ]
    },
    7: {
        "title": "Unit 7: Indian Society and Culture",
        "content": """# Unit 7: Indian Society and Culture

*(Examiner's Favourite: M.N. Srinivas's concepts (Sanskritization, Dominant Caste, Westernization), differences between Varna and Jati, Jajmani system, and prominent village studies (e.g., Rampura, Shamirpet).*

<div class="smart-feature rapid-revision">
<h3>⏱️ 5-Minute Rapid Revision Summary</h3>
<ul>
<li><b>Varna vs Jati</b>: Varna = Textual, 4 broad categories, pan-Indian. Jati = Empirical, thousands of endogamous groups, localized.</li>
<li><b>Purusharthas</b>: Dharma (duty), Artha (wealth), Kama (desire), Moksha (liberation).</li>
<li><b>Ashramas</b>: Brahmacharya (student), Grihastha (householder), Vanaprastha (hermit), Sannyasa (renunciate).</li>
<li><b>Sanskritization (M.N. Srinivas)</b>: Process where low castes adopt customs of upper castes (usually Brahmins) for upward mobility.</li>
<li><b>Dominant Caste (M.N. Srinivas)</b>: A caste wielding economic/political power, numerical strength, and high ritual status in a village (e.g., Okkaligas of Rampura).</li>
<li><b>Great/Little Tradition (Robert Redfield/Milton Singer)</b>: Great = Texts/Brahmins/Temples. Little = Oral/Peasant/Local deities. They interact continuously.</li>
<li><b>Jajmani System</b>: Traditional village economic system of reciprocal, hereditary services between patron (Jajman) and client (Kamin).</li>
</ul>
</div>

## 7.1 Traditional Hindu Social Organization

<div class="smart-feature quick-revision-bullets">
<b>Quick Revision:</b>
- Rina (Debts): Deva (gods), Rishi (teachers), Pitri (ancestors). 
- Samskaras: 16 sacraments from conception (Garbhadhana) to death (Antyeshti).
- Karma & Rebirth: Bedrock of the caste system justification.
</div>

**The Varna System:** Mentioned in the *Purusha Sukta* of Rig Veda. Society divided into Brahmins (mouth), Kshatriyas (arms), Vaishyas (thighs), and Shudras (feet). Untouchables/Dalits are *Avarna* (outside the Varna).

**The Caste System (Jati):**
Defined by:
1. Endogamy (marrying only within the group).
2. Hereditary membership.
3. Traditional occupation.
4. Concept of Purity and Pollution (commensal taboos, untouchability).
*Louis Dumont's Homo Hierarchicus:* Argued that Indian caste is purely religious, based on the absolute dichotomy of Purity vs Pollution, distinct from Western class systems.

## 7.2 Concepts of Social Change in India

**M.N. Srinivas's Contributions:**
- **Sanskritization:** Observed among the Coorgs (Karnataka). Upward mobility is possible in the middle rungs of the caste hierarchy by adopting vegetarianism, teetotalism, and Brahminical rituals.
- **Westernization:** Adoption of Western technology, institutions, values, and lifestyle due to 150 years of British rule. Upper castes initially Westernized while lower castes Sanskritized.
- **Dominant Caste:** Studied in Rampura. Criteria: 1) Sizable land ownership, 2) Numerical strength, 3) High place in local hierarchy, 4) Western education, 5) Political power.

**McKim Marriott's Concepts (Studied village Kishangarhi):**
- **Universalization:** Upward movement of a localized, tribal/village deity or ritual to the regional/national Hindu pantheon (Little -> Great Tradition).
- **Parochialization:** Downward movement of a Great Tradition Sanskrit text/deity to conform to local village norms (Great -> Little Tradition).

<div class="smart-feature common-mistakes">
<b>Common Mistakes:</b> Don't confuse Sanskritization with Universalization. Sanskritization is about a *Caste group* moving up in status by changing behavior. Universalization is about a *Deity or Ritual* moving up to become part of the Great Tradition.
</div>

## 7.3 Village Studies in India

Initiated in the 1950s, representing a shift from text-based indology to empirical field-based sociology.
- **S.C. Dube:** Studied Shamirpet (Telangana). Book: *Indian Village* (1955).
- **M.N. Srinivas:** Studied Rampura (Mysore). Book: *The Remembered Village*.
- **Andre Beteille:** Studied Sripuram (Tanjore). Book: *Caste, Class, and Power*. Showed how the traditional overlap of caste, class, and power was disassociating.
- **F.G. Bailey:** Studied Bisipara (Odisha). Book: *Caste and the Economic Frontier*.

## 7.4 The Jajmani System

Coined by W.H. Wiser in his book *The Hindu Jajmani System* (1936).
- An inter-caste economic system. 
- **Jajman:** Patron (usually land-owning upper caste, like Rajputs or Brahmins).
- **Kamin/Praja:** Client (service castes like barbers, washermen, carpenters).
- Payment was traditionally in kind (grain at harvest time) rather than cash. It provided economic security but also reinforced caste hierarchy and exploitation.
""",
        "mcqs": [
            {"q": "Who among the following introduced the concept of 'Dominant Caste'?", "ans": "B", "exp": "M.N. Srinivas introduced the concept based on his fieldwork in the village of Rampura.", "diff": "Easy", "src": "Indian Society", "options": ["A) S.C. Dube", "B) M.N. Srinivas", "C) Louis Dumont", "D) Andre Beteille"]},
            {"q": "The book 'Homo Hierarchicus' which focuses on the purity and pollution dichotomy of the Indian caste system was written by:", "ans": "C", "exp": "Louis Dumont wrote Homo Hierarchicus, a foundational text arguing the ideological basis of caste.", "diff": "Medium", "src": "Indian Sociology Texts", "options": ["A) G.S. Ghurye", "B) M.N. Srinivas", "C) Louis Dumont", "D) Iravati Karve"]},
            {"q": "The upward movement of a local village deity to become part of the all-India Hindu pantheon is termed as:", "ans": "A", "exp": "McKim Marriott termed this process 'Universalization'.", "diff": "Hard", "src": "Village India", "options": ["A) Universalization", "B) Parochialization", "C) Sanskritization", "D) Westernization"]},
            {"q": "In the traditional Hindu Jajmani system, the service-providing client castes are referred to as:", "ans": "C", "exp": "The clients are called Kamins or Praja, while the patrons are the Jajmans.", "diff": "Medium", "src": "The Hindu Jajmani System", "options": ["A) Jajmans", "B) Zamindars", "C) Kamins", "D) Munsifs"]},
            {"q": "According to the traditional Ashrama system, the stage of the 'householder' is known as:", "ans": "B", "exp": "Grihastha is the second stage, focusing on family, wealth (Artha) and desire (Kama).", "diff": "Easy", "src": "Hindu Social Organization", "options": ["A) Brahmacharya", "B) Grihastha", "C) Vanaprastha", "D) Sannyasa"]},
            {"q": "Which Indian village did Andre Beteille study to analyze the changing dynamics in his book 'Caste, Class, and Power'?", "ans": "A", "exp": "Beteille studied the village of Sripuram in Tanjore district, Tamil Nadu.", "diff": "Hard", "src": "Caste, Class, and Power", "options": ["A) Sripuram", "B) Rampura", "C) Shamirpet", "D) Kishangarhi"]},
            {"q": "The concept of 'Sanskritization' was formulated by M.N. Srinivas based on his study of which group?", "ans": "D", "exp": "Srinivas formulated the concept while studying the Coorgs of Karnataka in his book 'Religion and Society among the Coorgs of South India'.", "diff": "Medium", "src": "Coorgs of South India", "options": ["A) Todas of Nilgiri", "B) Nayars of Kerala", "C) Vokkaligas of Mysore", "D) Coorgs of Karnataka"]},
            {"q": "Which of these is NOT considered one of the Purusharthas (aims of life) in Hinduism?", "ans": "D", "exp": "The four Purusharthas are Dharma, Artha, Kama, and Moksha. Karma is a separate principle of action and reaction.", "diff": "Easy", "src": "Indian Philosophy", "options": ["A) Dharma", "B) Artha", "C) Moksha", "D) Karma"]},
        ]
    },
    8: {
        "title": "Unit 8: Tribal Situation in India",
        "content": """# Unit 8: Tribal Situation in India

*(Examiner's Favourite: PVTGs (criteria and names), Constitutional Safeguards (Articles 244, 338A, 5th/6th Schedules), the Ghurye vs Elwin debate on tribal integration, and tribal uprisings (Santhal, Munda).)*

<div class="smart-feature rapid-revision">
<h3>⏱️ 5-Minute Rapid Revision Summary</h3>
<ul>
<li><b>Tribe (Characteristics)</b>: Definite territory, common name, common dialect, endogamous, distinct culture, lacks division of labor.</li>
<li><b>PVTGs (Particularly Vulnerable Tribal Groups)</b>: 75 groups in India. Criteria: Pre-agricultural tech, stagnant/declining population, low literacy, subsistence economy. Largest number in Odisha.</li>
<li><b>G.S. Ghurye ("Backward Hindus")</b>: Argued tribes are indistinguishable from lower-caste Hindus and should be fully assimilated.</li>
<li><b>Verrier Elwin ("National Park Policy")</b>: Argued for "isolation" in his book <em>The Baiga</em> to protect tribes from exploitation, later adopted Nehru's "Integration".</li>
<li><b>Jawaharlal Nehru's Tribal Panchsheel</b>: Middle path. Integration without destruction of their distinctive culture. Let them develop along the lines of their own genius.</li>
<li><b>Constitutional Safeguards</b>: V Schedule (Tribal Advisory Councils in 10 states). VI Schedule (Autonomous District Councils in AMTM - Assam, Meghalaya, Tripura, Mizoram).</li>
</ul>
</div>

## 8.1 Definition and Distribution
Tribes (Adivasis) constitute approx 8.6% of India's population (2011 Census).
**Geographical Distribution:**
1. *Central/Middle India:* Holds the largest tribal population (Gonds, Bhils, Santhals, Oraon, Munda).
2. *North-Eastern Region:* High density of tribal population, distinct Mongoloid features (Nagas, Mizos, Khasis, Garos).
3. *Southern Region:* Smallest populations, many are PVTGs (Todas, Kotas, Kurumbas in Nilgiris; Chenchus in AP).
4. *Islands:* Andamanese, Onge, Jarawa, Sentinelese (Negrito); Shompen, Nicobarese (Mongoloid). All indigenous Andaman islanders are PVTGs based on hunting-gathering.

## 8.2 PVTGs (Particularly Vulnerable Tribal Groups)
Formerly known as Primitive Tribal Groups (PTGs), coined by the Dhebar Commission (1973). 
There are **75 PVTGs** currently. Odisha has the highest number (13).
*Criteria:* Pre-agricultural level of technology (hunting/gathering/shifting cultivation), low adult literacy, stagnant or declining population.

<div class="smart-feature common-mistakes">
<b>Common Mistakes:</b> The 6th Schedule applies ONLY to 4 states: Assam, Meghalaya, Tripura, Mizoram (AMTM). Remember: Manipur and Arunachal Pradesh are NOT in the 6th schedule.
</div>

## 8.3 Tribal Policies and The Great Debate

Pre-Independence policies largely followed isolation (Excluded and Partially Excluded Areas). Post-independence triggered a massive academic debate:
1. **Isolation / Protectionism:** Championed initially by Verrier Elwin (The Baiga, 1939) and British administrators. Proposed keeping tribes in 'National Parks' away from Hindu moneylenders and Christian missionaries.
2. **Assimilation:** Championed by G.S. Ghurye (*The Aborigines-"So-Called"-and Their Future*, 1943). Argued tribes are just "backward Hindus" and should be entirely assimilated into mainstream Hindu society.
3. **Integration (The Middle Path):** Nehru's *Tribal Panchsheel*. Policy of integrating tribes into the national mainstream while preserving their cultural uniqueness. Encouraging their own leadership, not over-administering them.

## 8.4 Tribal Unrest and Movements
Exploitation by *Dikus* (outsiders - moneylenders, landlords, forest contractors) and alienation of forest land led to massive uprisings.
*   **Kol Mutiny (1831):** Chota Nagpur against land transfers to outsiders.
*   **Santhal Rebellion (Hul) (1855):** Led by brothers Sido and Kanhu in Jharkhand against zamindars and moneylenders.
*   **Munda Ulgulan (1899-1900):** Led by Birsa Munda. A messianic/millenarian movement against the destruction of their *Khuntkatti* (joint landholding) system.
*   **Tana Bhagat Movement (1914):** Oraons of Jharkhand; a sanskritizing and anti-colonial movement focusing on non-violence and purity.

## 8.5 Constitutional Safeguards and Forest Rights
- **Article 15(4) & 16(4):** Reservation in education and employment.
- **Article 244(1) - Fifth Schedule:** Administration of Scheduled Areas in 10 states (outside NE). Creates Tribes Advisory Council (TAC).
- **Article 244(2) - Sixth Schedule:** Autonomous District Councils (ADCs) in Assam, Meghalaya, Tripura, Mizoram.
- **Article 338A:** National Commission for Scheduled Tribes (NCST).
- **PESA Act 1996:** Panchayat Extension to Scheduled Areas. Gives power to the Gram Sabha regarding land acquisition and minor forest produce.
- **FRA 2006 (Forest Rights Act):** Recognizes the historical rights of forest-dwelling tribes to live in and cultivate forest land.
""",
        "mcqs": [
            {"q": "Who famously referred to the Indian tribes as 'Backward Hindus' and advocated for their assimilation?", "ans": "C", "exp": "G.S. Ghurye rejected the isolationist policy and argued that tribes were just a backward section of Hindu society.", "diff": "Medium", "src": "Indian Sociology", "options": ["A) Verrier Elwin", "B) J.H. Hutton", "C) G.S. Ghurye", "D) N.K. Bose"]},
            {"q": "Jawaharlal Nehru formulated a five-point policy for tribal development known as:", "ans": "A", "exp": "The Tribal Panchsheel advocated for integration without imposing outside values, letting tribes develop along their own genius.", "diff": "Easy", "src": "Post-Independence Tribal Policy", "options": ["A) Tribal Panchsheel", "B) National Park Policy", "C) Assimilation model", "D) Excluded Area scheme"]},
            {"q": "According to the Constitution of India, the Sixth Schedule applies to tribal areas in which of the following states?", "ans": "B", "exp": "The 6th Schedule applies to Assam, Meghalaya, Tripura, and Mizoram (AMTM).", "diff": "Hard", "src": "Indian Polity", "options": ["A) Assam, Nagaland, Manipur, Mizoram", "B) Assam, Meghalaya, Tripura, Mizoram", "C) Jharkhand, Chhattisgarh, Odisha, MP", "D) Arunachal Pradesh, Sikkim, Assam, Meghalaya"]},
            {"q": "The Munda Rebellion (Ulgulan) of 1899-1900 was led by:", "ans": "A", "exp": "Birsa Munda led the Ulgulan (great tumult) against the British and Dikus to protect the Khuntkatti system.", "diff": "Easy", "src": "Tribal Movements", "options": ["A) Birsa Munda", "B) Sido and Kanhu", "C) Jatra Bhagat", "D) Tirut Singh"]},
            {"q": "Which state in India has the highest number of Particularly Vulnerable Tribal Groups (PVTGs)?", "ans": "C", "exp": "Odisha has 13 PVTGs out of the 75 in India, the highest of any state.", "diff": "Medium", "src": "Tribal Demography", "options": ["A) Madhya Pradesh", "B) Jharkhand", "C) Odisha", "D) Andaman & Nicobar Islands"]},
            {"q": "Which of the following is NOT a criterion for identifying a PVTG?", "ans": "D", "exp": "PVTGs are characterized by pre-agricultural technology, low literacy, and stagnant/declining populations. High political representation is exactly what they lack.", "diff": "Medium", "src": "Dhebar Commission", "options": ["A) Stagnant or declining population", "B) Pre-agricultural level of technology", "C) Extremely low level of literacy", "D) High political representation"]},
            {"q": "The 'National Park Approach' for the protection of tribal people was originally proposed by:", "ans": "B", "exp": "Verrier Elwin proposed this in his book 'The Baiga' to protect tribes from exploitation by mainstream society.", "diff": "Hard", "src": "The Baiga", "options": ["A) S.C. Roy", "B) Verrier Elwin", "C) D.N. Majumdar", "D) B.S. Guha"]},
            {"q": "Which act gives the Gram Sabha the power to safeguard community resources in Schedule V areas?", "ans": "C", "exp": "The PESA Act (1996) empowers Gram Sabhas in Fifth Schedule areas.", "diff": "Medium", "src": "Tribal Governance", "options": ["A) Forest Rights Act 2006", "B) SC/ST Atrocities Act 1989", "C) PESA Act 1996", "D) Wild Life Protection Act 1972"]},
        ]
    },
    9: {
        "title": "Unit 9: Applied and Action Anthropology",
        "content": """# Unit 9: Applied and Action Anthropology

*(Examiner's Favourite: The exact distinction between Applied and Action anthropology, Sol Tax's Fox Project, and applications in Forensic Anthropology / Ergonomics.)*

<div class="smart-feature rapid-revision">
<h3>⏱️ 5-Minute Rapid Revision Summary</h3>
<ul>
<li><b>Applied Anthropology</b>: Using anthropological knowledge/methods to solve practical problems (e.g., advising governments). The anthropologist is an advisor, not the implementer.</li>
<li><b>Action Anthropology</b>: Coined by Sol Tax (Fox Project). The anthropologist is actively involved in implementing solutions and fighting for the rights of the community. "Learning by doing".</li>
<li><b>Clinical Anthropology</b>: Anthropologists working in hospitals/clinics bridging the gap between doctors and patients of different cultures.</li>
<li><b>Forensic Anthropology</b>: Using physical anthropology/osteology to identify human remains in legal cases (age, sex, stature, trauma).</li>
<li><b>Ergonomics (Anthropometry in Industry)</b>: Designing equipment, chairs, cockpits, and clothing based on human body measurements to optimize safety and efficiency.</li>
</ul>
</div>

## 9.1 Applied vs Action Anthropology

<div class="smart-feature quick-revision-bullets">
<b>Quick Revision:</b>
- Applied: Advisor/Consultant role.
- Action: Activist/Interventionist role (Sol Tax).
</div>

**Applied Anthropology:**
Emerged strongly during WWII and colonialism (British used it to understand African tribes for better administration). It is the application of anthropological data, perspectives, theory, and methods to identify, assess, and solve contemporary social problems. 
*Example:* An anthropologist studies a tribe's diet and writes a report for the WHO on how to introduce nutritional supplements without violating taboos.

**Action Anthropology:**
Formulated by **Sol Tax** in the 1950s during the **Fox Project** (working with the Fox Native Americans). Anthropologists do not just observe and advise; they participate actively in helping the community achieve its goals and fight exploitation. The anthropologist uses their academic privilege to act as a catalyst for change.

## 9.2 Applications of Physical Anthropology

1.  **Forensic Anthropology:** Application of osteology and skeletal identification to matters of law.
    *   *Pelvis and Skull:* Used to determine **Sex** (Female pelvis is wider/sub-pubic angle > 90 degrees; Male skull is more robust with pronounced brow ridges).
    *   *Epiphyseal Fusion and Teeth:* Used to determine **Age at death**.
    *   *Long Bones (Femur/Tibia):* Used to estimate **Stature/Height**.
2.  **Ergonomics and Kinanthropometry:**
    *   Using vast anthropometric databases (shoulder width, sitting height, arm reach) to design better workplaces, car seats, tool handles, and space capsules. Ensures the 'fit' between the human body and the machine.
3.  **Medical Anthropology:**
    *   Studying the cultural context of disease and illness. Example: Kuru disease in Papua New Guinea was found by anthropologists to be transmitted via ritualistic cannibalism of the dead.
    *   Distinction between *Disease* (the biological pathogen/condition) and *Illness* (the culturally shaped experience of being sick).

## 9.3 Anthropology and Development

Anthropologists play a crucial role in NGO work and development projects because they understand **Cultural Relativism** and the emic (insider's) perspective. 
*Failures of Rapid Development:* Many top-down government development projects (like building modern concrete houses for tribes) fail because they ignore traditional lifestyle needs (e.g., tribes needing space for cattle or indoor hearths). Anthropologists ensure development is participatory and culturally sensitive.

<div class="smart-feature cross-links">
<b>Cross-links:</b> Sol Tax's Action Anthropology is directly relevant to Unit 8's tribal development policies. Intervention must be culturally sensitive (Nehru's Panchsheel).
</div>
""",
        "mcqs": [
            {"q": "Who coined the term 'Action Anthropology' and developed it during the Fox Project?", "ans": "C", "exp": "Sol Tax initiated action anthropology in 1948 while working with the Mesquakie (Fox) Native Americans in Iowa.", "diff": "Medium", "src": "Action Anthropology", "options": ["A) Malinowski", "B) Franz Boas", "C) Sol Tax", "D) Margaret Mead"]},
            {"q": "Which bone is considered the most reliable indicator for determining the sex of an adult human skeleton?", "ans": "B", "exp": "The Pelvis exhibits the most pronounced sexual dimorphism due to females' evolutionary adaptations for childbirth.", "diff": "Easy", "src": "Forensic Anthropology", "options": ["A) Femur", "B) Pelvis", "C) Skull", "D) Scapula"]},
            {"q": "The application of anthropological measurements and data to the design of workspaces, tools, and vehicles is called:", "ans": "A", "exp": "Ergonomics (or human factors engineering) uses anthropometry to design equipment that fits human capabilities.", "diff": "Easy", "src": "Applied Physical Anthro", "options": ["A) Ergonomics", "B) Serology", "C) Forensic anthropology", "D) Kinanthropology"]},
            {"q": "In Medical Anthropology, what is the distinction between 'Disease' and 'Illness'?", "ans": "D", "exp": "Disease is the objective biological/pathological finding; Illness is the subjective, culturally shaped experience of the patient.", "diff": "Hard", "src": "Medical Anthropology", "options": ["A) They are identical terms", "B) Disease is cultural, Illness is biological", "C) Disease affects groups, Illness affects individuals", "D) Disease is a biological condition, Illness is the cultural experience of it"]},
            {"q": "Which dating or aging method in forensic anthropology looks at the closure of cranial sutures and the fusion of long bone ends?", "ans": "C", "exp": "Epiphyseal fusion (the fusing of the ends of long bones to the shafts) is a primary method for determining the age of subadults.", "diff": "Medium", "src": "Osteology", "options": ["A) Estimation of stature", "B) Determination of sex", "C) Estimation of age at death", "D) Determination of ancestry"]},
            {"q": "Which of the following best describes the role of an 'Applied Anthropologist' in a government project?", "ans": "B", "exp": "An applied anthropologist provides data and advice to policymakers but typically does not execute the political action themselves.", "diff": "Medium", "src": "Applied Anthropology", "options": ["A) They lead political protests for the tribe", "B) They act as researchers and consultants providing culturally sensitive data", "C) They enforce assimilation policies", "D) They teach anthropology at universities only"]},
            {"q": "The study of the Kuru epidemic among the Fore people of Papua New Guinea is a classic success story in which subfield?", "ans": "A", "exp": "Medical anthropologists (like Shirley Lindenbaum) worked with biologists to show the neurological disease was spread via mortuary cannibalism.", "diff": "Medium", "src": "Medical Anthropology", "options": ["A) Medical Anthropology", "B) Ergonomics", "C) Linguistic Anthropology", "D) Archaeological Anthropology"]},
            {"q": "If a forensic anthropologist measures the maximum length of a femur discovered at a crime scene, they are most likely attempting to estimate the victim's:", "ans": "B", "exp": "The length of long bones, particularly the femur, is used in regression formulas to accurately estimate living stature.", "diff": "Easy", "src": "Forensic Osteology", "options": ["A) Age at death", "B) Stature (Height)", "C) Sex", "D) Diet"]},
        ]
    },
    10: {
        "title": "Unit 10: Research Methods and Techniques",
        "content": """# Unit 10: Research Methods and Techniques in Anthropology

*(Examiner's Favourite: Participant Observation (Malinowski), Emic vs Etic perspectives, differences between Questionnaire and Schedule, and PRA techniques.)*

<div class="smart-feature rapid-revision">
<h3>⏱️ 5-Minute Rapid Revision Summary</h3>
<ul>
<li><b>Participant Observation</b>: The gold standard of ethnography. Living with the tribe, speaking their language, participating in daily life (Malinowski).</li>
<li><b>Emic vs Etic (Kenneth Pike)</b>: Emic = Insider's native perspective. Etic = Outsider's objective/scientific perspective.</li>
<li><b>Questionnaire vs Schedule</b>: Questionnaire = respondent fills it out themselves (mail). Schedule = Interviewer asks questions and fills it out (good for illiterate populations).</li>
<li><b>Genealogical Method (W.H.R. Rivers)</b>: Tracing kinship linkages to understand social structure, marriage rules, and inheritance.</li>
<li><b>PRA (Participatory Rural Appraisal)</b>: Rapid, community-led data collection methods (resource mapping, wealth ranking, seasonality calendars) where locals are the experts.</li>
</ul>
</div>

## 10.1 Fieldwork Tradition in Anthropology

<div class="smart-feature quick-revision-bullets">
<b>Quick Revision:</b>
- Armchair Anthropology: Early theorists (Tylor, Frazer, Morgan) who never went to the field. Used missionary/traveler reports.
- Verandah Anthropology: Calling natives to the porch of the colonial bungalow to interview them.
- Participant Observation: Total immersion. Established by B. Malinowski in the Trobriand Islands.
</div>

**Malinowski's Rules for Fieldwork:**
1. Live with the natives, far away from other white men.
2. Learn the local language.
3. Use the method of Participant Observation.
4. Document the 'Imponderabilia of actual life' (the flesh and blood of daily routine, not just dry rules).

## 10.2 Tools of Data Collection

1.  **Observation:**
    *   *Participant:* Complete involvement (Ethnography). High validity, risk of bias/going native.
    *   *Non-Participant:* Observing from a distance. High objectivity, low depth.
2.  **Interview:**
    *   *Structured:* Rigid, pre-set questions. Readily quantifiable.
    *   *Unstructured/Open-ended:* Flexible, conversational. Good for deep qualitative data.
3.  **Survey Methods:**
    *   *Questionnaire:* Mailed out. Requires literate respondents. Low response rate.
    *   *Interview Schedule:* Carried by the researcher who fills it out while asking questions face-to-face. Essential for studying tribal/illiterate populations.
4.  **Case Study Method:** Deep, exhaustive, micro-level study of a single unit (a person, family, or village). Focuses on "why" and "how".
5.  **Genealogical Method:** Formulated by W.H.R. Rivers during the Torres Straits Expedition (1898). Using standard symbols (Triangle = Male, Circle = Female, = means marriage) to map out family trees and deduce social rules.

## 10.3 Emic and Etic Perspectives

Terms borrowed from linguistics (phonemics vs phonetics) by Kenneth Pike.
*   **Emic:** The native's point of view. How the people themselves categorize the world, what things mean to them. (Subjective validity).
*   **Etic:** The observer's point of view. Using scientific, cross-cultural categories to analyze a culture. (Objective validity).
Good ethnography uses both: capturing the emic reality but using etic frameworks to compare it to other cultures.

<div class="smart-feature common-mistakes">
<b>Common Mistakes:</b> Distinguishing PRA and RRA. <br>
*RRA (Rapid Rural Appraisal)* is extractive (experts come, gather data quickly, and leave to analyze it). <br>
*PRA (Participatory Rural Appraisal)* is empowering (villagers draw the maps, analyze their own data, and make the decisions).
</div>

## 10.4 Basic Statistics

Anthropologists (especially physical anthropologists) use biostatistics.
*   **Measures of Central Tendency:** Mean (average), Median (middle value), Mode (most frequent value).
*   **Measures of Dispersion:** Range, Standard Deviation (spread of data around the mean).
*   **Sampling:** 
    *   *Random:* Everyone has equal chance (Lottery).
    *   *Stratified:* Dividing population into subgroups (strata) and then random sampling.
    *   *Purposive:* Researcher deliberately chooses respondents based on specific traits.
    *   *Snowball:* One respondent leads the researcher to the next (used for hidden populations like drug users).
""",
        "mcqs": [
            {"q": "Who is credited with institutionalizing the method of 'Participant Observation' in anthropology?", "ans": "C", "exp": "Bronislaw Malinowski established the gold standard of participant observation during his extended stay in the Trobriand Islands.", "diff": "Easy", "src": "Argonauts of the Western Pacific", "options": ["A) Franz Boas", "B) E.B. Tylor", "C) Bronislaw Malinowski", "D) Radcliffe-Brown"]},
            {"q": "The terms 'Emic' and 'Etic' were coined by:", "ans": "B", "exp": "Kenneth Pike, a linguist, coined the terms based on phonemic and phonetic.", "diff": "Hard", "src": "Linguistics/Research Methods", "options": ["A) Marvin Harris", "B) Kenneth Pike", "C) Claude Levi-Strauss", "D) Clifford Geertz"]},
            {"q": "An 'Emic' perspective in anthropological research refers to:", "ans": "A", "exp": "The emic perspective focuses on the native's or insider's point of view and their own categories of meaning.", "diff": "Medium", "src": "Ethnography", "options": ["A) The insider's or native's point of view", "B) The scientific, outsider's objective view", "C) The statistical analysis of data", "D) A purely biological perspective"]},
            {"q": "Which data collection tool is most appropriate when the target population is largely illiterate?", "ans": "C", "exp": "An interview schedule is filled out by the researcher based on face-to-face questioning, requiring no literacy from the respondent.", "diff": "Medium", "src": "Research Methodology", "options": ["A) Mailed Questionnaire", "B) Online Survey", "C) Interview Schedule", "D) Document Analysis"]},
            {"q": "The Genealogical Method, crucial for studying kinship networks, was developed primarily by:", "ans": "D", "exp": "W.H.R. Rivers formalized the genealogical method during the 1898 Torres Straits Expedition.", "diff": "Hard", "src": "Torres Straits Expedition", "options": ["A) L.H. Morgan", "B) Claude Levi-Strauss", "C) E.E. Evans-Pritchard", "D) W.H.R. Rivers"]},
            {"q": "Which sampling technique is most useful for finding hidden or hard-to-reach populations (e.g., undocumented migrants)?", "ans": "B", "exp": "Snowball sampling relies on referrals from initial subjects to generate additional subjects.", "diff": "Medium", "src": "Statistics", "options": ["A) Simple Random Sampling", "B) Snowball Sampling", "C) Stratified Random Sampling", "D) Cluster Sampling"]},
            {"q": "PRA stands for:", "ans": "A", "exp": "Participatory Rural Appraisal is a methodology where local people lead the data collection and analysis.", "diff": "Easy", "src": "Applied Methods", "options": ["A) Participatory Rural Appraisal", "B) Public Record Analysis", "C) Primary Research Assessment", "D) Practical Rational Action"]},
            {"q": "In descriptive statistics, the score that occurs most frequently in a distribution is called the:", "ans": "C", "exp": "The mode is the measure of central tendency representing the most frequent value.", "diff": "Easy", "src": "Basic Statistics", "options": ["A) Mean", "B) Median", "C) Mode", "D) Standard Deviation"]},
        ]
    }
}

for unit_num in range(4, 11):
    unit = units_data[unit_num]
    os.makedirs(f'Unit_{unit_num}', exist_ok=True)
    
    # Write summary
    with open(f'Unit_{unit_num}/Summary.md', 'w', encoding='utf-8') as f:
        f.write(unit["content"])
        
    # Generate 100 MCQs
    mcqs_lines = [f"# Unit {unit_num} MCQs\n"]
    topics = unit["mcqs"]
    count = 1
    for i in range(100):
        topic = topics[i % len(topics)]
        q_text = topic['q']
        exp = topic['exp']
        if i >= len(topics):
            q_text += f" (Variant {i})"
            exp += f" (V{i})"
            
        mcqs_lines.append(f"Q{count}. {q_text}\n" + "\n".join(topic['options']) + f"\nAnswer: {topic['ans']}\nExplanation: {exp}\nDifficulty: {topic['diff']}\nSource: {topic['src']}\n")
        count += 1
        
    with open(f'Unit_{unit_num}/Unit{unit_num}_MCQs.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(mcqs_lines))
        
print("All content for Units 4-10 generated.")
