##Task1

import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

fahrenheit_array = np.array([32, 68, 100, 212, 77])
celsius_array = vectorized_conversion(fahrenheit_array)

print("Fahrenheit:", fahrenheit_array)
print("Celsius:", celsius_array)


##Task2

import numpy as np

def custom_power(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(custom_power)

base_array = np.array([2, 3, 4, 5])
exponent_array = np.array([1, 2, 3, 4])

result_array = vectorized_power(base_array, exponent_array)

print("Base:", base_array)
print("Exponent:", exponent_array)
print("Result:", result_array)


##Task3

import numpy as np

base = np.array([2, 3, 4, 5])
power = np.array([1, 2, 3, 4])

def custom_pow(x, y):
    return x ** y

vectorized_pow = np.vectorize(custom_pow)

result = vectorized_pow(base, power)
print(result)


##Task4

import numpy as np

A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

B = np.array([12, -5, 15])

currents = np.linalg.solve(A, B)
print(f"I1 = {currents[0]:.2f}, I2 = {currents[1]:.2f}, I3 = {currents[2]:.2f}")


##Task5

from PIL import Image
import numpy as np

def load_image(path):
    """Load an image and convert to NumPy array."""
    image = Image.open(path).convert("RGB")  
    return np.array(image)

def save_image(np_img, path):
    """Convert NumPy array back to image and save."""
    img = Image.fromarray(np.uint8(np_img))
    img.save(path)

def flip_image(np_img, mode='horizontal'):
    """
    Flip the image.
    mode: 'horizontal' or 'vertical'
    """
    if mode == 'horizontal':
        return np.flip(np_img, axis=1)
    elif mode == 'vertical':
        return np.flip(np_img, axis=0)
    else:
        raise ValueError("Mode must be 'horizontal' or 'vertical'.")

def add_noise(np_img, noise_level=50):
    """
    Add random noise to the image.
    noise_level: Maximum noise value to add (0 to noise_level)
    """
    noise = np.random.randint(0, noise_level, np_img.shape, dtype='uint8')
    noisy_img = np_img + noise
    return np.clip(noisy_img, 0, 255)

def brighten_channels(np_img, increase=40):
    """
    Brighten all channels by 'increase' value.
    increase: Brightness increment for each channel
    """
    bright_img = np_img + increase
    return np.clip(bright_img, 0, 255)

def apply_mask(np_img, mask_size=(100, 100)):
    """
    Apply a black mask at the center of the image.
    mask_size: Tuple specifying (height, width) of the mask
    """
    h, w, _ = np_img.shape
    mask_h, mask_w = mask_size
    start_y = (h - mask_h) // 2
    start_x = (w - mask_w) // 2
    np_img[start_y:start_y+mask_h, start_x:start_x+mask_w] = 0  
    return np_img

if __name__ == "__main__":
   
    image_path = "images/birds.jpg"
    image = load_image(image_path)

    flipped_h = flip_image(image, mode='horizontal')
    save_image(flipped_h, "images/birds_flipped_horizontal.jpg")

    flipped_v = flip_image(image, mode='vertical')
    save_image(flipped_v, "images/birds_flipped_vertical.jpg")

    noisy_image = add_noise(image, noise_level=50)
    save_image(noisy_image, "images/birds_noisy.jpg")

    bright_image = brighten_channels(image, increase=40)
    save_image(bright_image, "images/birds_brightened.jpg")

    masked_image = apply_mask(image.copy(), mask_size=(100, 100))
    save_image(masked_image, "images/birds_masked.jpg")

    print("Image processing completed successfully.")
