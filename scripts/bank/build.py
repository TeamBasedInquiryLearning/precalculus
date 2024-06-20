import os
import shutil
from checkit.bank import Bank

# generate_images = input("Generate images? y/n ").strip().upper() == "Y"
# if generate_images:
#     print("regenerating images")
# else:
#     print("skipping images")
generate_images = False
os.chdir("exercises")
b = Bank()
b.generate_exercises(images=generate_images)
b.write_json()
b.build_viewer()
os.chdir("..")
shutil.copytree("exercises/docs", "output/stage/2024/exercises", dirs_exist_ok=True)
