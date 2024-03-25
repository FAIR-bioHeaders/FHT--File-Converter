import argparse
import sys
import textwrap

from fht import fht


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Validate a FHT metadata file",
        epilog=textwrap.dedent(
            """\
                    positional <file> input and output files
                        input files can be one of:
                            <input>.yml
                            <input>.fasta  - fasta contining a fht header
                            <input>.html   - html containing microdata
                            <input>.json   - json containing a fht header
                            <input>.gfa    - gfa file contining a fht header
                            """
        ),
    )

    parser.add_argument(
        "file", nargs=1, metavar="<file>", help="input followed by output"
    )

    parser.add_argument("--version", action="version", version="%(prog)s 0.0.1")

    args = parser.parse_args()

    fht_to_be_validated = fht()

    with open(args.file[0], "r") as input_file:
        if args.file[0].endswith(".yml") or args.file[0].endswith(".yaml"):
            fht_to_be_validated.input_yaml(input_file)
        elif args.file[0].endswith(".fasta") or args.file[0].endswith(".fa"):
            fht_to_be_validated.input_fasta(input_file)
        elif args.file[0].endswith(".json"):
            fht_to_be_validated.input_json(input_file)
        elif args.file[0].endswith(".html"):
            fht_to_be_validated.input_microdata(input_file)
        elif args.file[0].endswith(".gfa"):
            fht_to_be_validated.input_gfa(input_file)
        else:
            sys.exit("Input file extention not found")

    fht_to_be_validated.fht_validate()
