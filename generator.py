from PIL import Image 
from IPython.display import display 
import random
import json

###########################
##### LAYERS MAPPING ######
###########################

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Blue", "Green", "Light_Blue", "Lime", "Orange", "Pink", "White"] 
background_weights = [10, 10, 10, 10, 10, 10, 40]

body = ["Green_Sloth_Skin"]
body_weights = [100]

hats = ["Air_Pods", "Bucked_Hat_Black", "Bucked_Hat_Blu", "Bucked_Hat_Green", "Bucked_Hat_Pink"]
hats_weights = [20, 20, 20, 20, 20]

mouth = ["3", "Angry", "Cigar", "Crazy_Mouth", "Farched", "Gotcha", "Happy", "Ics", "Joint", "Kiss", "Mmmmh", "Ooo", "Smile", "What"]
mouth_weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 20]

nose = ["Nose"]
nose_weights = [100]

occhi = ["Cute", "Fattanza", "Happy", "Hungry", "Love", "Ohh", "Wow"]
occhi_weights = [10, 10, 10, 10, 10, 10, 40]

shirt = ["Running", "White"]
shirt_weights = [50, 50]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

background_files = {
    "Blue": "blu",
    "Green": "green",
    "Light_Blue": "light_blu",
    "Lime": "lime",
    "Orange": "orange",
    "Pink": "pink",
    "White": "white"
}

body_files = { 
    "Green_Sloth_Skin": "Green_Sloth_Skin"
}

hats_files = {
    "Air_Pods": "air_pods", 
    "Bucked_Hat_Black": "bucked_hat_black", 
    "Bucked_Hat_Blu": "bucked_hat_blu", 
    "Bucked_Hat_Green": "bucked_hat_green", 
    "Bucked_Hat_Pink": "bucked_hat_pink"   
}

mouth_files = {
    "3": "3", 
    "Angry": "angry", 
    "Cigar": "cigar", 
    "Crazy_Mouth": "Crazy_mouth", 
    "Farched": "farche'd", 
    "Gotcha": "gotcha", 
    "Happy": "happy", 
    "Ics": "ics", 
    "Joint": "joint", 
    "Kiss": "kiss", 
    "Mmmmh": "mmmh", 
    "Ooo": "ooo", 
    "Smile": "smile", 
    "What": "what"
}

nose_files = {
    "Nose": "nose"
}

occhi_files = {
    "Cute": "cute", 
    "Fattanza": "fattanza", 
    "Happy": "happy_eyes", 
    "Hungry": "hungry", 
    "Love": "love", 
    "Ohh": "OHH", 
    "Wow": "wow"
}

shirt_files = {
    "Running": "Running_connection", 
    "White": "White_hoodie"
}

###########################
###########################
###########################



###########################
##### GENERATE TRAITS #####
###########################


if __name__ == "__main__":
    TOTAL_IMAGES = 100 # Number of random unique images we want to generate

    all_images = [] 

    # A recursive function to generate unique image combinations
    def create_new_image():
        
        new_image = {} #

        # For each trait category, select a random trait based on the weightings 
        new_image["Background"] = random.choices(background, background_weights)[0]
        new_image["Body"] = random.choices(body, body_weights)[0]
        new_image["Hats"] = random.choices(hats, hats_weights)[0]
        new_image["Mouth"] = random.choices(mouth, mouth_weights)[0]
        new_image["Nose"] = random.choices(nose, nose_weights)[0]
        new_image["Occhi"] = random.choices(occhi, occhi_weights)[0]
        new_image["Shirt"] = random.choices(shirt, shirt_weights)[0]
        
        if new_image in all_images:
            return create_new_image()
        else:
            return new_image
        
        
    # Generate the unique combinations based on trait weightings
    for i in range(TOTAL_IMAGES): 
        
        new_trait_image = create_new_image()
        
        all_images.append(new_trait_image)

    # Returns true if all images are unique
    def all_images_unique(all_images):
        seen = list()
        return not any(i in seen or seen.append(i) for i in all_images)

    # Add token Id to each image
    i = 0
    for item in all_images:
        item["tokenId"] = i
        i = i + 1
        
    #print(all_images)
    
    background_count = {}
    for item in background:
        background_count[item] = 0
        
    body_count = {}
    for item in body:
        body_count[item] = 0

    hats_count = {}
    for item in hats:
        hats_count[item] = 0
    
    mouth_count = {}
    for item in mouth:
        mouth_count[item] = 0
    
    nose_count = {}
    for item in nose:
        nose_count[item] = 0
    
    occhi_count = {}
    for item in occhi:
        occhi_count[item] = 0

    shirt_count = {}
    for item in shirt:
        shirt_count[item] = 0
        
    for image in all_images:
        background_count[image["Background"]] += 1
        body_count[image["Body"]] += 1
        hats_count[image["Hats"]] += 1
        mouth_count[image["Mouth"]] += 1
        nose_count[image["Nose"]] += 1
        occhi_count[image["Occhi"]] += 1
        shirt_count[image["Shirt"]] += 1
        
        
    print(background_count)
    print(body_count)
    print(hats_count)
    print(mouth_count)
    print(nose_count)
    print(occhi_count)
    print(shirt_count)
    
    #### Generate Metadata for all Traits 
    METADATA_FILE_NAME = './metadata/all-traits.json'; 
    with open(METADATA_FILE_NAME, 'w') as outfile:
        json.dump(all_images, outfile, indent=4)
        
        
    #### Generate Images    
    for item in all_images:

        im1 = Image.open(f'./trait-layers/backgrounds/{background_files[item["Background"]]}.png').convert('RGBA')
        im2 = Image.open(f'./trait-layers/Body/{body_files[item["Body"]]}.png').convert('RGBA')
        im3 = Image.open(f'./trait-layers/Hats/{hats_files[item["Hats"]]}.png').convert('RGBA')
        im4 = Image.open(f'./trait-layers/Mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
        im5 = Image.open(f'./trait-layers/Nose/{nose_files[item["Nose"]]}.png').convert('RGBA')
        im6 = Image.open(f'./trait-layers/Occhi/{occhi_files[item["Occhi"]]}.png').convert('RGBA')
        im7 = Image.open(f'./trait-layers/Shirt/{shirt_files[item["Shirt"]]}.png').convert('RGBA')

        #Create each composite
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(com1, im3)
        com3 = Image.alpha_composite(com2, im4)
        com4 = Image.alpha_composite(com3, im5)
        com5 = Image.alpha_composite(com4, im6)
        com6 = Image.alpha_composite(com5, im7)

        #Convert to RGB
        rgb_im = com6.convert('RGB')
        file_name = str(item["tokenId"]) + ".png"
        rgb_im.save("./images/" + file_name)