# This function will help us to find out the threshold image
def apply_threshold(image, threshold):
    thresholded_image = []
    for row in image:
        thresholded_row = []
        for pixel in row:
            if pixel > threshold:
                thresholded_row.append(255)
            else:
                thresholded_row.append(0)
        thresholded_image.append(thresholded_row)

    return thresholded_image

# Example usage:
example_image = [
    [50, 200, 150],
    [30, 255, 180],
    [100, 90, 240]
]

threshold_value = 100
thresholded_image = apply_threshold(example_image, threshold_value)
for row in thresholded_image:
    print(row)