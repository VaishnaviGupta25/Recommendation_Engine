def recommend_assessments(user_input, assessments):
    recommendations = []

    for assessment in assessments:
        score = 0

        # Match level
        if assessment["level"] == user_input["level"] or assessment["level"] == "All":
            score += 1

        # Match industry
        if assessment["industry"] == user_input["industry"] or assessment["industry"] == "All":
            score += 1

        # Match skills
        for skill in user_input["skills"]:
            if skill in assessment["skills"]:
                score += 2

        if score > 0:
            recommendations.append((assessment["name"], score))

    # Sort by highest score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return [r[0] for r in recommendations]