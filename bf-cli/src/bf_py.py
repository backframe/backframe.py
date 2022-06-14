import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="bf-py",
        usage="bf-py [OPTIONS] COMMAND [ARGS]...",
        description="A framework for rapid development and deployment of APIs",
        exit_on_error=True,
        add_help=True
    )
    parser.add_argument("-v", "--version")

    sub = parser.add_subparsers(title="COMMANDS")
    sub.add_parser(
        name="generate"
    ).add_argument("-g", help="Whether to add version control to the program or not")

    parser.parse_args()


if __name__ == "__main__":
    main()