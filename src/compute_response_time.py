import cv2
import glob

def compute_response_time():
	filename_list = glob.glob("./screenshot/return_of_superman/*.png")
	filename_list.sort()

	img_histogram = list()


	for filename in filename_list:
		img1 = cv2.imread(filename)
		#img_color[filename[:-4]] = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

		hist= cv2.calcHist([img1], [0,1,2], None, [256,256,256], [0,256,0,256,0,256])
		#hist = cv2.normalize(hist, hist).flatten()
		img_histogram.append((filename, hist))	

	hist_diff_list = list()

	for i in range(0, len(img_histogram)-1):
		diff = cv2.compareHist(img_histogram[i][1],img_histogram[i+1][1],cv2.HISTCMP_CORREL)
		#print(img_histogram[i][0].split("/")[-1:][0])
		print("Diff of "+str(img_histogram[i][0].split("/")[-1:][0])+ " and "+str(img_histogram[i+1][0].split("/")[-1:][0])+" = "+str(diff))
		hist_diff_list.append(diff)

	#print(hist_diff_list)

def main():
	compute_response_time()

if __name__ == '__main__':
	main()