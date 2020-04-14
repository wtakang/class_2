#!/home/tanyi/development/pythonclass/class_2/projects/calculator/bin/python3

import sys

import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

class Mainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('scientific calculator') # set the title of the application
        self.setFixedSize(500, 300) #give the mainwindow a fix size
        self.setLayout(qtw.QVBoxLayout()) #make a verticla box layout
        self.buttons() # create all the buttons needed for the calculator
        
        self.numbers= [] #this is used to store the users input
        self.func_nums = [] # used to store the mathematical operation to be performed
        
        
        self.show()
    
    def buttons(self):
            container = qtw.QWidget()
            container.setLayout(qtw.QGridLayout())
    
            #result field
            self.result_field =  qtw.QLineEdit()

            
            #buttons
            btn9 = qtw.QPushButton('9',clicked=lambda:self.num_press('9'))
            btn8 = qtw.QPushButton('8',clicked=lambda:self.num_press('8'))
            btn7 = qtw.QPushButton('7',clicked=lambda:self.num_press('7'))
            btn6 = qtw.QPushButton('6',clicked=lambda:self.num_press('6'))
            btn5 = qtw.QPushButton('5',clicked=lambda:self.num_press('5'))
            btn4 = qtw.QPushButton('4',clicked=lambda:self.num_press('4'))
            btn3 = qtw.QPushButton('3',clicked=lambda:self.num_press('3'))
            btn2 = qtw.QPushButton('2',clicked=lambda:self.num_press('2'))
            btn1 = qtw.QPushButton('1',clicked=lambda:self.num_press('1'))
            btn0 = qtw.QPushButton('0',clicked=lambda:self.num_press('0'))
            btnpoint = qtw.QPushButton('.',clicked=lambda:self.num_press('.'))
            
            # function buttons
            addbtn = qtw.QPushButton('+',clicked=lambda:self.func_press('+'))
            minusbtn = qtw.QPushButton('-',clicked=lambda:self.func_press('-'))
            multiplybtn = qtw.QPushButton('*',clicked=lambda:self.func_press('*'))
            dividebtn = qtw.QPushButton('/',clicked=lambda:self.func_press('/'))
            
            sinbtn = qtw.QPushButton('sin',clicked=self.operation1)
            cosbtn = qtw.QPushButton('cos')#,clicked=lambda:self.operation('cos'))
            tanbtn = qtw.QPushButton('tan')#,clicked=lambda:self.operation('tan'))
            percentbtn = qtw.QPushButton('%')#,clicked=lambda:self.operation('%'))
            
            # result button
            equalbtn = qtw.QPushButton('=',clicked= self.func_result)
            # clear button
            clearbtn = qtw.QPushButton('clear', clicked= self.clear_calc)
            
            
            #add buttons to the layout
            container.layout().addWidget(self.result_field, 0,0,1,4)
            
            container.layout().addWidget(btn9, 1,0)
            container.layout().addWidget(btn8, 1,1)
            container.layout().addWidget(btn7, 1,2)
            container.layout().addWidget(dividebtn, 1,3)
            
            container.layout().addWidget(btn6, 2,0)
            container.layout().addWidget(btn5, 2,1)
            container.layout().addWidget(btn4, 2,2)
            container.layout().addWidget(multiplybtn, 2,3)
            
            container.layout().addWidget(btn3, 3,0)
            container.layout().addWidget(btn2, 3,1)
            container.layout().addWidget(btn1, 3,2)
            container.layout().addWidget(minusbtn, 3,3)
            
            container.layout().addWidget(btn0, 4,0)
            container.layout().addWidget(btnpoint, 4,1)
            container.layout().addWidget(clearbtn, 4,2)
            container.layout().addWidget(addbtn, 4,3)
            
            container.layout().addWidget(sinbtn, 5,0)
            container.layout().addWidget(cosbtn, 5,1)
            container.layout().addWidget(tanbtn, 5,2)
            container.layout().addWidget(equalbtn, 5,3)
            
            self.layout().addWidget(container)
            
            #self.numbers= [] #this is used to store the users input
            #self.func_nums = [] # used to store the mathematical operation to be performed
    
    def num_press(self, key_number):
        self.numbers.append(key_number)
        temp_string = ''.join(self.numbers)
        if self.func_nums:
            self.result_field.setText(''.join(self.func_nums) + temp_string)
        else: 
            self.result_field.setText(temp_string)
        
    def func_press(self, operator):
        
        temp_string =''.join(self.numbers) 
        self.func_nums.append(temp_string) 
        self.func_nums.append(operator)
        self.numbers = []
        self.result_field.setText(''.join(self.func_nums))
                                  
    def func_result(self):
        fin_string = ''.join(self.func_nums)+''.join(self.numbers)
        result_string = eval(fin_string)
        
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)
        return result_string

    def clear_calc(self):
        self.result_field.clear()
        self.numbers = []
        self.func_nums = []
    
    def operation1(self):
        import math
        self.numbers = []
        value = self.func_result()
        value = ''.join(value)
        value = eval(value)
        result = math.sin(value)
        self.result_field.setText(result)
           
   
app = qtw.QApplication([])
mw =  Mainwindow() 
app.setStyle(qtw.QStyleFactory.create('Fusion'))
sys.exit(app.exec_())
