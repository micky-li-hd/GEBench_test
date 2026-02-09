"""Command-line interface for GUI Agent."""

import argparse
from pathlib import Path

from .api import Generator, Evaluator
from .config import GenerationConfig, EvaluationConfig


def generate_command(args):
    """Handle generation command."""
    config = GenerationConfig(
        provider=args.provider,
        api_key=args.api_key,
        output_dir=Path(args.output_dir),
    )

    generator = Generator(config)
    generator.generate(
        data_type=args.data_type,
        data_folder=Path(args.data_folder),
        workers=args.workers,
    )

    print("Generation complete!")


def evaluate_command(args):
    """Handle evaluation command."""
    config = EvaluationConfig(
        judge=args.judge,
        api_key=args.api_key,
        dataset_root=Path(args.dataset_root) if args.dataset_root else None,
    )

    evaluator = Evaluator(config)
    results = evaluator.evaluate(
        data_type=args.data_type,
        output_folder=Path(args.output_folder),
        workers=args.workers,
    )

    print(f"Evaluation complete! Evaluated {len(results)} samples.")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="GUI Agent - GUI Generation & Evaluation Toolkit")
    subparsers = parser.add_subparsers(help="Available commands")

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate GUIs")
    gen_parser.add_argument("--data-type", required=True, choices=["type1", "type2", "type3", "type4", "type5"])
    gen_parser.add_argument("--data-folder", required=True, help="Input data folder")
    gen_parser.add_argument("--provider", default="gemini", choices=["gemini", "gpt", "seedream"])
    gen_parser.add_argument("--api-key", required=True, help="API key for provider")
    gen_parser.add_argument("--output-dir", default="outputs/", help="Output directory")
    gen_parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers")
    gen_parser.set_defaults(func=generate_command)

    # Evaluate command
    eval_parser = subparsers.add_parser("evaluate", help="Evaluate generated GUIs")
    eval_parser.add_argument("--data-type", required=True, choices=["type1", "type2", "type5"])
    eval_parser.add_argument("--output-folder", required=True, help="Folder with generated outputs")
    eval_parser.add_argument("--judge", default="gpt4o", choices=["gpt4o", "gemini", "qwen_vl"])
    eval_parser.add_argument("--api-key", required=True, help="API key for evaluator")
    eval_parser.add_argument("--dataset-root", help="Root directory of original dataset (required for Type 1/2)")
    eval_parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers")
    eval_parser.set_defaults(func=evaluate_command)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()
