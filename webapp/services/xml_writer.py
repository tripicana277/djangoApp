import xml.etree.ElementTree as ET
from io import BytesIO


def generate_xml(data: dict):
    root = ET.Element("root")

    for line in data["lines"]:
        item = ET.SubElement(root, "line")
        item.text = line

    tree = ET.ElementTree(root)

    buffer = BytesIO()
    tree.write(buffer, encoding="utf-8", xml_declaration=True)

    return buffer.getvalue()
