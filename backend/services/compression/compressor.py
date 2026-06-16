from services.compression.pymupdf_compressor import (
    PyMuPDFCompressor
)

from services.compression.ghostscript_compressor import (
    GhostscriptCompressor
)

ENGINE = "pymupdf"

def get_compressor():

    if ENGINE == "pymupdf":
        return PyMuPDFCompressor()

    if ENGINE == "ghostscript":
        return GhostscriptCompressor()

    raise ValueError(
        f"Unknown engine: {ENGINE}"
    )


def compress_pdf(
    input_path,
    output_path
):

    compressor = get_compressor()

    compressor.compress(
        input_path,
        output_path
    )