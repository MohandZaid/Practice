import turtle

class Base_PingPong_Elements:
    def __init__(self, title, element_width, element_height,
                left_player_up_key,left_player_down_key,
                right_player_up_key,right_player_down_key,
                close_key,start_play_key,
                auto_update=0,background="black"):

        self.__title=title

        self.__element_width=element_width
        self.__element_length=element_height
        self.__background=background
        self.__autoupdate=auto_update

        self.__left_player_up_key=left_player_up_key
        self.__left_player_down_key=left_player_down_key

        self.__right_player_up_key=right_player_up_key
        self.__right_player_down_key=right_player_down_key

        self.__close_key=close_key
        self.__start_play_key=start_play_key

        self=turtle.Screen()
        self.title(title)
        self.bgcolor(background)
        self.setup(width=element_width, height=element_height)
        self.tracer(auto_update)
        self.listen()


    def close(self): #function to close loop
        self=turtle.bye() #set status to false to exit the loop

    def wind_update(self):
        self=turtle.update()

class PingPong_Elements(Base_PingPong_Elements):
    def __init__(self, name, element_width, element_length,
                render_speed=0,element_shape="square", element_color="orange",
                init_position=(0,0),element_steps=20, score=0):
        
        self.__name=name
        self.__element_width=element_width
        self.__element_length=element_length
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
    
    def get_ycore(self):
        return turtle.ycor
    def set_ycore(self,y):
        self=turtle.sety(y)

    def racket_up(self):
        y=self.get_ycore() #get the y coordinate of racket
        y+=20 #set the new y after click by adding step
        self.set_ycore(y) #set the new y coordinate position 

    def racket_down(self):
        y=self.get_ycore()
        y-=20
        self.set_ycore(y)

    def get_score(self):
        return self.__score

    def set_score(self):
        self.__score+=1

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_element_width(self):
        return self.__element_width

    def get_element_length(self):
        return self.__element_length


    def get_element_xcore(self):
            return turtle.xcor

    def get_element_ycore(self):
        return turtle.ycor




class PingPong_Ball(PingPong_Elements):
    def __init__(self, name, element_width, element_length, render_speed=0,
                element_shape="circle", element_color="red", init_position=(0, 0),
                xspeed=0.1,yspeed=0.1, slope=-1):

        super().__init__(name, element_width, element_length, render_speed, element_shape, element_color)
        
        self=turtle.Turtle()

        self.__xspeed=xspeed
        self.__yspeed=yspeed
        self.__slope=slope
        self.__init_position=init_position

        self.goto(self.__init_position)
        self.hideturtle()

    def get_xspeed(self):
        return self.__xspeed

    def get_yspeed(self):
        return self.__yspeed

    # def set_xspeed(self):
    #     self.__xspeed *=self.__slope

    # def set_yspeed(self):
    #     self.__yspeed *=self.__slope

    def get_xcore(self):
        return turtle.xcor

    def get_ycore(self):
        return turtle.ycor


class Score_Calc:
    def __init__(self, position, font_color,left_player_object, right_player_object, render_speed=0):
        self.__position=position
        self.__font_color=font_color
        self.__left_player_object=left_player_object
        self.__right_player_object=right_player_object
        self.__render_speed=render_speed

        self=turtle.Turtle()
        self.penup()
        self.hideturtle()

        self.goto(position)
        self.color(font_color)
        self.speed(render_speed)

        self.write(f"{PingPong_Elements.get_name(left_player_object)} : {PingPong_Elements.get_score(left_player_object)} -- {PingPong_Elements.get_score(right_player_object)} : {PingPong_Elements.get_name(right_player_object)}" ,align="center", font=("Courier",24,"bold"))

    def present_score(self, left_player_object, right_player_object):
        self=turtle.write(f"{PingPong_Elements.get_name(left_player_object)} : {PingPong_Elements.get_score(left_player_object)} -- {PingPong_Elements.get_score(right_player_object)} : {PingPong_Elements.get_name(right_player_object)}" ,align="center", font=("Courier",24,"bold"))
