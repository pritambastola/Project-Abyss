from rapidfuzz import process


class Matcher:

    def best(self, word, choices):

        result = process.extractOne(word, choices)

        if result is None:
            return word

        choice, score, _ = result

        if score >= 85:
            return choice

        return word