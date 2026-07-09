from database.schema import create_schema
from system.application_scanner import ApplicationScanner
from system.application_indexer import ApplicationIndexer
from brain.fast_router import FastRouter


def main():

    create_schema()

    scanner = ApplicationScanner()
    scanner.scan()

    indexer = ApplicationIndexer()
    indexer.generate_aliases()
    indexer.close()

    router = FastRouter()

    while True:
        command = input("Jarvis > ")

        if command.lower() == "exit":
            break

        if not router.execute(command):
            print("Unknown command")

    router.close()


if __name__ == "__main__":
    main()