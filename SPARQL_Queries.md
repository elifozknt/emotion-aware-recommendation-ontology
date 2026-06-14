# SPARQL Queries

This file contains the SPARQL queries used to test and demonstrate the Emotion-Aware Intelligent Recommendation Ontology in GraphDB.

## Common Prefixes

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
```

---

## Q1 – Repository Sanity Check

This query checks whether the ontology triples were loaded into GraphDB successfully.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT * 
WHERE {
  ?s ?p ?o .
}
LIMIT 100
```

Expected result: The query returns ontology triples from the repository.

---

## Q2 – Retrieve Users and Their Emotions

This query retrieves each user and the emotional state associated with that user.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?user ?emotion
WHERE {
  ?user rdf:type ex:User .
  ?user ex:feels ?emotion .
}
```

Expected result: Elif–Stress, Busra–Boredom, Enes–Tiredness, Deniz–Sadness.

---

## Q3 – Retrieve Users with Negative Emotions

This query uses the emotion class hierarchy and retrieves only users whose emotion is typed as `ex:NegativeEmotion`.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?user ?emotion
WHERE {
  ?user ex:feels ?emotion .
  ?emotion rdf:type ex:NegativeEmotion .
}
```

Expected result: Elif–Stress, Enes–Tiredness, Deniz–Sadness.

---

## Q4 – Personality-Based Content Recommendation

This query retrieves content suitable for a user according to the user's personality profile.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>

SELECT ?user ?personality ?content
WHERE {
  ?user ex:hasPersonality ?personality .
  ?content ex:suitableForPersonality ?personality .
}
```

Expected result: Introvert users receive LoFiPlaylist and BreathingExercise; extrovert users receive ComfortMovie.

---

## Q5 – Emotion-Based Need and Content Recommendation

This query demonstrates the main recommendation logic: user emotion creates a need, and that need is satisfied by suitable content.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>

SELECT ?user ?emotion ?need ?content
WHERE {
  ?user ex:feels ?emotion .
  ?emotion ex:createsNeed ?need .
  ?need ex:satisfiedBy ?content .
}
```

Expected result: Stress produces Relaxation and returns LoFiPlaylist/BreathingExercise; Boredom produces Distraction and returns PuzzleGame; Tiredness produces Motivation and returns MotivationalPodcast; Sadness produces EmotionalSupport and returns ComfortMovie.

---

## Q6 – Count Users by Emotion Type

This aggregation query counts how many users belong to each emotion category.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?emotionType (COUNT(?user) AS ?userCount)
WHERE {
  ?user ex:feels ?emotion .
  ?emotion rdf:type ?emotionType .
  FILTER(?emotionType IN (ex:NegativeEmotion, ex:NeutralEmotion, ex:PositiveEmotion))
}
GROUP BY ?emotionType
```

Expected result: NegativeEmotion = 3, NeutralEmotion = 1.

---

## Q7 – Retrieve Dynamic Emotion Intensity

This query retrieves dynamic emotion observations and their intensity levels.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>

SELECT ?user ?dynEmotion ?intensity
WHERE {
  ?user ex:hasDynamicEmotion ?dynEmotion .
  ?dynEmotion ex:hasIntensityLevel ?intensity .
}
ORDER BY DESC(?intensity)
```

Expected result: ElifStressHigh = 0.85, EnesLowMotivationMorning = 0.65.

---

## Q8 – Retrieve Session Interaction Logs

This query retrieves the interaction events recorded in an emotion session.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>

SELECT ?session ?interaction ?content ?type
WHERE {
  ?session ex:hasInteraction ?interaction .
  ?interaction ex:interactedWith ?content .
  ?interaction ex:hasInteractionType ?type .
}
```

Expected result: Session001 contains Interaction001 with LoFiPlaylist as play and Interaction002 with BreathingExercise as complete.

---

## Q9 – Retrieve Content Platform Availability

This query retrieves which content items are available on which platforms.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>

SELECT ?content ?platform
WHERE {
  ?content ex:availableOnPlatform ?platform .
}
```

Expected result: LoFiPlaylist and MotivationalPodcast are available on Spotify; ComfortMovie is available on Netflix; BreathingExercise, MeditationAudio, and PuzzleGame are available on MobileApp.

---

## Q10 – Retrieve Data Provenance for Interactions

This query retrieves the data source used to populate user interaction instances.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>

SELECT ?interaction ?source ?url
WHERE {
  ?interaction ex:populatedFrom ?source .
  ?source ex:hasSourceURL ?url .
}
```

Expected result: Interaction001 and Interaction002 are populated from SpotifyAPISource.

---

## Q11 – Track Emotion Change Over Time

This query demonstrates temporal emotion modeling by retrieving emotion transitions.

```sparql
PREFIX ex: <http://example.org/emotion-aware-recommendation#>

SELECT ?fromEmotion ?toEmotion
WHERE {
  ?fromEmotion ex:changesOverTime ?toEmotion .
}
```

Expected result: ElifStressLow changes over time to ElifStressHigh.
