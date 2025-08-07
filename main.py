
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import datetime
import csv
import os

class EmployeeTracker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.employee_name = TextInput(hint_text='Employee Name')
        self.salary = TextInput(hint_text='Daily Salary', input_filter='int')
        self.advance = TextInput(hint_text='Advance Taken Today', input_filter='int')
        self.status = Label(text='Mark Present or Absent')

        self.add_widget(self.employee_name)
        self.add_widget(self.salary)
        self.add_widget(self.advance)
        self.add_widget(self.status)

        btn_layout = BoxLayout(size_hint_y=None, height='40dp')
        present_btn = Button(text='Present')
        present_btn.bind(on_release=lambda x: self.mark_attendance('P'))
        absent_btn = Button(text='Absent')
        absent_btn.bind(on_release=lambda x: self.mark_attendance('A'))
        btn_layout.add_widget(present_btn)
        btn_layout.add_widget(absent_btn)

        self.add_widget(btn_layout)
        export_btn = Button(text='Export Monthly Report')
        export_btn.bind(on_release=self.export_data)
        self.add_widget(export_btn)

        self.data = []

    def mark_attendance(self, status):
        today = datetime.now().strftime('%d-%m-%Y')
        record = {
            'Date': today,
            'Name': self.employee_name.text,
            'Status': status,
            'Daily Salary': self.salary.text,
            'Advance': self.advance.text
        }
        self.data.append(record)
        self.status.text = f"Marked {status} for {record['Name']} on {today}"

    def export_data(self, instance):
        filename = f"employee_tracker_{datetime.now().strftime('%m_%Y')}.csv"
        filepath = os.path.join("/mnt/data", filename)
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Date', 'Name', 'Status', 'Daily Salary', 'Advance'])
            writer.writeheader()
            writer.writerows(self.data)
        self.status.text = f"Exported to {filename}"

class EmployeeTrackerApp(App):
    def build(self):
        return EmployeeTracker()

if __name__ == '__main__':
    EmployeeTrackerApp().run()
