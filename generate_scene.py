import os
from lxml import etree
from datetime import datetime

SRC_FILE  = "resources/solo12.xml"
DST_FILE = "resources/solo12_gen.xml"

if __name__ == "__main__":
    # We do custom parsing and inclusion of the elements in order to reuse includes.
    # MuJoCo doesn't allow the same file to be included twice in a model, and this
    # solution is simpler than PyMJCF.
    tree = etree.parse(SRC_FILE)

    # We introduce a custom <include_with_attrs> element which is required to have
    # the "from" attribute with a relative path to a valid .xml file.
    # It optionally has other attributes as well.
    # When the parser encounters an <include_with_attrs>, it parses the referenced
    # .xml, discards the root element and adds all its children to the original
    # element that owned the <include_with_attrs>.
    # All attributes other than "from" will be recursively added to
    # every imported element. Collisions will be overwritten.
    # Note:
    #  - One pass is performed therefore recursive imports are not resolved
    includes = list(tree.iter("include_with_attrs"))
    
    for include in includes:
        if (src_path := include.get("from")) is None:
            raise ValueError(
                f"Missing 'from' attribute in <include_with_attrs>" +
                f"at line {include.sourceline} of {SRC_FILE}"
            )

        parent = include.getparent()
        attrs = [attr for attr in include.items() if attr[0] != "from"]
        subt = etree.parse(os.path.join(os.path.dirname(SRC_FILE), src_path))

        # Set extra attributes:
        for child in subt.iter():
            list(child.set(*attr) for attr in attrs)

        # Append subelements to original tree:
        for child in subt.findall("*"):
            parent.append(child)

    # Collect and delete all <include_with_attrs> elements:
    for elem in list(tree.iter("include_with_attrs")):
        elem.getparent().remove(elem)

    # Add comment that file was autogenerated:
    comment = etree.Comment(f"""
    ==================================
    This file was autogenerated from {SRC_FILE} by {os.path.basename(__file__)} on {datetime.now().strftime("%d/%m/%y %H:%M")}.
    The original .xml included {len(includes)} <include_with_attrs> elements.
    ==================================
    """)

    tree.getroot().addprevious(comment)

    # Write output:
    tree.write(DST_FILE, with_tail = True)