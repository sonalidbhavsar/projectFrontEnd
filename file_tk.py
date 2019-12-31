from Tkinter import *
import ttk
import Tkinter, Tkconstants, tkFileDialog
import pickle
import pandas as pd
def select_file():
	entry.configure(state='normal')
	entry.delete(0,END)
	root.filename = tkFileDialog.askopenfilename(initialdir ="/",title = "Select file",filetypes = (("excelfiles","*.xls"),("all files","*.*")))
	print (root.filename)
	entry.insert(0,root.filename)
	entry.configure(state='readonly')

class Processing:
	def __init__(self):
		y_list=[]

	def process(self,file):
		#model=pickle.load_file("F:\\Downloads\\finalized_model.sav")
		loaded_model = pickle.load(open("F:\\Downloads\\finalized_modelproto2.sav" , 'rb'))
		X=pd.read_excel(feature_file)
		y_list=model.predict(X)
		

	def download(self):
		print("wait")
		df = pd.DataFrame (y_list)
		filepath = 'prediction.xlsx'
		df.to_excel(filepath, index=False)

root = Tk()
root.geometry("800x1200")
Grid.rowconfigure(root, 0, weight=0)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
but=ttk.Button(root,text='Select features file',command=select_file)
#but.pack()
feature_file = StringVar()
entry=ttk.Entry(root,text=' ',textvariable=feature_file)
#entry.pack()
but.grid(row=0,column=0,padx=20,pady=200,sticky=N+S+E+W)
entry.grid(row=0,column=1,padx=20,pady=200,sticky=N+S+E+W)
p=Processing()
submit=ttk.Button(root,text='UPLOAD FEATURES FILE',width=50,command=lambda: p.process(feature_file))
submit.grid(row=2,column=0,sticky=N+S+E+W,pady=100,padx=100)
submit.place(relx=0.5, rely=0.5, anchor=CENTER)
download=ttk.Button(root,text='DOWNLOAD PREDICTION FILE',width=50,command=p.download)
download.grid(row=2,column=0,sticky=N+S+E+W,pady=100,padx=100)
download.place(relx=0.5, rely=0.6, anchor=CENTER)
'''photo = PhotoImage(file = "F:\\Iricenlogo.png")
root.iconphoto(False, photo)'''
root.mainloop()
