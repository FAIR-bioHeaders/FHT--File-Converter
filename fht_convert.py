import argparse
import sys
import textwrap

from fht import fht


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Convert from one FHT supported file type to another",
        epilog=textwrap.dedent(
            """\
                    positional <file> input and output files
                        input files can be one of:
                            <input>.yml
                            <input>.fasta  - fasta contining a fht header
                            <input>.html   - html containing microdata
                            <input>.json
                            <input>.gfa

                        output files can be one of:
                            <output>.yml
                            <output>.fasta - fasta output type will be made as a fasta header without sequences
                            <output>.html  - microdata output type will be made into generic html output
                            <output>.json
                            <output>.gfa
                            """
        ),
    )

    parser.add_argument(
        "file", nargs=2, metavar="<file>", help="input followed by output"
    )

    parser.add_argument("--version", action="version", version="%(prog)s 0.0.1")

    args = parser.parse_args()

    fht_to_be_converted = fht()

    with open(args.file[0], "r") as input_file:
        if args.file[0].endswith(".yml") or args.file[0].endswith(".yaml"):
            fht_to_be_converted.input_yaml(input_file)
        elif args.file[0].endswith(".fasta") or args.file[0].endswith(".fa"):
            fht_to_be_converted.input_fasta(input_file)
        elif args.file[0].endswith(".json"):
            fht_to_be_converted.input_json(input_file)
        elif args.file[0].endswith(".html"):
            fht_to_be_converted.input_microdata(input_file)
        elif args.file[0].endswith(".gfa"):
            fht_to_be_converted.input_gfa(input_file)
        else:
            sys.exit("Input file extention not found")

    original_stdout = sys.stdout

    with open(args.file[1], "w") as output_file:
        sys.stdout = output_file
        if args.file[1].endswith(".yml") or args.file[1].endswith(".yaml"):
            print(fht_to_be_converted.ouput_yaml())
        elif args.file[1].endswith(".fasta") or args.file[1].endswith(".fa"):
            print(fht_to_be_converted.output_fasta())
        elif args.file[1].endswith(".json"):
            print(fht_to_be_converted.output_json())
        elif args.file[1].endswith(".html"):
            print(fht_to_be_converted.output_microdata())
        elif args.file[1].endswith(".gfa"):
            print(fht_to_be_converted.output_gfa())
        else:
            sys.stdout = original_stdout
            sys.exit("Output file extention not found")

    sys.stdout = original_stdout
