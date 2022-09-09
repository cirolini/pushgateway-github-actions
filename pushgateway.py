import argparse
import ast
from prometheus_client import Info, push_to_gateway, CollectorRegistry

parser = argparse.ArgumentParser()
parser.add_argument('--pushgatey_url', help='URL of pushgateway')
parser.add_argument('--job', help='Job name')
parser.add_argument('--metric_name', help='The name of the metric you want to create/update')
parser.add_argument('--metric_description', help='The description of the metric you want to create/update')
parser.add_argument('--metric_labels', help='The list of labels for your metric')
args = parser.parse_args()

registry = CollectorRegistry()
i = Info(args.metric_name, args.metric_description, registry=registry)
i.info(ast.literal_eval(args.metric_labels))
push_to_gateway(args.pushgatey_url, job=args.job, registry=registry)
