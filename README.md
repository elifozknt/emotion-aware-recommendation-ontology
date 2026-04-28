Emotion-Aware Intelligent Recommendation Ontology
Description
This project presents an ontology for modeling an intelligent recommendation system based on user emotions, needs, context, personality traits, preferences, and content effects. The system matches a user's current emotional state and situational context to appropriate digital content, generating personalized recommendations with confidence scores and feedback tracking.
Domain
Emotion-aware recommendation systems / Affective computing.
Purpose
The purpose of this ontology is to provide personalized content recommendations according to a user's emotional state and contextual situation.
Scope
This ontology includes concepts such as user, emotion, need, content, context, personality, preference, recommendation, platform, and feedback. It does not include medical diagnosis or clinical decision-making.
Example Scenario
A user named Elif feels stressed at night and is alone at home → the system identifies her need for relaxation → recommends a calming lo-fi playlist available on Spotify → logs a confidence score of 0.92 and collects feedback.

Main Concepts (Classes)
ClassDescriptionUserA person who receives recommendationsEmotionAn emotional state experienced by a user (e.g., Stress, Sadness, Anxiety)NeedA user need arising from an emotion (e.g., Relaxation, Motivation)ContentA digital content item that can be recommended (e.g., LoFiPlaylist, PuzzleGame)RecommendationA personalized suggestion generated for a userContextThe situation in which the user is locatedTimeContextSubclass of Context — time of day (Morning, Evening, Night)EnvironmentSubclass of Context — physical/social environment (Home, Alone, WithFriends)PersonalityA personality trait affecting recommendation suitabilityPreferenceA user's preferred content typeEffectThe expected psychological effect of a content itemPlatformThe digital platform where content is deliveredFeedbackA user's response to a recommendation

Key Relationships (Properties)

User → feels → Emotion
Emotion → createsNeed → Need
Need → satisfiedBy → Content
Content → hasEffect → Effect
Effect → relievesEmotion → Emotion
Recommendation → givenTo → User
Recommendation → includesContent → Content
Recommendation → basedOnEmotion → Emotion
Recommendation → considersContext → Context


Design Decisions
Why these classes?
We started from the ORSD competency questions and worked backwards. Every class exists because it is needed to answer at least one competency question via a SPARQL query. For example, Effect was included (rather than just linking content to emotion directly) because CQ4 asks specifically what effect a content item has — this requires Effect to be a first-class entity, not just a property value.
Why is Context split into TimeContext and Environment?
Context has many dimensions. Rather than a single free-text field, we modeled time and environment as separate subclasses so they can be queried independently (e.g., "all content suitable for night" vs. "all content suitable for home"). This also allows a recommendation to consider multiple context dimensions simultaneously.
Why Feedback and Recommendation as separate classes?
Feedback is not part of the recommendation itself — it is a response that comes after. Keeping them separate allows the system to track multiple feedbacks per recommendation over time and makes the data property hasFeedbackScore cleanly scoped.
Why use rdfs:subClassOf for TimeContext and Environment?
Both are types of Context, and queries that target Context generically (e.g., CQ6 and CQ9) should automatically include both subclasses. Using rdfs:subClassOf enables this without requiring separate query branches.
Ontology reuse
For this initial phase we used a custom namespace (ex:). In future iterations we plan to align with established vocabularies such as MFOEM (emotion ontology), Schema.org for content metadata, and FOAF for user identity.

Instances (ABox)
The ontology includes four complete scenario instances:
UserEmotionNeedRecommended ContentPlatformElifStressRelaxationLo-Fi PlaylistSpotifyDenizSadnessEmotional SupportComfort MovieNetflixBüşraBoredomDistractionPuzzle GameMobile AppEnesTirednessMotivationMotivational PodcastSpotify

Files
FileDescriptionontology.ttlOWL ontology in Turtle format (TBox + ABox)orsd-template (Elif Özkanat...).pdfOntology Requirements Specification Document (ORSD)

Technologies

OWL 2
RDF
Turtle (.ttl)
GitHub


Authors

Elif Özkanat (220315023)
Büşra Pehlivanlar (220315051)
Enes Ulucan (220315018)

Course: Knowledge Engineering and Ontologies — 2025–2026 Spring Semester
