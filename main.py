import requests
from logger import logging
import os


links = [
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV6PT5/SV6PT5_EN_{0}.png",  # shrouded fable
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SVP/SVP_EN_{0}.png",  # surging sparks
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV01/SV01_EN_{0}.png",  # scarlet and violet
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV04/SV04_EN_{0}.png",  # paradox rift
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV06/SV06_EN_{0}.png",  # twilight masquerade
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV02/SV02_EN_{0}.png",  # paldea evolved
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV03/SV03_EN_{0}.png",  # obsidian flames
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV07/SV07_EN_{0}.png",  # stellar crown
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV05/SV05_EN_{0}.png",  # temporal force
    # "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV3PT5/SV3PT5_EN_{0}.png",  # 151
    "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SV4PT5/SV4PT5_EN_{0}.png",  # paldean fates
    "https://assets.pokemon.com/static-assets/content-assets/cms2/img/cards/web/SVP/SVP_EN_{0}.png",  # scarlet and violet promo cards
]

output_location = "/media/jonard/Data/Pokemon_cards/"


def main():
    for base_url in links:
        logging.info(f"Start {base_url}")
        retry = 0
        for url in range(1, 600):
            image_link_list = base_url.format(url)
            base_path, file_name = os.path.split(image_link_list)
            base_path, folder_name = os.path.split(base_path)
            response = requests.get(image_link_list)
            if response.status_code == 200:
                base_output_folder = os.path.join(output_location, folder_name)
                output_file = os.path.join(output_location, folder_name, file_name)
                if not os.path.exists(base_output_folder):
                    os.makedirs(base_output_folder)
                if not os.path.exists(output_file):
                    with open(output_file, "wb") as file:
                        file.write(response.content)
                        logging.info(f"Saved successfully {output_file}")
                else:
                    logging.info(f"File already exists {folder_name} {file_name}")
            else:
                logging.warning(f"Failed: {response.status_code} retry {retry}")
                retry += 1
                if retry > 3:
                    logging.warning(f"Failed: {response.status_code} break")
                    break


if __name__ == "__main__":
    main()
