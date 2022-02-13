import turtle

# from mainG import racket11,racket22

class Base_PingPong_Elements:
    def __init__(self, title, element_width, element_height, auto_update=0,background="black"):
        self.__title=title
        self.__background=background
        self.__element_width=element_width
        self.__element_length=element_height
        self.__autoupdate=auto_update

        self=turtle.Screen()
        self.title(title)
        self.bgcolor(background)
        self.setup(width=element_width, height=element_height)
        self.tracer(auto_update)

class PingPong_Elements(Base_PingPong_Elements):
    def __init__(self, name, element_width, element_length, render_speed=0,
                element_shape="square", element_color="orange", init_position=(0,0),element_steps=20,
                score=0):
        
        self.__name=name
        self.__element_width=element_width
        self.__length=element_length
        self.__render_speed=render_speed
        self.__element_shape=element_shape
        self.__element_color=element_color
        self.__init_position=init_position
        self.__element_steps=element_steps
        self.__score=score

        self=turtle.Turtle()
        self.speed(render_speed)
        self.shape(element_shape) #set the shape of the object
        self.color(element_color) #set the color of the object
        self.shapesize(stretch_wid=element_width,stretch_len=element_length) #stretch the shape size (default: wid=20pi*1 , len=20pi*1)
        self.penup() #stop object of drawing lines
        self.goto(init_position) #set the position of the object
    
    def get_score(self):
        return self.__score

    def set_score(self):
        self.__score+=1

    

class PingPong_Ball(PingPong_Elements):
    def __init__(self, name, element_width, element_length, render_speed=0,
                element_shape="square", element_color="orange", init_position=(0, 0), element_steps=20,
                divx=0.1,divy=0.1):

        super().__init__(name, element_width, element_length, render_speed, element_shape, element_color, init_position, element_steps)
        
        self.__divx=divx
        self.__divy=divy


class Score_Calc:
    def __init__(self, position, font_color, render_speed):
        self.__position=position
        self.__font_color=font_color
        self.__render_speed=render_speed

        self=turtle.Turtle()
        self.penup()
        self.hideturtle()

        self.goto(position)
        self.color(font_color)
        self.speed(render_speed)

        # self.write(f"player1 : {racket11.get_score} -- {racket22.get_score} : player2" ,align="center", font=("Courier",24,"bold"))

    # def present_score(self):
    #     self.write()