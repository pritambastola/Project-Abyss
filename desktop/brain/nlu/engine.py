from brain.nlu.cleaner import Cleaner
from brain.nlu.tokenizer import Tokenizer
from brain.nlu.entity_extractor import EntityExtractor
from brain.nlu.intent_detector import IntentDetector
from brain.nlu.confidence import ConfidenceScorer
from brain.nlu.synonym_resolver import SynonymResolver

class NLUEngine:

    def __init__(self):

        self.cleaner = Cleaner()

        self.tokenizer = Tokenizer()

        self.extractor = EntityExtractor()

        self.detector = IntentDetector()

        self.confidence = ConfidenceScorer()

        self.synonyms = SynonymResolver()

    def process(self, text):

        cleaned = self.cleaner.clean(text)

        tokens = self.tokenizer.tokenize(cleaned)

        # Resolve synonyms BEFORE anything else
        tokens = self.synonyms.resolve(tokens)

        entities = self.extractor.extract(tokens)

        intent = self.detector.detect(
            tokens,
            entities
        )

        intent.original_text = text
        intent.cleaned_text = cleaned
        intent.tokens = tokens

        intent = self.confidence.score(intent)

        return intent