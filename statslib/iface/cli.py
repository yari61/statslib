import sys
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_estimate = subparsers.add_parser("estimate")
data_group = parser_estimate.add_argument_group("data")
data_group.add_argument("-d", "--data-file", type=str)
functional_group = parser_estimate.add_argument_group("functional")
functional_group.add_argument("-c", "--config-module", type=str)
functional_group.add_argument("-m", "--method", type=str)
functional_group.add_argument("-l", "--length", type=int)
functional_group.add_argument("--ma-order", type=int)
functional_group.add_argument("--ma-params", type=float, nargs="+")
functional_group.add_argument("--ar-order", type=int)
functional_group.add_argument("--ar-params", type=float, nargs="+")
parser_estimate.set_defaults(which="estimate")

parser_graph = subparsers.add_parser("graph")
parser_graph.add_argument("-i", "--index", type=int)
parser_graph.set_defaults(which="graph")

if __name__ == "__main__":
    args = sys.argv[1:]
    args = parser.parse_args(args)
    print(args)
