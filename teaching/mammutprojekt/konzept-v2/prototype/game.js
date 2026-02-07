// === Schicksalswege — Game Engine ===

// Game State
const gameState = {
    family: null,
    generation: 1,
    year: 1871,
    currentCharacter: null,
    legacy: {
        bildung: 0,
        vermoegen: 0,
        politisch: 0,  // -100 (konservativ) bis +100 (revolutionär)
        gesundheit: 100,
        ansehen: 50
    },
    history: [],
    currentScene: null
};

// Family Data
const families = {
    arbeiter: {
        name: "Schumann",
        type: "Arbeiterfamilie",
        color: "#8b0000",
        startCharacter: {
            name: "Heinrich Schumann",
            age: 28,
            portrait: "👨‍🔧",
            backstory: "Geboren in einem Dorf in Brandenburg, zog Heinrich mit 16 nach Berlin. Jetzt arbeitet er in einer Maschinenfabrik in Moabit. Seine Frau Anna und die kleine Tochter Martha leben mit ihm in einer Zwei-Zimmer-Wohnung in einer Mietskaserne."
        },
        startLegacy: { bildung: 10, vermoegen: 5, politisch: 20, gesundheit: 80, ansehen: 20 }
    },
    buerger: {
        name: "Hoffmann",
        type: "Bürgerfamilie",
        color: "#1e4d2b",
        startCharacter: {
            name: "Dr. Friedrich Hoffmann",
            age: 35,
            portrait: "👨‍⚕️",
            backstory: "Arzt in einer Kleinstadt nahe Freiburg. Friedrich führt eine gut gehende Praxis und ist Mitglied im Bildungsverein. Seine Frau Elisabeth kümmert sich um die drei Kinder und den Haushalt."
        },
        startLegacy: { bildung: 70, vermoegen: 50, politisch: 0, gesundheit: 90, ansehen: 70 }
    },
    juedisch: {
        name: "Goldstein",
        type: "Jüdische Familie",
        color: "#1a365d",
        startCharacter: {
            name: "Samuel Goldstein",
            age: 40,
            portrait: "👨‍💼",
            backstory: "Textilhändler in Berlin. Samuels Vater kam aus Posen, er selbst ist in Berlin geboren. Das Geschäft floriert, die Familie ist integriert — doch manchmal spürt Samuel die Blicke der anderen."
        },
        startLegacy: { bildung: 50, vermoegen: 60, politisch: 10, gesundheit: 85, ansehen: 45 }
    },
    adel: {
        name: "von Tresckow",
        type: "Adelsfamilie",
        color: "#4a1942",
        startCharacter: {
            name: "Major Otto von Tresckow",
            age: 45,
            portrait: "🎖️",
            backstory: "Gutsherr in der Mark Brandenburg. Otto diente im Krieg gegen Frankreich und kehrte mit dem Eisernen Kreuz zurück. Das Gut ist seit Generationen in Familienbesitz — doch die Zeiten ändern sich."
        },
        startLegacy: { bildung: 60, vermoegen: 80, politisch: -60, gesundheit: 75, ansehen: 90 }
    }
};

