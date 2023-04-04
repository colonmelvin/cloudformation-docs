import yaml
import sys
from cfn_tools import load_yaml, dump_yaml


def generate_documentation(template_file):
    with open(template_file, 'r') as file:
        content = load_yaml(file)

    parameters = content.get('Parameters', {})
    outputs = content.get('Outputs', {})
    resources = content.get('Resources', {})

    print("# AWS CloudFormation Template Documentation")
    print("\n## Parameters")
    print("\n| Name | Description | Type | Default |")
    print("|------|-------------|------|---------|")
    for key, value in parameters.items():
        name = key
        description = value.get('Description', '')
        type_ = value.get('Type', '')
        default = value.get('Default', '')
        print(f"| {name} | {description} | {type_} | {default} |")

    print("\n## Outputs")
    print("\n| Name | Description |")
    print("|------|-------------|")
    for key, value in outputs.items():
        name = key
        description = value.get('Description', '')
        print(f"| {name} | {description} |")

    print("\n## Resources")
    print("\n| Name | Type |")
    print("|------|------|")
    for key, value in resources.items():
        name = key
        type_ = value.get('Type', '')
        url = f"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-{type_.lower().replace('::', '-').replace('aws-', '')}.html"
        print(f"| [{name}]({url}) | {type_} |")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cfn_docs.py <path_to_cloudformation_template>")
        sys.exit(1)
    else:
        template_file = sys.argv[1]
        generate_documentation(template_file)
