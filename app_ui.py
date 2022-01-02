# from PyQt5.QtCore    import Qt
# from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QWidget,
#                             QPushButton, QGridLayout, QSpacerItem,
#                             QSizePolicy, QLabel, QApplication)
# from PySide6.QtCore import *
# from PySide6.QtGui import *
# from PySide6.QtWidgets import *
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QFile, Qt, QPoint, QUrl, QSize, QTimer, QEvent
# from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton

# from PyQt5.QtGui import QPixmap

# from edit.css import Dialog

# from py_slider import 

# ////////////////\\\\\\\\\\\\\\\\
# os and system libraries
import sys,os
# os.chdir(sys._MEIPASS) #for installer or exe file
# from typing_extensions import runtime
# PyQt5 Libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtGui , QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
# image liberary
import PIL
from PIL import Image
import glob

# Dark theme
import qdarkstyle
# img2pdf
import img2pdf
# \\\\\\\\\\\\\\\\\////////////////


# ======================================================
# Error1 Undu style sheeet dark mode
# Error2 Show Slider on drop event
# 100% slider value get an error
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Global Variables
listVar=[]
Width_list=[]
value1=10




# -----------------------Droper class or list box class---------------------------------------------------------------

class ListBoxWidget(QListWidget,QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(690, 190)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            droppath = event.mimeData().text()
            f = os.path.splitext(droppath)
            if f[1]== '.jpg' or f[1]== '.jpeg' or f[1]== '.JPG' or f[1]== '.JPEG' or f[1] == '.png' or f[1]=='.PNG':
                #mouse release event function 
                event.accept()
            else:
                QMessageBox.information(self,"Invalid file " , "Not a valid picture file! ",QMessageBox.Yes)
        else:
            event.ignore()


    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()


    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            # win=Window()

            self.links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    self.links.append(str(url.toLocalFile()))
                    listVar.append(str(url.toLocalFile()))
                else:
                    self.links.append(str(url.toString()))
                    listVar.links.append(str(url.toString()))
     
            self.addItems(self.links)
            # Window.is_Visible(win)
        else:
            event.ignore()
            


# -----------------------------------------------------------------------------------------------
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Compression Python project")
        self.setWindowIcon(QtGui.QIcon("ico3.ico"))
        
        self.setGeometry(600,300,800,400)
        self.setFixedSize(800,400)
        self.setObjectName("Main_Window")
        self.setAttribute(Qt.WA_TranslucentBackground, True)

#------------------------------- Style Sheet connect -------------------------------
        stylesheet=""
        with open("qss.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)


#-------------------------------Removing Title Bar And Frame-------------------------------

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint) # | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        # vbox = QVBoxLayout()
        # sizegrip = QSizeGrip(self)
        # vbox.addWidget(sizegrip)
        # self.setLayout(vbox)

        self.UIx()


    def UIx(self):
        self.text = QLabel("IMG Commpresstion Box",self)
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        # mouse press and mouse move event for backgroud widget or screen
        self.widget.mousePressEvent= self.mousePressE
        self.widget.mouseMoveEvent = self.mouseMoveE
        
        
        # layout = QVBoxLayout(self)
        # layout.addWidget(self.widget)
        # layout = QGridLayout(self.widget)
#         layout.addItem(QSpacerItem(
# 400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 0)
        # self.hbox =QHBoxLayout()
        
#-------------------------------Choose_File-------------------------------


# ----------------------IMG
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(1)
        self.frame.move(80,50)
        self.frame_heading = QLabel(self.frame)
        self.frame_heading.setObjectName("Frame_Heading")
        self.frame_heading.setText("Choose File")
        self.frame_heading.move(70,5)
        self.frame.setObjectName("Choose_File")
        self.frame.mousePressEvent = self.get_Content
        
# ----------------------Folder

        self.frame2 = QFrame(self)
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setLineWidth(2)
        self.frame2.move(80,75)
        self.frame2_heading = QLabel(self.frame2)
        self.frame2_heading.setObjectName("Frame_Heading")
        self.frame2_heading.setText("Choose Folder")
        self.frame2_heading.move(65,8)
        self.frame2.setObjectName("Choose_File2")
        self.frame2.mousePressEvent = self.Get_Folder

#-------------------------------Clear_File-------------------------------

        self.clrframe = QFrame(self)
        self.clrframe.setFrameShape(QFrame.StyledPanel)
        self.clrframe.setLineWidth(2)
        self.clrframe.move(480,50)
        self.clrframe.setObjectName("Clear_file")
        self.clrframe_heading = QLabel(self.clrframe)
        self.clrframe_heading.setObjectName("Clr_Heading")
        self.clrframe_heading.setText("Clear Queue")
        self.clrframe_heading.move(65,15)
        self.clrframe.mousePressEvent = self.Clr_B

        #------------------------------- Closing button -------------------------------

        self.close_button = QLabel('x',self)
        self.close_button.move(750,14)
        self.close_button.setObjectName("closeButton")
        self.close_button.resize(20,20)
        self.close_button.setStyleSheet(" border-radius: 10px;")
        self.close_button.mousePressEvent = self.Close_B

    #work on button
        #------------------------------- Minimize button -------------------------------

        self.Miniz = QLabel('-',self)
        self.Miniz.move(720,14)
        self.Miniz.setObjectName("Miniz")
        self.Miniz.resize(20,20)
        self.Miniz.setStyleSheet(" border-radius: 10px;")
        self.Miniz.mousePressEvent = self.Minimize




#-------------------------------Drop_File or DropBox-------------------------------

        self.Drop_box = ListBoxWidget(self)
        self.Drop_box.move(50,120)
        self.Drop_box.installEventFilter(self)
        self.Drop_heading = QLabel(self.Drop_box)
        self.Drop_heading.setObjectName("Drop_Heading")
        self.Drop_heading.setText("Drop Your File Here")
        self.Drop_heading.move(260,90)
        self.Drop_box.setObjectName("Drop_File")
        
        


# -----------------------------------slider---------------------------------------
        mySlider = QSlider(Qt.Horizontal, self)
        mySlider.setGeometry(60, 280, 680, 30)
        self.Hslider=mySlider
        mySlider.setObjectName('slider')
        mySlider.setMaximum(100)
        mySlider.setValue(10)
        mySlider.valueChanged[int].connect(self.changeValue)
        mySlider.setVisible(False)
        

#-------------------------------Save all or Convert-------------------------------
        self.save= QFrame(self)
        self.save.setFrameShape(QFrame.StyledPanel)
        self.save.setLineWidth(2)
        self.save.move(280,330)
        self.save.mousePressEvent = self.Save_Dir
        self.save_heading = QLabel(self.save)
        self.save_heading.setObjectName("Save_Heading")
        self.save_heading.setText("Convert")
        self.save_heading.move(90,15)
        self.save.setObjectName("save_file")
# download icon
        self.DownIcon = QLabel('▼',self.save)
        self.DownIcon.resize(30,30)
        self.DownIcon.move(15,10)
        self.DownIcon.setStyleSheet("font-size:15px;color:white;padding-left:0px;border:3px solid white; border-radius: 15px;")
# countIcon
        self.count = QLabel(self)
        self.count.resize(44,44)
        self.count.move(500,325)
        self.count.setStyleSheet("text-align: justify;background-color: #A5A5A5;font-size:11px;font-weight:800;color: white;padding-left:0px;border:3px solid white; border-radius: 22px;")
        self.count.setVisible(False)
#Dark mode
        # self.DarkMode = QLabel('O',self)
        # self.DarkMode.resize(30,30)
        # self.DarkMode.move(700,355)
        # self.DarkMode.setStyleSheet("text-align: justify;background-color:black;font-size:11px;font-weight:800;color: white;padding-left:0px;padding-down:10px;border:3px solid white;backgrond-color:red; border-radius: 10px;")


# --------------------------------Ing2PDF or imgtopdf ---------------------------------------------------------------
    


        self.pdf= QPushButton("IMG2PDF",self)
        self.pdf.move(700,350)
        self.pdf.resize(55,25)
        self.pdf.clicked.connect(self.Img2Pdf)

# --------------------------------Img converison ---------------------------------------------------------------
    


        self.img_C= QPushButton("PNG↔JPG",self)
        self.img_C.move(640,350)
        self.img_C.resize(60,25)
        self.img_C.clicked.connect(self.Img_Conversion)
# ----------------------------------End Main Window----------------------------------------
        
        self.show()
    


# ----------------------------------- Functions ------------------------------------------4

#-------------------- exit function
    def Close_B(self,event):
        self.close()
        print("\n\nExit -->::::\n\n")
    def Minimize(self,event):
        self.showMinimized() 
        print("\n\nMinimised -->::::\n\n")





        
# /-------------------choose file  or Grt file path

    def get_Content(self,file_path):
        global Width_list
        file_name, _ = QFileDialog.getOpenFileName(self,"Select File","C:\\Users\\sdhal\\Pictures\\","All Files (*);; .jpeg (*.jpeg);; .png (*.png)")
        self.file_N =file_name
        self.changeValue(10)
        if file_name:
            self.Drop_box.addItems([str(file_name)])
            listVar.append(str(file_name))

# -----------------------slider Setvalue
            if listVar:
                self.count.setText("10%")
                self.Drop_heading.setVisible(False)
                self.Hslider.setVisible(True)
                self.count.setVisible(True)
                if len(listVar)<=1: 
                    self.i=0
                else:
                    self.i=1
            else:
                self.count.setText(None)
                self.Drop_heading.setVisible(True)
                self.Hslider.setVisible(False)
                self.count.setVisible(False)
                self.i=None







# ===========================GEt Folder location or dir
    def Get_Folder(self,event):
        global Width_list
        folder = QFileDialog.getExistingDirectory(self,"Select Directory","C:\\Users\\sdhal\\Pictures\\")
        self.changeValue(10)
        if folder:
            # print(str(folder+ "/"))
            self.Fdir = str(folder) + "/"

# to get list of pics inside the selected folder
            files=os.listdir(folder)
            images = [file for file in files if file.endswith(('jpg', 'png' , 'jpeg'))]
            for image in images:
                First_pic = folder+"/" +image
                img = Image.open(First_pic)
                self.Drop_box.addItems([str(First_pic)])
                listVar.append(str(First_pic))

# -----------------------slider Setvalue
# ---------------------show slider
            if listVar: 
                self.count.setText("10%")
                self.Drop_heading.setVisible(False)
                self.Hslider.setVisible(True)
                self.count.setVisible(True)
                if len(listVar)>1: 
                    self.i=1
                else:
                    self.i=0

            else:
                self.count.setText(None)
                self.Drop_heading.setVisible(True)
                self.Hslider.setVisible(False)
                self.count.setVisible(False)
                self.i=None

# /////////////////////////////////////////////////////////////////////

# ------------------value change of slider 
    def changeValue(self, value):
        global value1
        value1=value
        self.count.setText(str(value1)+"%")

# ====================================Save all or convert
    def Save_Dir(self,event):
        if listVar:
            save_dir = QFileDialog.getExistingDirectory(self,"Save File","C:\\Users\\sdhal\\Pictures\\")      
            self.saveD=save_dir
            if save_dir:
                self.Store_width()
                # self.Store_width()
                self.show_info_messagebox()

# --------------Save_Files-------------------------------------------------------
    def splite_name(self,list_var):
        diractory = list_var.split(".")
        return str(diractory[-1])
    def splite_name2(self,list_var):
        diractory = list_var.split("/")
        return str(diractory[-1])



# ----------------Store_width------------------------------------------------------------

    def Store_width(self):
        global value1
        global Width_list
        i=0
        for m in listVar:
            Img = Image.open(m)
            Width_list.append(float(Img.size[0]))
        for Wid in Width_list:
            width= Wid*(1-(int(value1)*0.01))
            if self.i==0:
                new_pic, okPressed = QInputDialog.getText(self, "Get Image Name","Image Name : ", QLineEdit.Normal, "")
                if okPressed and new_pic != '':
                    new_pic =str(self.saveD)+ "/"+ new_pic+ "."+self.splite_name(listVar[i])
            else:
                new_pic =str(self.saveD) + "/_Compressed_"+self.splite_name2(listVar[i])

            self.Compression_code(listVar[i], new_pic,int(width))
            print("done : "+str(i+1))
            # print(self.splite_name2(listVar[i],i))
            i+=1

        Width_list.clear()
        i=0
        
# ----------------Show Message Box on Done--------------------------------------------------------------

    def show_info_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("Done!! ")
        
        # setting Message box window title
        msg.setWindowTitle("Compression Complete ")
        
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)
        
        # start the app
        retval = msg.exec_()


