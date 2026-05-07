def match_resume(text):
    skills = ["python", "fastapi", "aws", "docker"]

    matched = []

    for skill in skills:
        if skill.lower() in text.lower():
            matched.append(skill)

    score = len(matched) * 25

    return {
        "score": score,
        "matched_skills": matched
    }