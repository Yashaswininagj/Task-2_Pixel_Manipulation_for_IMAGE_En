from PIL import Image

def encrypt_image(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Get image size
    width, height = image.size
    
    # Encrypt the image by swapping pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            # Example encryption: swapping red and blue channels
            image.putpixel((x, y), (b, g, r))
    
    # Save the encrypted image
    encrypted_path = image_path.split('.')[0] + "_encrypted.png"
    image.save(encrypted_path)
    
    print("Image encrypted successfully!")
    print("Encrypted image saved as:", encrypted_path)

def decrypt_image(encrypted_image_path):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    
    # Get image size
    width, height = encrypted_image.size
    
    # Decrypt the image by swapping pixel values back
    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_image.getpixel((x, y))
            # Example decryption: swapping red and blue channels back to original
            encrypted_image.putpixel((x, y), (b, g, r))
    
    # Save the decrypted image
    decrypted_path = encrypted_image_path.split('_encrypted')[0] + "_decrypted.png"
    encrypted_image.save(decrypted_path)
    
    print("Image decrypted successfully!")
    print("Decrypted image saved as:", decrypted_path)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
        if choice == 'e':
            image_path = input("Enter the path of the image to encrypt: ")
            encrypt_image(image_path)
        elif choice == 'd':
            encrypted_image_path = input("Enter the path of the encrypted image to decrypt: ")
            decrypt_image(encrypted_image_path)
        else:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

        another = input("Do you want to perform another operation? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()

# Please install pillow
# ----pip install pillow