# --------------------------------clear Queue

    def Clr_B(self,event):
        global Width_list
        self.Hslider.setVisible(False)
        self.Drop_heading.setVisible(True)
        self.count.setVisible(False)
        self.Drop_box.clear()
        listVar.clear()
        Width_list.clear()


# -------------------Img to Pdf-------------------------------------------------


    def Img2Pdf(self):
        global listVar
        option=QFileDialog.Options()
        if listVar:
            file=QFileDialog.getSaveFileName(self,"Save PDF ","defualt.pdf","All Files (*)",options=option)
            self.save_pdf_file = file[0]
            if self.save_pdf_file:
                File_name= open(self.save_pdf_file,"wb")
                File_name.write(img2pdf.convert(listVar[:]))
                File_name.close()
                self.pdf_complete(self.save_pdf_file)

# ----------------Show Message Box for pdf on Done--------------------------------------------------------------

    def pdf_complete(self,File_name):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("IMG to PDF Complete !! ")
        
        # setting Message box window title
        msg.setWindowTitle("Done!! ")
        
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Open)
        # msg.buttonClicked.connect(msgButtonClick)
        # start the app
        retval = msg.exec_()
        if retval == QMessageBox.Open:
            print(File_name)
            import webbrowser
            path = File_name
            webbrowser.open_new(path)


