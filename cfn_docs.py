import sys
import yaml
from cfn_tools import load_yaml, dump_yaml


def generate_documentation(template_file):
    with open(template_file, 'r') as file:
        content = load_yaml(file)

    parameters = content.get('Parameters', {})
    outputs = content.get('Outputs', {})
    resources = content.get('Resources', {})

    markdown_content = "# AWS CloudFormation Template Documentation\n"
    markdown_content += "\n## Parameters\n"
    markdown_content += "\n| Name | Description | Type | Default |\n"
    markdown_content += "|------|-------------|------|---------|\n"
    for key, value in parameters.items():
        name = key
        description = value.get('Description', '')
        type_ = value.get('Type', '')
        default = value.get('Default', '')
        markdown_content += f"| {name} | {description} | {type_} | {default} |\n"

    markdown_content += "\n## Outputs\n"
    markdown_content += "\n| Name | Description |\n"
    markdown_content += "|------|-------------|\n"
    for key, value in outputs.items():
        name = key
        description = value.get('Description', '')
        markdown_content += f"| {name} | {description} |\n"

    markdown_content += "\n## Resources\n"
    markdown_content += "\n| Name | Type |\n"
    markdown_content += "|------|------|\n"
    for key, value in resources.items():
        name = key
        type_ = value.get('Type', '')
        url = f"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-{type_.lower().replace('::', '-').replace('aws-', '')}.html"
        markdown_content += f"| [{name}]({url}) | {type_} |\n"

    return markdown_content



def write_to_file(filename, content):
    with open(filename, 'wt') as file:
        file.write(content)


def main():
    if len(sys.argv) < 3:
        print("Usage: python cfn_docs.py <path_to_cloudformation_template> <output_filename>  [--preview]")
        sys.exit(1)
    else:
        template_file = sys.argv[1]
        output_filename = sys.argv[2]
        markdown_content = generate_documentation(template_file)
        if '--preview' in sys.argv:
            print(markdown_content)
            confirm = input(f"Write to file '{output_filename}'? (Y/N): ")
            if confirm.lower() == 'y':
                write_to_file(output_filename, markdown_content)
                print(f"Markdown content has been written to '{output_filename}'.")
            else:
                print("Operation cancelled.")  
        else:
            write_to_file(output_filename, markdown_content)


if __name__ == "__main__":
    main()
