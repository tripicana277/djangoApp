import csv
import io
import xml.etree.ElementTree as ET
from xml.dom import minidom


def parse_txt_to_rows(file_obj, encoding="utf-8"):
    text = file_obj.read().decode(encoding)
    reader = csv.reader(io.StringIO(text))
    rows = [row for row in reader if row]
    return text, rows


def rows_to_xml(rows):
    root = ET.Element("records")

    for row in rows:
        record_elem = ET.SubElement(root, "record")
        for idx, value in enumerate(row, start=1):
            col_elem = ET.SubElement(record_elem, f"col{idx}")
            col_elem.text = value

    # ElementTree → XML文字列
    rough_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    # minidom で整形（改行 & インデント）
    parsed = minidom.parseString(rough_xml)
    pretty_xml = parsed.toprettyxml(
        indent="  ", encoding="utf-8"
    )  # ← 2スペースインデント

    return pretty_xml.decode("utf-8")
