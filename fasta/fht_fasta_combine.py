import argparse
import os
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
                            <input>.json
                            <input>.gfa

                            second input must be a fasta file
                            """
        ),
    )

    parser.add_argument(
        "file", nargs=2, metavar="<file>", help="input followed by fasta output"
    )

    parser.add_argument("--version", action="version", version="%(prog)s 0.0.1")

    args = parser.parse_args()

    fht_to_be_combined = fht()

    with open(args.file[0], "r") as input_file:
        if args.file[0].endswith(".yml") or args.file[0].endswith(".yaml"):
            fht_to_be_combined.input_yaml(input_file)
        elif args.file[0].endswith(".fasta") or args.file[0].endswith(".fa"):
            fht_to_be_combined.input_fasta(input_file)
        elif args.file[0].endswith(".json"):
            fht_to_be_combined.input_json(input_file)
        elif args.file[0].endswith(".html"):
            fht_to_be_combined.input_microdata(input_file)
        else:
            sys.exit("Input file extention not found")

    output_filename = os.path.splitext(args.file[1])[0] + ".fht.fasta"

    with open(args.file[0], "r") as sources:
        fasta_lines = sources.readlines()

    with open(output_filename, "w") as output_file:
        output_content = fht_to_be_combined.output_fasta()
        output_file.write(output_content)
        for line in fasta_lines:
            output_file.write(line)
