from kivy.uix.screenmanager import ScreenManager

class NavigationScreenManager(ScreenManager) :
    
    scree_stack = []
    
    def push(self, screen_name) :
        if screen_name not in self.scree_stack :
            self.scree_stack.append(self.current)
            self.transition.direction = 'left'
            self.current = screen_name
        
    def pop(self) :
        if len(self.scree_stack) > 0 :
            screen_name = self.scree_stack[-1]
            del self.scree_stack[-1]
            self.transition.direction = 'right'
            self.current = screen_name
            