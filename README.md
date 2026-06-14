## 🌐 Ontology Documentation

📄 [View Live Documentation](https://elifozknt.github.io/emotion-aware-recommendation-ontology/index.html)

---

## Phase 2 Updates

* Personality class extended with 6 subclasses (Big Five model)
* Emotion class extended with 3 subclasses (PositiveEmotion, NegativeEmotion, NeutralEmotion)
* Added DynamicEmotion class for emotion intensity tracking
* Added BehaviorProfile class for user behavior modeling
* Added EmotionSession class for session-based emotion monitoring
* Added UserInteraction class for interaction logging
* Added DataSource class for provenance tracking
* Added LLM-assisted ontology population support
* Added SHACL validation support
* Added GraphDB knowledge graph deployment
* Added 11 SPARQL competency query implementations
* Version: 2.0.0

# Emotion-Aware Intelligent Recommendation Ontology

## Description

This project presents an ontology for modeling an intelligent recommendation system based on user emotions, needs, context, personality traits, behavioral profiles, preferences, and content effects. The system matches a user's current emotional state and situational context to appropriate digital content and generates personalized recommendations.

Version 2.0 extends the ontology with dynamic emotion tracking, session-based interaction logging, data provenance, SHACL validation, and LLM-assisted ontology population capabilities.

## Domain

Emotion-aware recommendation systems / Affective Computing / Semantic Web.

## Purpose

The purpose of this ontology is to provide personalized content recommendations according to a user's emotional state, contextual situation, personality traits, and behavioral characteristics.

## Scope

This ontology includes concepts such as:

* User
* Emotion
* DynamicEmotion
* Need
* Content
* Recommendation
* Context
* Personality
* BehaviorProfile
* EmotionSession
* UserInteraction
* DataSource
* Platform
* Feedback

It does **not** include medical diagnosis, clinical decision-making, or real-time sensor processing.

## Example Scenario

A user named Elif feels stressed at night and is alone at home → the system identifies her need for relaxation → recommends a calming LoFi playlist available on Spotify → logs user interactions and tracks emotional intensity changes over time.

---

## Main Concepts (Classes)

| Class             | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| `User`            | A person who receives recommendations                      |
| `Emotion`         | An emotional state experienced by a user                   |
| `DynamicEmotion`  | Emotion intensity observations that change over time       |
| `Need`            | A user need arising from an emotion                        |
| `Content`         | A digital content item that can be recommended             |
| `Recommendation`  | A personalized suggestion generated for a user             |
| `Context`         | The situation in which the user is located                 |
| `TimeContext`     | Subclass of Context representing time information          |
| `Environment`     | Subclass of Context representing environmental information |
| `Personality`     | User personality traits (Big Five hierarchy)               |
| `BehaviorProfile` | Behavioral tendencies inferred from user actions           |
| `EmotionSession`  | Session-based emotional monitoring                         |
| `UserInteraction` | User interactions with recommended content                 |
| `DataSource`      | Provenance information for generated instances             |
| `Preference`      | A user's preferred content type                            |
| `Effect`          | The expected psychological effect of a content item        |
| `Platform`        | The digital platform where content is delivered            |
| `Feedback`        | A user's response to a recommendation                      |

---

## Key Relationships (Properties)

* `User → feels → Emotion`
* `Emotion → createsNeed → Need`
* `Need → satisfiedBy → Content`
* `Content → hasEffect → Effect`
* `Effect → relievesEmotion → Emotion`
* `User → hasDynamicEmotion → DynamicEmotion`
* `DynamicEmotion → changesOverTime → DynamicEmotion`
* `EmotionSession → hasInteraction → UserInteraction`
* `UserInteraction → interactedWith → Content`
* `UserInteraction → populatedFrom → DataSource`
* `Recommendation → givenTo → User`
* `Recommendation → includesContent → Content`
* `Recommendation → basedOnEmotion → Emotion`
* `Recommendation → considersContext → Context`

---

## Knowledge Graph & GraphDB

The ontology was deployed and tested in GraphDB.

The knowledge graph includes:

* Users
* Emotions
* Dynamic emotions
* Needs
* Content items
* Recommendations
* Interaction logs
* Data provenance information

GraphDB was used for:

* Knowledge graph visualization
* Ontology exploration
* SPARQL query execution
* Class hierarchy inspection
* Relationship analysis

---

## SPARQL Queries

The project includes 11 SPARQL queries demonstrating:

* User emotion retrieval
* Negative emotion detection
* Personality-based recommendations
* Emotion-based recommendations
* Dynamic emotion intensity tracking
* Session interaction analysis
* Platform availability analysis
* Data provenance tracking
* Emotion transition analysis
* Aggregation queries
* Competency question validation

📄 See: `SPARQL_Queries.md`

---

## SHACL Validation

Ontology validation was performed using SHACL constraints and pySHACL.

Validation files:

* `shapes.ttl`
* `validate_shacl.py`

Validation result:

```text
Conforms: True
```

The ontology satisfies all defined SHACL constraints successfully.

---

## LLM Integration

The ontology supports LLM-assisted ontology population.

Example workflow:

1. User provides emotional information in natural language.
2. LLM extracts emotion and contextual information.
3. Ontology instances are generated automatically.
4. SPARQL queries retrieve suitable recommendations.
5. Personalized content is returned to the user.

---

## Instances (ABox)

The ontology includes four complete scenario instances:

| User  | Emotion   | Need             | Recommended Content | Platform   |
| ----- | --------- | ---------------- | ------------------- | ---------- |
| Elif  | Stress    | Relaxation       | LoFiPlaylist        | Spotify    |
| Deniz | Sadness   | EmotionalSupport | ComfortMovie        | Netflix    |
| Büşra | Boredom   | Distraction      | PuzzleGame          | Mobile App |
| Enes  | Tiredness | Motivation       | MotivationalPodcast | Spotify    |

---

## Repository Structure

```text
emotion-aware-recommendation-ontology/
│
├── ontology_v2.ttl
├── shapes.ttl
├── validate_shacl.py
├── SPARQL_Queries.md
├── README.md
├── docs/
│   └── Widoco Documentation
└── ORSD/
```

---

## Technologies

* OWL 2
* RDF
* Turtle (.ttl)
* GraphDB
* SPARQL
* SHACL
* pySHACL
* WIDOCO
* GitHub
* Python

---

## Authors

* Elif Özkanat (220315023)
* Büşra Pehlivanlar (220315051)
* Enes Ulucan (220315018)

**Course:** Knowledge Engineering and Ontologies — 2025–2026 Spring Semester

**Instructor:** Gamze Türkmen
