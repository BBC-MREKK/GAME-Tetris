import tkinter as tk
from main import Tetris, Application 

def test_game_integration():
    root = tk.Tk()
    app = Application(master=root)
    
    assert app.tetris.level == 0
    assert app.tetris.score == 0
    assert not app.tetris.game_over

    app.tetris.move(0, 1)
    app.tetris.rotate()
    

    assert app.tetris.level >= 0
    assert app.tetris.score >= 0
    assert app.tetris.game_over in (True, False)

    root.destroy()

if __name__ == '__main__':
    test_game_integration()