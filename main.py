from src.managers.managers import CliRSScraper


def main():
    manager = CliRSScraper()
    manager.write_data()


if __name__ == "__main__":
    main()
