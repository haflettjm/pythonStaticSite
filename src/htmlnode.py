class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        string = ""
        if self.props != None:
            for label, prop in self.props.items():
                string += f'{label}="{prop}" '
        string = string.strip()
        return string
    
    def __eq__(self, node):
        if self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props:
            return True
        return False
    
    def __repr__(self):
        children = ""
        if self.children != None:
            for child in self.children:
                children = f'{child} '
        props = self.props_to_html()

        return f'HTMLNode(tag:{self.tag}, value:{self.value}, children:{children}, props:{props})'

