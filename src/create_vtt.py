import datetime
import time

def main():
	vtt_file = open("../video/liveAlone/livealone.vtt", "w")

	vtt_file.write("WEBVTT\n\n")

	start_time = datetime.datetime(100,1,1,0,0,0,0)
	end_time = datetime.datetime(100,1,1,1,24,54,0)
	index_time = start_time
	count = 0
	y_index = 0

	while True:
		if index_time >= end_time:
			break
		if count == 0:
			next_time = index_time+datetime.timedelta(seconds=45)
			vtt_file.write(str(index_time.time())+".000 --> "+str(next_time.time())+".000\n")
			vtt_file.write("thumb_sprite.png#xywh=0,"+str(y_index)+",100,56\n\n")
			count = 1
		elif count == 1:
			next_time = index_time+datetime.timedelta(seconds=45)
			vtt_file.write(str(index_time.time())+".000 --> "+str(next_time.time())+".000\n")
			vtt_file.write("thumb_sprite.png#xywh=100,"+str(y_index)+",100,56\n\n")
			count = 2
		elif count == 2:
			y_index += 56
			count = 0

		index_time = next_time

	vtt_file.close()

if __name__ == '__main__':
	main()