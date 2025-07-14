from pathlib import Path


def save_persona(username, persona_text):
    Path("output").mkdir(exist_ok=True)
    filepath = f"output/{username}_persona.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to: {filepath}")
