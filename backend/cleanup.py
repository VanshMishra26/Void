import os
import shutil

from datetime import datetime
from datetime import timedelta

OUTPUT_FOLDER = "outputs"

MAX_AGE_HOURS = 24

now = datetime.now()

for folder in os.listdir(
    OUTPUT_FOLDER
):

    path = os.path.join(
        OUTPUT_FOLDER,
        folder
    )

    if not os.path.isdir(path):
        continue

    created = datetime.fromtimestamp(
        os.path.getctime(path)
    )

    age = now - created

    if age > timedelta(
        hours=MAX_AGE_HOURS
    ):

        print(
            "Deleting:",
            path
        )

        shutil.rmtree(path)