# -------------------Image . conversion -------------------------------------------------
    def splite_name3(self,list_var):
        diractory = list_var.split(".")
        return str(diractory[-2])

    def Img_Conversion(self,event):
        file, _ = QFileDialog.getOpenFileName(self,"Select File","C:\\Users\\sdhal\\Pictures\\","All Files (*);; .jpeg (*.jpeg);; .png (*.png)")
        # files=self.splite_name(file)
        if file.endswith(('jpg','JPG', 'JPEG' , 'jpeg')):
            img=Image.open(file)
            img.convert('RGB')
            img.save( self.splite_name3(file)+'.png','png')
            print(self.splite_name3(file)+'.png')
        else:
            if file.endswith(('png','PNG')):
                img=Image.open(file).convert('RGB')
                print(self.splite_name3(file)+'.jpeg')
                img.save( self.splite_name3(file)+'.jpg', "jpeg")


            
            


    


#----------------- Move and press event for background frame to move frameless windows
# action 1
    def mousePressE(self,event):
        self.oldPosition = event.globalPos()
        

# action 2
    def mouseMoveE(self,event):
        delta = QPoint(event.globalPos()-self.oldPosition)
        self.move(self.x()+delta.x(),self.y()+delta.y())
        self.oldPosition = event.globalPos()