// Story Scenes
const scenes = {
    arbeiter: {
        intro: {
            year: 1871,
            image: "Berliner Mietskaserne, Hinterhof",
            text: `Der Januar ist bitterkalt. Heinrich kommt von der Frühschicht nach Hause. Zwölf Stunden an der Drehbank, die Finger steif vor Kälte.

In der Wohnung ist es kaum wärmer. Anna stillt die kleine Martha, die wieder hustet. "Die Kohlen sind fast alle", sagt sie leise.

Auf dem Tisch liegt ein Flugblatt. Jemand hat es im Treppenhaus gelassen. "Arbeiter aller Länder, vereinigt euch!" steht darauf.`,
            choices: [
                {
                    text: "Das Flugblatt lesen und behalten",
                    consequence: "→ Politisches Interesse wächst",
                    effects: { politisch: +10, ansehen: -5 },
                    nextScene: "bildungsverein"
                },
                {
                    text: "Das Flugblatt zum Anzünden benutzen — Wärme ist wichtiger",
                    consequence: "→ Pragmatisch bleiben",
                    effects: { gesundheit: +5 },
                    nextScene: "fabrikarbeit"
                },
                {
                    text: "Das Flugblatt dem Hausmeister zeigen — wer weiß, wer das verteilt",
                    consequence: "→ Ansehen bei der Obrigkeit steigt",
                    effects: { ansehen: +10, politisch: -15 },
                    nextScene: "anpassung"
                }
            ]
        },
        bildungsverein: {
            year: 1872,
            image: "Arbeiterbildungsverein, abends",
            text: `Ein Jahr ist vergangen. Heinrich hat angefangen, nach Feierabend den Arbeiterbildungsverein zu besuchen. 

Hier lernt er Lesen und Schreiben — richtig, nicht nur das bisschen aus der Dorfschule. Ein älterer Arbeiter, Karl, erklärt ihm die Ideen von Marx und Lassalle.

"Du hast Talent", sagt Karl eines Abends. "Du könntest Vorarbeiter werden. Oder —" er senkt die Stimme — "du könntest für die Sache arbeiten."`,
            choices: [
                {
                    text: "Sich für eine Beförderung zum Vorarbeiter empfehlen",
                    consequence: "→ Mehr Geld, aber weniger Zeit für die Bewegung",
                    effects: { vermoegen: +15, bildung: +5, politisch: -10 },
                    nextScene: "vorarbeiter"
                },
                {
                    text: "Aktiv in der Arbeiterbewegung werden",
                    consequence: "→ Riskant, aber sinnvoll",
                    effects: { politisch: +20, ansehen: -10, bildung: +10 },
                    nextScene: "bewegung"
                },
                {
                    text: "Beides versuchen — Familie und Überzeugung",
                    consequence: "→ Schwieriger Spagat",
                    effects: { bildung: +10, gesundheit: -10 },
                    nextScene: "balance"
                }
            ]
        },
        bewegung: {
            year: 1878,
            image: "Geheimes Treffen, Keller",
            text: `Die Sozialistengesetze sind in Kraft. Alles, wofür Heinrich gekämpft hat, ist jetzt verboten.

Aber die Bewegung lebt weiter — im Untergrund. Heinrich verteilt illegale Schriften, organisiert geheime Treffen. Es ist gefährlich. Verhaftungen sind an der Tagesordnung.

Die kleine Martha ist jetzt sieben. Sie fragt, warum Papa manchmal so spät nach Hause kommt.

Anna macht sich Sorgen. "Wenn sie dich erwischen, Heinrich..."`,
            choices: [
                {
                    text: "Weitermachen — die Sache ist wichtiger als die persönliche Sicherheit",
                    consequence: "→ Hohes Risiko, aber Überzeugung bleibt",
                    effects: { politisch: +25, ansehen: -20, gesundheit: -15 },
                    nextScene: "untergrund"
                },
                {
                    text: "Vorsichtiger werden — nur noch im Hintergrund helfen",
                    consequence: "→ Familie schützen, aber dabeibl bleiben",
                    effects: { politisch: +10, gesundheit: +5 },
                    nextScene: "vorsicht"
                },
                {
                    text: "Aufhören — die Familie geht vor",
                    consequence: "→ Sicherheit, aber Enttäuschung",
                    effects: { politisch: -20, gesundheit: +10, ansehen: +10 },
                    nextScene: "rueckzug"
                }
            ]
        }
        // More scenes would continue here...
    }
    // Other family storylines would be added here...
};

// === UI Functions ===

function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

function selectFamily(familyKey) {
    gameState.family = familyKey;
    const family = families[familyKey];
    
    // Set initial legacy
    gameState.legacy = { ...family.startLegacy };
    gameState.currentCharacter = family.startCharacter;
    
    // Update character intro screen
    document.getElementById('portrait-image').innerHTML = 
        `<span style="font-size: 5rem">${family.startCharacter.portrait}</span>`;
    
    document.getElementById('character-info').innerHTML = `
        <h3>${family.startCharacter.name}</h3>
        <p class="age">${family.startCharacter.age} Jahre alt • ${family.type}</p>
        <p class="backstory">${family.startCharacter.backstory}</p>
    `;
    
    // Set family color theme
    document.documentElement.style.setProperty('--current-family', family.color);
    
    showScreen('character-intro');
}

function startStory() {
    const familyScenes = scenes[gameState.family];
    if (familyScenes && familyScenes.intro) {
        loadScene(familyScenes.intro);
    } else {
        // Placeholder for families without scenes yet
        loadPlaceholderScene();
    }
    showScreen('story-scene');
}

