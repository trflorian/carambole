import torch
import cv2

# DINOv2
dinov2_vits14: torch.nn.Module = torch.hub.load("facebookresearch/dinov2", "dinov2_vits14")  # type: ignore

img = cv2.imread("images/board.png")

# Convert the image to RGB format
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Resize the image to the required input size for DINOv2
img_resized = cv2.resize(img_rgb, (224, 224))

# Convert the image to a tensor and normalize it
img_tensor = torch.tensor(img_resized).permute(2, 0, 1).unsqueeze(0).float() / 255.0

# Move the tensor to the appropriate device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

img_tensor = img_tensor.to(device)
dinov2_vits14 = dinov2_vits14.to(device)

# Perform inference
with torch.no_grad():
    features = dinov2_vits14(img_tensor)

# Extract the features
features = features.cpu().numpy()

# Print the shape of the features
print("Features shape:", features.shape)
