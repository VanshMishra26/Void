import fitz
import os


class PyMuPDFCompressor:

    def compress(
        self,
        input_path,
        output_path
    ):

        before = os.path.getsize(
            input_path
        )

        doc = fitz.open(input_path)

        doc.save(
            output_path,
            garbage=4,
            deflate=True
        )

        doc.close()

        after = os.path.getsize(
            output_path
        )

        print(
            f"Compression: {before} -> {after}"
        )