from PIL import Image, ImageOps

# Load image
img = Image.open("danie-franco-A6O7pgc7vHg-unsplash_121031.jpg")

# Current dimensions
w, h = img.size
print(f"Original size: {w}x{h}")

# IMPORTANT: Calculate the actual padding needed based on common laptop resolutions
# Most laptops are 1920x1080 (16:9) or 1366x768 (16:9)

# For a portrait image to fill a 16:9 landscape screen:
# The width will stretch to fill, so we need to calculate what height is needed
# to ensure the stretched portion covers 16:9 while keeping content safe

# Method: Add enough padding so that when cropped to 16:9, your content survives
# Typically need 2-3x the height for portrait images

padding_multiplier = 3.0  # Start with 2.5x height (150% extra padding)
# Try increasing to 3.0 or 3.5 if 2.5 isn't enough

final_height = int(h * padding_multiplier)
final_width = w

print(f"New size with padding: {final_width}x{final_height}")
print(f"Total padding added: {final_height - h}px")
print(f"Padding per side: {(final_height - h)//2}px (top and bottom)")

# Create padded image with original centered vertically
# Using black padding - change color as needed
padded = ImageOps.pad(
    img,
    (final_width, final_height),
    color=(0, 0, 0),  # Black padding
    centering=(0.5, 0.5)  # Center the original image
)

# Save as PNG for lossless quality (no quality degradation)
output_path = "1.png"
padded.save(output_path, optimize=False)
print(f"Saved to: {output_path}")

print("\nTry these multipliers if 2.5 doesn't work:")
print("- 2.5 = 150% extra height")
print("- 3.0 = 200% extra height")
print("- 3.5 = 250% extra height")
print("- 4.0 = 300% extra height")