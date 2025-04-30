from flask import Blueprint, send_from_directory
import os

# ... existing code ...


@bp.route("/docs")
@bp.route("/docs/<path:path>")
def docs(path="index.html"):
    docs_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "docs", "_build", "html"
    )
    return send_from_directory(docs_path, path)


# ... existing code ...
