import zipfile
import os

def create_zip(files, zip_path):

    print("FILES TO ZIP:", files)

    with zipfile.ZipFile(zip_path, "w") as zipf:

        for file in files:

            print("ADDING TO ZIP:", file)

            zipf.write(
                file,
                arcname=os.path.basename(file)
            )

    print("ZIP CREATED:", zip_path)