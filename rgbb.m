pkg load image

% Read the image
image = imread('/home/navya/Pictures/IMG_20240220_175640.jpg');

% Convert image to RGB format
image_rgb = image(:,:,[3,2,1]);

% Get image dimensions
[height, width, ~] = size(image_rgb);

% Flatten the image to get RGB values for each pixel
rgb_values = reshape(image_rgb, height * width, []);

% Write RGB values to a CSV file
csvwrite('rgb_values.csv', rgb_values);
disp('success')

