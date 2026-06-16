from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PdfMerger

import os


def merge_pdfs(files, output_path):

    merger = PdfMerger()

    for file in files:
        merger.append(file)

    merger.write(output_path)
    merger.close()


def split_pdf(
    input_path,
    split_points,
    output_folder
):

    reader = PdfReader(input_path)

    total_pages = len(reader.pages)

    print("TOTAL PAGES:", total_pages)

    split_points = sorted(split_points)

    # validation
    for point in split_points:

        if point <= 0:
            raise ValueError(
                "Split points must be > 0"
            )

        if point >= total_pages:
            raise ValueError(
                f"Split point {point} exceeds total pages"
            )

    all_points = [0] + split_points + [total_pages]

    output_files = []

    for i in range(len(all_points) - 1):

        start = all_points[i]
        end = all_points[i + 1]

        writer = PdfWriter()

        for page_num in range(start, end):
            writer.add_page(
                reader.pages[page_num]
            )

        output_path = os.path.join(
            output_folder,
            f"part_{i+1}.pdf"
        )

        with open(output_path, "wb") as f:
            writer.write(f)

        output_files.append(output_path)

    return output_files