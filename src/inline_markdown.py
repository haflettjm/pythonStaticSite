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
    new_nodes =[]
    for node in old_nodes:
        ## check to see if empty if empty don't append skip
        if len(node.text) < 1:
            continue
        ## now we grab all matches
        extracted = extract_markdown_images(node.text)
        ## if there are no matches just append
        if len(extracted) < 2:
            new_nodes.append(node)
        new_nodes.append(node)
    return new_nodes

def extract_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        extracted = extract_nodes_link(node.text)
        if len(extracted) < 2:
            new_nodes.append(node)
        for extract in extracted:
            print("extracts: \n")
            print(extract)
            print("\n")
        new_nodes.append(node)
    return new_nodes
