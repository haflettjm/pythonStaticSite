import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes):
    return new_nodes

def extract_nodes_link(old_nodes):
    new_nodes =[]
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        ## check to see if empty if empty don't append skip
        ## now we grab all matches
        extracted_links = extract_markdown_links(node.text)

        ## if there are no matches just append
        if len(extracted.links) < 2:
            new_nodes.append(node)
        sections = node.text.split(f"![{image_alt}]({image_link})",1)
        new_nodes.append(node)
        print(new_nodes)
    return new_nodes
