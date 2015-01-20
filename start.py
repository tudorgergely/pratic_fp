from ui.administer_ui import *
from ui.play_ui import *

from repository.FileRepository import *
from domain.Word import *
from controller.WordController import *

def start():
	repo = FileRepository('scramble.txt')
	ctrl = WordController(repo)

	ad_ui = AdministerUi(ctrl)
	pl_ui = PlayUi(ctrl)

	while True:
		ad_ui.run_administer()
		pl_ui.run_play()

start()