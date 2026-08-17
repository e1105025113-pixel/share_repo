# score_manager.py

class ScoreManager:

    def __init__(self, app):
        self.app = app

        self.score_a = 0.0
        self.score_b = 0.0

    def update_score(self):
        if self.score_a.is_integer():
            text_a = str(int(self.score_a))
        else:
            text_a = str(self.score_a)

        if self.score_b.is_integer():
            text_b = str(int(self.score_b))
        else:
            text_b = str(self.score_b)

        self.app.label_a.config(text=text_a)
        self.app.label_b.config(text=text_b)

    def add_a(self, point):
        phase_index = self.app.timer_manager.phase_index

        # セッティング・ブレイク中は得点不可
        if phase_index in (0, 2):
            return

        # 自律ラウンドは1.5倍
        if phase_index == 1:
            point = float(point * 1.5)

        self.score_a += point
        self.update_score()

        if self.app.timer_manager.running:
            self.add_score_log(
                self.app.team_a_name.get(),
                point
            )

    def sub_a(self, point):
        phase_index = self.app.timer_manager.phase_index

        if phase_index in (0, 2):
            return


        self.score_a -= point
        self.update_score()

        self.add_score_log(
            self.app.team_a_name.get(),
            -point
        )

    def add_b(self, point):
        phase_index = self.app.timer_manager.phase_index

        if phase_index in (0, 2):
            return

        if phase_index == 1:
            point = float(point * 1.5)

        self.score_b += point
        self.update_score()

        if self.app.timer_manager.running:
            self.add_score_log(
                self.app.team_b_name.get(),
                point
            )

    def sub_b(self, point):
        phase_index = self.app.timer_manager.phase_index

        if phase_index in (0, 2):
            return


        self.score_b -= point
        self.update_score()

        self.add_score_log(
            self.app.team_b_name.get(),
            -point
        )

    def add_score_log(self, team, point):

        if not self.app.timer_manager.running:
            return

        time_left = self.app.timer_manager.time_left

        minutes = time_left // 60
        seconds = time_left % 60

        if team == self.app.team_a_name.get():

            total = self.score_a

            text = (
                f"{minutes:02}:{seconds:02} | "
                f"{point:+g} | 合計 {total:g}"
            )

            self.insert_log(
                self.app.score_log_box_a,
                text
            )

        else:

            total = self.score_b

            text = (
                f"{minutes:02}:{seconds:02} | "
                f"{point:+g} | 合計 {total:g}"
            )

            self.insert_log(
                self.app.score_log_box_b,
                text
            )

    def insert_log(self, box, text):

        box.config(state="normal")
        box.insert("1.0", text + "\n")
        box.config(state="disabled")

    def reset_score(self):

        self.score_a = 0.0
        self.score_b = 0.0

        self.update_score()

        self.app.score_log_box_a.config(state="normal")
        self.app.score_log_box_a.delete("1.0", "end")
        self.app.score_log_box_a.config(state="disabled")

        self.app.score_log_box_b.config(state="normal")
        self.app.score_log_box_b.delete("1.0", "end")
        self.app.score_log_box_b.config(state="disabled")

    def add_separator(self, phase_name):

        self.insert_log(
            self.app.score_log_box_a,
            "━━━━━━━━━━━━━━━━"
        )

        self.insert_log(
            self.app.score_log_box_a,
            f" {phase_name} 終了 "
        )

        self.insert_log(
            self.app.score_log_box_a,
            "━━━━━━━━━━━━━━━━"
        )

        self.insert_log(
            self.app.score_log_box_b,
            "━━━━━━━━━━━━━━━━"
        )

        self.insert_log(
            self.app.score_log_box_b,
            f" {phase_name} 終了 "
        )

        self.insert_log(
            self.app.score_log_box_b,
            "━━━━━━━━━━━━━━━━"
        )