# action in dropbox right click for del


    def eventFilter(self, source, event):
       if event.type() == QEvent.ContextMenu and source is self.Drop_box:
        #    print(event)
        #    print(source)
           menu =QMenu()
           menu.addAction("Delete")
        #    clicked = 
           if listVar:
               if menu.exec_(event.globalPos()):
                   clicked = self.Drop_box.currentRow()
                   item = source.itemAt(event.pos())
                   self.Drop_box.takeItem(clicked)
                   listVar.pop(clicked)
                   return True
       return super().eventFilter(source,event)

    def contextMenuEvent(self, event):
        CMenu = QMenu(self)
        # DarkMode=CMenu.addAction("Change Mode")
        DarkMode=CMenu.addAction("Dark Mode")
        LightMode=CMenu.addAction("light Mode")
        A2=CMenu.addAction("Quit")
        action = CMenu.exec_(self.mapToGlobal(event.pos()))
        if action == A2:
            self.close()
            print("\n\nAPP closed--->>:::\n\n")
        if action == DarkMode:
            self.widget.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.Drop_box.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.close_button.setStyleSheet("color:white;border-radius: 10px;")
            self.Miniz.setStyleSheet("color:white;border-radius: 10px;")
            self.Drop_heading.resize(210,25)
            self.Drop_heading.move(255 ,90)
            

            print("DarkMode")

        if action == LightMode:
            self.widget.setStyleSheet("color white;")
            self.Drop_box.setStyleSheet("color:white;")
            self.close_button.setStyleSheet("color:black;border-radius: 10px;")
            self.Miniz.setStyleSheet("color:black;border-radius: 10px;")

            print("LightMode")
        #     


# comression COde-------------------------------------------------

    def Compression_code(self, old_pic, new_pic,width):
        img = Image.open(old_pic)
        wpercent = (width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((width,hsize), PIL.Image.ANTIALIAS)
        img.save(new_pic)
        
    @classmethod
    def is_Visible(self):
        global listVar
        if listVar:
            self.Hslider.setVisible(True)
            # self.count.setText("10%")
            # self.Drop_heading.setVisible(False)
            # self.count.setVisible(True)
            
        # else:
        #     self.Hslider.setVisible(False)
        #     self.Drop_heading.setVisible(True)
        #     self.count.setVisible(False)
        #     self.count.setText(None)
            
# -----------------------------------------------------------------------------------------------------------------
# ////////////////////////////////////////  Main Fxn  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# -------------------------------------------------------------------------------------------------------------------

def main():
    global window
    App = QApplication(sys.argv)
    window= Window()
    
# for disply it on system tray--------------------------------------
    trayIcon = QSystemTrayIcon(QIcon('ico3.ico',))
    trayIcon.setToolTip('Icon')
    trayIcon.show()
    menu = QMenu()
    exitAction =menu.addAction('Exit')
    exitAction.triggered.connect(App.quit)
    trayIcon.setContextMenu(menu)
# -------------------------------------------------------------------

    # demo =DialogApp()
    # Dark Mode
    # App.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    # demo.show()
    window.show()
    print("\n\nAPP Open--->>:::\n\n")

    sys.exit(App.exec_())
    print("\n\nAPP closed--->>:::\n\n")
    


# ----------------------------------Calling Main() fxn
if __name__ == '__main__':
    main()

else:
    print(__name__,"FFFF")