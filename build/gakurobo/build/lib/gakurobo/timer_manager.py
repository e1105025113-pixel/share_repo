# timer_manager.py

from gakurobo.config import PHASES


class TimerManager:

    def __init__(self, app):

        self.app = app

        self.phase_index = 0
        self.time_left = PHASES[0][1]

        self.running = False

    def update_timer(self):

        minutes = self.time_left // 60
        seconds = self.time_left % 60

        self.app.phase_label.config(
            text=PHASES[self.phase_index][0]
        )

        self.app.timer_label.config(
            text=f"{minutes:02}:{seconds:02}"
        )

        if self.time_left <= 10:
            self.app.timer_label.config(
                fg="red"
            )
        else:
            self.app.timer_label.config(
                fg="white"
            )

    def countdown(self):

        if not self.running:
            return

        if self.time_left > 0:

            self.time_left -= 1

            self.update_timer()

            self.app.root.after(
                1000,
                self.countdown
            )

        else:

            self.running = False

            phase_name = PHASES[self.phase_index][0]

            self.app.score_manager.add_separator(
                phase_name
            )

    def start_timer(self):

        if not self.running:

            self.running = True

            self.countdown()

    def stop_timer(self):

        self.running = False

    def reset_timer(self):

        self.running = False

        self.phase_index = 0

        self.time_left = PHASES[0][1]

        self.update_timer()

    def set_phase(self, index):

        self.running = False

        self.phase_index = index

        self.time_left = PHASES[index][1]

        self.update_timer()
