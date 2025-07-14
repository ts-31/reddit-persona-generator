def build_prompt(username, posts, comments, mode="concise"):
    if mode == "detailed":
        return f"""
You are an AI tasked with building a detailed and human-like user persona from Reddit activity.

Instructions:
1. Analyze the user's posts and comments.
2. Create a persona that includes:
   - Age group (guess based on writing)
   - Occupation (if inferred)
   - Interests and hobbies
   - Personality traits
   - Online habits
   - Challenges or goals (if mentioned)
3. For each point in the persona, include a relevant quote from a post or comment.

Reddit User: u/{username}

Posts:
{chr(10).join(f"- {p}" for p in posts)}

Comments:
{chr(10).join(f"- {c}" for c in comments)}

Your output must be a structured persona in plain English with quotes in parentheses.
"""
    else:  # concise mode
        return f"""
You are an AI tasked with generating a **very short and high-level user persona** from Reddit activity.

🎯 Goal:
Summarize the user in a way that can be **read in 15–30 seconds**, like a quick internal profile.

📌 Instructions:
1. Analyze the user's posts and comments below.
2. Output a persona with these sections:
   - Age group (1 line)
   - Occupation (1 line)
   - Interests & hobbies (1–2 lines)
   - Personality traits (2 lines max)
   - Online habits (1 line)
   - Challenges or goals (1–2 lines)
3. Be **brief, bullet-pointed, and professional**.
4. Use **at most one short quote** total.
5. Do not write paragraphs or essays.
6. Keep total length under **150 words**.

👤 Reddit User: u/{username}

📝 Posts:
{chr(10).join(f"- {p}" for p in posts)}

💬 Comments:
{chr(10).join(f"- {c}" for c in comments)}

✍️ Output Format:
Start with `## Persona: u/{username}` and use **bold section titles** followed by 1–2 bullet points each. Do not exceed 150 words total.
"""
