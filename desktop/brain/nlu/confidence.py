class ConfidenceScorer:

    def score(self, intent):

        score = 0.0

        if intent.action:
            score += 0.4

        if intent.target:
            score += 0.4

        if intent.entities:
            score += 0.2

        intent.confidence = score

        return intent