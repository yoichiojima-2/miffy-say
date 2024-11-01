from argparse import ArgumentParser, Namespace


def main(msg: str) -> str:
    return f" () () \n(・x・)  <  {msg}"


def parse_args() -> Namespace:
    parser = ArgumentParser() 
    parser.add_argument("--message", "-m", type=str, default = "say what you want me to say")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(main(args.message))
