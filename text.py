class Text:

    #initialization function
    def init(self, screen, x, y, text, font, color):
        self.screen = screen 
        self.ojx = float(x)
        self.ojy = float(y)
        self.font = font
        self.text = text
        self.color = color
        self.x = self.ojx
        self.y = self.ojy

    #updates the text and draws it
    def update(self):
        self.screen.blit(self.font.render(str(self.text),True, self.color), (self.x,self.y))

    #centers the text around the x and y point
    def center(self):
        self.x = self.ojx - self.font.size(str(self.text))[0]/2
        self.y = self.ojy - self.font.size(str(self.text))[1]/2