from checkit.bank import Bank
import os

generate_images = input("Generate images? y/n ").strip().upper() == "Y"
os.chdir("exercises")
b = Bank()
b.generate_exercises(images=generate_images)
b.write_json()
b.build_viewer()
os.chdir("..")