function loadScene(scene) {
    gameState.currentScene = scene;
    
    // Update header
    document.getElementById('current-era').textContent = scene.year;
    document.getElementById('current-character').textContent = gameState.currentCharacter.name;
    
    // Update scene image
    document.getElementById('scene-image').innerHTML = 
        `<span style="opacity: 0.5">${scene.image}</span>`;
    
    // Update story text (convert line breaks)
    document.getElementById('story-text').innerHTML = 
        scene.text.split('\n\n').map(p => `<p>${p}</p>`).join('');
    
    // Generate choices
    const choicesContainer = document.getElementById('choices');
    choicesContainer.innerHTML = scene.choices.map((choice, index) => `
        <button class="choice-btn" onclick="makeChoice(${index})">
            ${choice.text}
            <span class="consequence">${choice.consequence}</span>
        </button>
    `).join('');
}

function loadPlaceholderScene() {
    const family = families[gameState.family];
    
    document.getElementById('current-era').textContent = '1871';
    document.getElementById('current-character').textContent = gameState.currentCharacter.name;
    
    document.getElementById('scene-image').innerHTML = 
        '<span style="opacity: 0.5">Szene wird geladen...</span>';
    
    document.getElementById('story-text').innerHTML = `
        <p><em>Die Geschichte der Familie ${family.name} beginnt hier.</em></p>
        <p>Diese Perspektive wird noch entwickelt. In der finalen Version werden hier die Entscheidungen und Schicksale der Familie erzählt.</p>
    `;
    
    document.getElementById('choices').innerHTML = `
        <button class="choice-btn" onclick="showScreen('family-select')">
            Andere Familie wählen
            <span class="consequence">→ Zurück zur Familienauswahl</span>
        </button>
    `;
}

function makeChoice(choiceIndex) {
    const scene = gameState.currentScene;
    const choice = scene.choices[choiceIndex];
    
    // Apply effects
    Object.keys(choice.effects).forEach(stat => {
        gameState.legacy[stat] = Math.max(0, Math.min(100, 
            gameState.legacy[stat] + choice.effects[stat]
        ));
    });
    
    // Record in history
    gameState.history.push({
        year: scene.year,
        choice: choice.text,
        effects: choice.effects
    });
    
    // Load next scene
    const familyScenes = scenes[gameState.family];
    if (familyScenes && familyScenes[choice.nextScene]) {
        setTimeout(() => {
            loadScene(familyScenes[choice.nextScene]);
        }, 300);
    } else {
        // End of available content
        showTransition();
    }
}

function showTransition() {
    document.getElementById('years-passing').textContent = 
        `${gameState.year} → ${gameState.year + 20}`;
    
    const legacySummary = document.getElementById('legacy-summary');
    legacySummary.innerHTML = `
        <h4>Was bleibt von ${gameState.currentCharacter.name}?</h4>
        <p>Bildung: ${getLegacyLevel(gameState.legacy.bildung)}</p>
        <p>Vermögen: ${getLegacyLevel(gameState.legacy.vermoegen)}</p>
        <p>Politische Haltung: ${getPoliticalStance(gameState.legacy.politisch)}</p>
        <p>Ansehen: ${getLegacyLevel(gameState.legacy.ansehen)}</p>
    `;
    
    showScreen('generation-transition');
}

function getLegacyLevel(value) {
    if (value < 20) return "sehr niedrig";
    if (value < 40) return "niedrig";
    if (value < 60) return "durchschnittlich";
    if (value < 80) return "hoch";
    return "sehr hoch";
}

function getPoliticalStance(value) {
    if (value < -60) return "streng konservativ";
    if (value < -20) return "konservativ";
    if (value < 20) return "gemäßigt";
    if (value < 60) return "liberal/progressiv";
    return "sozialistisch";
}

function continueToNextGeneration() {
    // Would load next generation here
    alert("Nächste Generation wird in der Vollversion verfügbar sein!");
    showScreen('start-screen');
}

function openFamilyTree() {
    document.getElementById('family-tree').classList.add('active');
}

function closeOverlay() {
    document.querySelectorAll('.overlay').forEach(o => o.classList.remove('active'));
}

// === Initialize ===
document.addEventListener('DOMContentLoaded', () => {
    showScreen('start-screen');
});
