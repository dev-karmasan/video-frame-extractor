import os
from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import subprocess

root = Tk()
root.title('Image extractor')
# root.geometry("500x450")

filenamespath_list = [] # List to store filenamespath
filenames_list = [] # List to store filenames

# functions for section 1: Loading files section
def loadFiles():
    clear() # clear the texts first if there is any

    root.filenames =  filedialog.askopenfilenames(initialdir = "C:/Users/Sandeep/Desktop/Geyser/Strokkur_Sony_130320", title = "Select file", filetypes = (("mp4","*.mp4"),("avi","*.avi"),("mov","*.mov"))) # Load the video files

    filenamespath_list = list(root.filenames) # List to store filepaths

    filenames_list = [] # List to store filenames
           
    # Extract filenames from filepaths
    filenames_list += [Path(i).stem for i in filenamespath_list]

    # Makes each line for the paths
    filenamespath_list = '\n'.join([i for i in filenamespath_list])
    
    # update file list label
    file_list = Label(loading_frame, text = filenamespath_list, font = ('Consolas', 16))
    file_list.grid(row = 0, column = 1)

    print(filenamespath_list)


def clear():
    file_list = Label(loading_frame, text = '', padx = 300, pady = 60, bd = 1)
    file_list.grid(row = 0, column = 1)
    # filenamespath_list = [] # List to store filepaths
    # filenames_list = [] # List to store filenames


# functions for section 2: Extraction options
images_options = ['png', 'jpg'] # options for output images
digit_options = ['1', '2', '3'] # options for digit for the filenames

fps = IntVar() # Integer variable for frames per seconds
fps.set(5) # Default integer variable for frames per seconds

image_output_selection = StringVar() # string variable for image output selection
image_output_selection.set(images_options[0]) # default selection for image output option

digit_number_selection = IntVar() # integer variable for digit number selection
digit_number_selection.set(digit_options[1]) # default selection for digit number


# functions for section 3: Start the extraction
def execution(fps, image_output_selection, digit_number_selection):
    # subprocess.run('mkdir')
    print(filenamespath_list)

def start():
    if image_output_selection.get() == 'jpg':
        image_output_response = messagebox.askyesno('Warning', 'You have chosen jpg as an output, the output images quality might be depreciated. Would you like to proceed?')
        if image_output_response == 1:
            final_response = messagebox.askyesno('Is this selection correct?',
                            'Number of frames = ' + str(fps.get()) + '\n'
                            'Output format = ' + image_output_selection.get() + '\n'
                            'Number of digits to suffix = ' + str(digit_number_selection.get()) + '\n')
            if final_response == 1:
                execution(fps, image_output_selection, digit_number_selection)
    else:
        final_response = messagebox.askyesno('Is this selection correct?',
                            'Number of frames = ' + str(fps.get()) + '\n'
                            'Output format = ' + image_output_selection.get() + '\n'
                            'Number of digits to suffix = ' + str(digit_number_selection.get()) + '\n')
        if final_response == 1:
            execution(fps, image_output_selection, digit_number_selection)




#-------------------------------------------------------------------------------
# Section 1: Loading files section
loading_frame = LabelFrame(root, text = 'load your files')
loading_frame.pack(padx = 5, pady = 5)

# label to show the selected videos
file_list = Label(loading_frame, text = '', padx = 300, pady = 60, bd = 1)
file_list.grid(row = 0, column = 1)

# button for loading videos
button_load = Button(loading_frame, text = 'Load', padx = 40, pady = 20, command = loadFiles)
button_load.grid(row = 1, column = 0, padx = 5, pady = 5)

# button for clearing the loaded files
button_clear = Button(loading_frame, text = 'Clear', padx = 40, pady = 20, command = clear)
button_clear.grid(row = 1, column = 2, padx = 5, pady = 5)

#-----------------------------------------------------------
# Section 2: Extraction options
options_frame = LabelFrame(root, text = 'select your options', padx = 200, pady = 20)
options_frame.pack(padx = 5, pady = 5)


# Number of frames per second
Label(options_frame, text = 'Frames per second', padx = 40, pady = 30, bd = 1).grid(row = 0, column = 0)
fps_number = Entry(options_frame, text = "Enter desired fps", textvariable = fps)
fps_number.grid(row = 1, column = 0)

# Select desired output format
Label(options_frame, text = 'Output Image', padx = 40, pady = 30, bd = 1).grid(row = 0, column = 1)
image_output = OptionMenu(options_frame, image_output_selection, *images_options)
image_output.grid(row = 1, column = 1)

# Numbers of digit after the exported frame name
Label(options_frame, text = 'Number of digits to suffix', padx = 40, pady = 30, bd = 1).grid(row = 0, column = 2)
digit_number = OptionMenu(options_frame, digit_number_selection, *digit_options)
digit_number.grid(row = 1, column = 2)




#-----------------------------------------------------------------------------------------
# Section 3: Start the extraction
execution_frame = LabelFrame(root, text = 'Start the extraction', padx = 300, pady = 20)
execution_frame.pack(padx = 5, pady = 5)

button_start = Button(execution_frame, text = 'Start', padx = 40, pady = 20, command = start)
button_start.grid(row = 0, column = 0)



root.mainloop()