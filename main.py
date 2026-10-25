"""Interfaz de consola del analizador."""

import argparse
import json

from analyzer import analyze_text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analiza un texto y devuelve JSON.")
    parser.add_argument("text", help="Texto entre comillas")
    args = parser.parse_args(argv)
    print(json.dumps(analyze_text(args.text), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
