#!/bin/bash
# Download Moritz Bromme - Lebensgeschichte eines modernen Fabrikarbeiters from Zeno.org

BASE="http://www.zeno.org/Kulturgeschichte/M/Bromme,+Moritz+Theodor+William/Lebensgeschichte+eines+modernen+Fabrikarbeiters"
OUTDIR="/root/.openclaw/workspace/teaching/mammutprojekt/konzept-v2/quellen/arbeiter-autobiografien"
OUTFILE="$OUTDIR/bromme-lebensgeschichte.txt"

echo "# Moritz Bromme: Lebensgeschichte eines modernen Fabrikarbeiters (1905)" > "$OUTFILE"
echo "# Quelle: Zeno.org" >> "$OUTFILE"
echo "" >> "$OUTFILE"

chapters=(
    "Zur+Einleitung"
    "Meine+Gro%C3%9Feltern"
    "Meine+Eltern"
    "Meine+Kindheit+in+Schm%C3%B6lln"
    "In+den+Steinnu%C3%9Fkopffabriken+Schm%C3%B6llns"
    "Meine+Kellnerlaufbahn"
    "Pantoffelmacher"
    "In+Ronneburg,+den+neuen+Heimat"
    "Ein+Jahr+der+Unordnung"
    "Arbeitskollegen+und+Andere"
    "Verheiratet"
    "In+der+Gerarer+Werkzeug-+und+Maschinenfabrik+Wesselmann+Bohrer+&+Co."
    "In+der+Lungenheilanstalt"
    "Mein+Familienleben"
)

for chapter in "${chapters[@]}"; do
    echo "Downloading: $chapter"
    url="$BASE/$chapter"
    # Extract text using lynx
    lynx -dump -nolist "$url" 2>/dev/null | \
        sed -n '/^$/,/ZenoServer/p' | \
        head -n -5 >> "$OUTFILE"
    echo "" >> "$OUTFILE"
    echo "---" >> "$OUTFILE"
    echo "" >> "$OUTFILE"
    sleep 1
done

echo "Done! Saved to $OUTFILE"
wc -l "$OUTFILE"
