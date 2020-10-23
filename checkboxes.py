from main import App

class Checkboxes(App):
    def checkboxklass_choose(self):
        if self.ui.checkboxklass_common.isChecked():
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(True)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(True)
        else:
            self.ui.checkboxott_common.setChecked(False)
            self.ui.checkboxott_common.setDisabled(False)
            self.ui.checkboxinterop_common.setChecked(False)
            self.ui.checkboxinterop_common.setDisabled(False)
            exm=self.ui.checkboxinterop_common
            exm.setDisabled()