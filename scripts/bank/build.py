from checkit.bank import Bank
import os

# generate_images = input("Generate images? y/n ").strip().upper() == "Y"
# if generate_images:
#     print("regenerating images")
# else:
#     print("skipping images")
generated_images = False
os.chdir("exercises")
b = Bank()
b.generate_exercises(images=generate_images)
b.write_json()
b.build_viewer()
os.chdir("..")
