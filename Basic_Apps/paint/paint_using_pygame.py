#ti=his is a version of paint which uses pixels to perform paint tasks, very less features and minimilistic. commented fill func some problem is arising.

#importing stuff
import pygame
pygame.init()
pygame.font.init()

#Required Variables
fps=60
Width,Height=600,700
Rows=Cols=50
pixel_Size=Width//Cols
toolbar_size=Height-Width
exitwindow=False
screen=pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pixels")
clock=pygame.time.Clock()
grid=[]
drawingcolor='#000000'
font=pygame.font.SysFont(None,22)
want_grid=False

class Button:
    def __init__(self,x,y,width,height,color,text=None,text_color='#000000') -> None:
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.color=color
        self.text_color = text_color
    
    def draw(self):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.width,self.height])
        pygame.draw.rect(screen,'#000000',[self.x,self.y,self.width,self.height],2)
        if self.text:
            text=font.render(self.text,True,self.text_color)
            screen.blit(text,[self.x+self.width/2-text.get_width()/2,self.y+self.height/2-text.get_width()/2])
    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True

def Draw(pos):
    global drawingcolor,grid,want_grid
    x,y=pos
    row=y//pixel_Size
    col=x//pixel_Size
    if row<Rows and col<Cols:
        grid[row][col]=drawingcolor
    else:
        for button in buttons:
            if not button.clicked(pos):
                continue

            drawingcolor = button.color
            if button.text=="Clear":
                grid=[]
                makegrid()
                drawingcolor='#000000' 
            elif button.text=="Lines":
                want_grid=not want_grid
            # elif button.text=="Fill":
            #     fill(grid)

def grid_lines():
    for i in range(Rows+1):
        pygame.draw.line(screen,'#000000',(0,i*pixel_Size),(Width,i*pixel_Size))
    for i in range(Cols+1):
        pygame.draw.line(screen,'#000000',(i*pixel_Size,0),(i*pixel_Size,Height-toolbar_size))

def win_grid():
    y=-pixel_Size
    for i in range(0,Rows):
        x=-pixel_Size
        # grid.append([])
        for j in range (0,Cols):
            pygame.draw.rect(screen,grid[i][j],[x+pixel_Size,y+pixel_Size,pixel_Size,pixel_Size])
            x+=pixel_Size
            # grid[i].append('#FFFFFF')
        y+=pixel_Size

    if want_grid:
            grid_lines()

    for button in buttons:
        button.draw()

    pygame.display.update()


def makegrid():
     for i in range(0,Rows):
        grid.append([])
        for j in range (0,Cols):
            grid[i].append('#FFFFFF')

# def fill(grid):
#     global drawingcolor,Cols,Rows
#     row,col=100,100
#     while(row>Rows or col>Cols):
#         if pygame.mouse.get_pressed()[0]:
#             pos=pygame.mouse.get_pos()
#             # print(pos)
#             x,y=pos
#             row=y//pixel_Size
#             col=x//pixel_Size
#     print(row,col)
#     dir=[[0,1],[0,-1],[1,0],[-1,0]]
#     q=[]
#     q.append([row,col])
#     while(len(q)):
#         dx,dy=q[0][0],q[0][1]
#         q.pop(0)
#         # print(dx," ",dy)
#         grid[dx][dy]=drawingcolor
#         for i in dir:
#             tx=dx+i[0]
#             ty=dy+i[1]
#             if tx>=0 and ty>=0 and tx<Cols and ty<Rows and grid[tx][ty]=='#FFFFFF':
#                 q.append([tx,ty])




button_y = Height - toolbar_size/2 - 25
buttons = [
    Button(10, button_y, 50, 50, '#000000'),
    Button(70, button_y, 50, 50, '#FF0000'),
    Button(130, button_y, 50, 50, '#00FF00'),
    Button(190, button_y, 50, 50, '#0000FF'),
    Button(250, button_y, 50, 50, '#FFFFFF', "Erase", '#000000'),
    Button(310, button_y, 50, 50, '#FFFFFF', "Clear", '#000000'),
    Button(370, button_y, 50, 50, '#FFFFFF', "Lines", '#000000')
    # Button(430, button_y, 50, 50, '#FFFFFF', "Fill", '#000000')
]

#game loop
while not exitwindow:
    screen.fill('#48494B')
    makegrid()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitwindow=True
        else:   
            if pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                Draw(pos)
        win_grid()
        pygame.display.update()
        clock.tick(fps)
pygame.quit()
quit()
