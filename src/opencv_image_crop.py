import cv2
import glob

def crop_image(filePath):
	image = cv2.imread(filePath)
	y = 173
	x=336
	h=495
	w=880
	crop = image[y:y+h, x:x+w]
	cv2.imshow('Image', crop)

	fileName = filePath.split("/")[-1:][0]
	cv2.imwrite('./screenshot/cropped_return_of_superman/'+fileName, crop)


def main():
	screenshot_filePath_list = glob.glob("./screenshot/return_of_superman/*.png")

	for filePath in screenshot_filePath_list:
		crop_image(filePath)

if __name__ == '__main__':
	main()