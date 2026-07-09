from brain.nlu.engine import NLUEngine

nlu = NLUEngine()

while True:

    text = input("> ")

    intent = nlu.process(text)

    print(intent)