from core.application import Application


def main():

    app = Application()

    app.logger.info("Project-Abyss Started")

    app.logger.info(
        f"Assistant: {app.config.get('assistant.name')}"
    )


if __name__ == "__main__":
    main()