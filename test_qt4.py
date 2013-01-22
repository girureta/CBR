import sys
from PyQt4 import QtGui,QtCore

from playChess_qt4 import Ui_Dialog

import chess


class test(QtGui.QDialog):

	def __init__(self):

		QtGui.QMainWindow.__init__(self) 
		self.ventana = Ui_Dialog()
		self.ventana.setupUi(self)
		self.setCombos()
		
		self.connect(self.ventana.queryButton,QtCore.SIGNAL('clicked()'), self.query)
		
		print 'GUI loaded, loading CBR system'
		
		FLibFile = 'data/database'
		RLibFile = 'data/symetricDB'
		self.chessCBR = chess.CBRProcessor(FLibFile, RLibFile)
		
	def query(self):
		print 'click'
		
		pos=[0]*6
		
		pos[0]=1+self.ventana.WKColumnComb.currentIndex()
		pos[1]=1+self.ventana.WKRowComb.currentIndex()
		pos[2]=1+self.ventana.WRColumnComb.currentIndex()
		pos[3]=1+self.ventana.WRRowComb.currentIndex()
		pos[4]=1+self.ventana.BKColumnComb.currentIndex()
		pos[5]=1+self.ventana.BKRowComb.currentIndex()
	
		query = chess.Play(pos,10)
		
		print 'The entered play is:', query.data
		
		print 'Getting answer, this may take a while...'
		
		results = self.chessCBR.solveQuery(query, False)

		print "RESULTS:", results
		
		self.ventana.resultLine.setText(results)

	def setCombos(self):
		
		for v in chess.COLNUMBERS.iterkeys():
			self.ventana.WKColumnComb.addItem(v)
			self.ventana.BKColumnComb.addItem(v)
			self.ventana.WRColumnComb.addItem(v)
			
			
		for v in chess.COLNAMES.iterkeys():
			self.ventana.WKRowComb.addItem(str(v))
			self.ventana.BKRowComb.addItem(str(v))
			self.ventana.WRRowComb.addItem(str(v))
		
		


if __name__ == '__main__':
    #main()
    app = QtGui.QApplication(sys.argv)
    t=test()
    sys.exit(t.exec_())
