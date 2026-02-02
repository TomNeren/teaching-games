#!/bin/bash
# Mammutprojekt - Bild & Musik Generierung
# Verwendet Hugging Face Router API

set -e

HF_TOKEN=$(grep HF_TOKEN /root/.openclaw/.env | cut -d= -f2)
IMG_DIR="/root/.openclaw/workspace/teaching/mammutprojekt/prototype/images/generated"
AUDIO_DIR="/root/.openclaw/workspace/teaching/mammutprojekt/prototype/audio/music"

mkdir -p "$IMG_DIR" "$AUDIO_DIR"

STYLE="1930s Germany, sepia toned historical photograph, atmospheric, cinematic, "

echo "════════════════════════════════════════════════════"
echo "  Mammutprojekt - Asset Generation"
echo "════════════════════════════════════════════════════"

generate_image() {
    local name=$1
    local prompt=$2
    local output="$IMG_DIR/${name}.jpg"
    
    if [[ -f "$output" ]]; then
        echo "  ⏭️  $name (existiert)"
        return
    fi
    
    echo -n "  🎨 $name..."
    
    curl -s -X POST \
        "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell" \
        -H "Authorization: Bearer $HF_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"inputs\": \"${STYLE}${prompt}\"}" \
        -o "$output"
    
    if file "$output" | grep -q "image"; then
        echo " ✓"
    else
        echo " ✗"
        rm -f "$output"
    fi
    sleep 2
}

generate_music() {
    local name=$1
    local prompt=$2
    local output="$AUDIO_DIR/${name}.flac"
    
    if [[ -f "$output" ]]; then
        echo "  ⏭️  $name (existiert)"
        return
    fi
    
    echo -n "  🎵 $name..."
    
    curl -s -X POST \
        "https://router.huggingface.co/hf-inference/models/facebook/musicgen-small" \
        -H "Authorization: Bearer $HF_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"inputs\": \"$prompt\"}" \
        -o "$output"
    
    if file "$output" | grep -qE "audio|FLAC"; then
        echo " ✓"
    else
        echo " ✗"
        rm -f "$output"
    fi
    sleep 3
}

echo ""
echo "=== BILDER ==="
echo ""

# Werner (Zuschauer)
generate_image "werner_apartment" "modest German apartment interior 1938, wooden furniture, radio, warm evening light"
generate_image "werner_window" "view through window at night, distant orange flames, smoke, worried observer"
generate_image "werner_street" "German street at night 1938, broken glass, smoke, Kristallnacht chaos"
generate_image "werner_helping" "two men in 1930s coats, one helping another into doorway, dark street, courage"
generate_image "werner_morning" "German street morning, broken shop windows, Star of David, people looking down"

# David (Opfer)
generate_image "david_school" "Jewish boy outside school gates 1935, excluded, lonely, other children walking past"
generate_image "david_star" "yellow Star of David sewn onto coat, hands sewing, 1941"
generate_image "david_family" "Jewish family at dinner table 1930s, Shabbat candles, worried faces"
generate_image "david_hiding" "young person in dark cramped attic, fear, light through cracks"
generate_image "david_train" "train platform 1941, Jewish families with suitcases, deportation, farewell"

# Allgemein
generate_image "synagogue" "synagogue on fire at night 1938, flames, tragic destruction"
generate_image "boycott" "German shop 1933, Star of David on window, SA guards, boycott"

echo ""
echo "=== MUSIK ==="
echo ""

# Stimmungen
generate_music "peaceful" "gentle piano and violin, warm 1930s atmosphere, nostalgic, soft classical"
generate_music "hope" "hopeful orchestral strings, cello melody, tender emotional classical"
generate_music "tension" "dark orchestral tension, low strings tremolo, ominous suspenseful"
generate_music "danger" "urgent strings, dramatic timpani, threatening brass, dark classical"
generate_music "grief" "sorrowful violin solo, mourning cello, slow tempo, classical"
generate_music "farewell" "melancholic piano, tearful strings, bittersweet emotional"
generate_music "chaos" "chaotic orchestral, dissonant strings, violent brass, dramatic"
generate_music "courage" "brave orchestral theme, determined strings, quiet heroism"
generate_music "remember" "solemn orchestral memorial, dignified strings, classical requiem"

echo ""
echo "════════════════════════════════════════════════════"
echo "  ✓ Fertig!"
echo "  Bilder: $IMG_DIR"
echo "  Musik:  $AUDIO_DIR"
echo "════════════════════════════════════════════════════"
