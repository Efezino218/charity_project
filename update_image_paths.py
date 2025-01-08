import os
import re

# Path to your templates folder
template_dir = "holdingcore_app/templates/holdingcore_app"

# Function to update image paths
def update_image_paths(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")  # Debugging: Show file being processed
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Replace src="img/... or src='img/... with {% static 'holdingcore_app/img/... %}"
                updated_content = re.sub(
                    r'src=[\'"](?:\.?/)?img/(.*?)[\'"]',
                    r"src=\"{% static 'holdingcore_app/img/\1' %}\"",  # Correct the quotes handling
                    content
                )

                # Write back the updated content
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"Updated: {file_path}")

# Run the function
update_image_paths(template_dir)
