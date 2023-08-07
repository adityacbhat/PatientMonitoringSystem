total_num_actions=3
imagecount=0
look_around_X_data=[]
look_around_Y_data = []
value_for_y=0.
n_steps=32
data_path='./SyntheticDataV1'
label_track_dict={}
global mainx,mainy
mainx=[]
mainy=[]

 

for folders in os.listdir(data_path):
		for actions,sub_folders in enumerate(os.listdir(data_path+'/'+folders)):
			for real_actions in os.listdir(data_path+'/'+folders+'/'+sub_folders):
				frame_provider = VideoReader(data_path+'/'+folders+'/'+sub_folders+'/'+real_actions)
				run_demo(net, frame_provider, 256, cpu, 1, 1,actions-1)
		


def duplicate_creation(look_around_X_data,n_steps):
		mod_val=len(look_around_X_data) % n_steps
		duplicate_count=abs(int((((len(look_around_X_data)-mod_val)/ n_steps)+ 1)*n_steps-len(look_around_X_data)))
		tobeadded_X=look_around_X_data[len(look_around_X_data)-1]
		tobeadded_Y=look_around_Y_data[len(look_around_Y_data)-1]
		print("Adding last record Duplicates. Total number is: ",duplicate_count)
		for nums in range(0,duplicate_count):
			look_around_X_data.append(tobeadded_X)
			look_around_Y_data.append(tobeadded_Y)


	

def data_for_model(look_around_X_data,n_steps,look_around_Y_data):

	def most_frequent(List): 
		counter = 0
		num = List[0] 
		for i in List: 
			curr_frequency = List.count(i) 
			if(curr_frequency> counter): 
				counter = curr_frequency 
				num = i 
		return num 
	with open('Xdata.txt', 'w') as outfile:
		json.dump(look_around_X_data, outfile)

	X_ = np.array(look_around_X_data)
	blocks = int(len(X_) / n_steps)

	X_ = np.array(np.split(X_,blocks))
	
	Divided_Y=[]
	j=[]
  #  for elements in look_around_Y_data:
  #      if(elements[0]==0.0):
  #          j.append([1,0,0])
  #      elif(elements[0]==1.0):
  #          j.append([0,1,0])
  #      elif(elements[0]==2.0):
			#j.append([0,0,1])
		
	   
	for elements in look_around_Y_data:
		if(elements[0]==0.0):
			j.append([1,0])
		elif(elements[0]==1.0):
			j.append([0,1])
	 #   elif(elements[0]==2.0):
	#        j.append([0,0,1])
	 #   elif(elements[0]==3.0):
	 #      j.append([0,0,0,1,0])
	 #   elif(elements[0]==4.0):
	   #    j.append([0,0,0,0,1])
	for i in range(0,len(j),n_steps):
		Divided_Y.append(j[i:i+n_steps])
	final_y=[]
	for i in range(0,len(Divided_Y)):
		final_y.append(most_frequent(Divided_Y[i]))
	with open('Ydata.txt', 'w') as outfile:
		json.dump(j, outfile)
	y_= np.array(final_y)

	return X_,y_





if(len(look_around_X_data)%n_steps!=0):
	duplicate_creation(look_around_X_data,n_steps)




npX_,npy_=data_for_model(look_around_X_data,n_steps,look_around_Y_data)

print("Shapes: npx: ",npX_.shape," npy: ",npy_.shape,"\n\n\nnpy: ",npy_)
f = Figlet(font='slant')   
print (f.renderText("MODEL STARTS FROM HERE"))
print("\n\nYtest:  ",npy_,'\n\n')




X_train, X_test, y_train, y_test = train_test_split(npX_, npy_, test_size=0.4, random_state=5)

print("(X_train shape, y_train shape, X_test shape ,y_test shape)")
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)