# keyboard_manager.py


class KeyboardManager:

    def __init__(self, app):

        self.app = app

        self.pressed_keys = set()

    def key_down(self, event):

        key = event.keysym.lower()

        # 長押しによる連続入力防止
        if key in self.pressed_keys:
            return

        self.pressed_keys.add(key)

        # 試合停止中のみチーム選択可能
        if not self.app.timer_manager.running:

            if key == "1":
                self.app.team_a_name.set("Aチーム")

            elif key == "2":
                self.app.team_a_name.set("Bチーム")

            elif key == "3":
                self.app.team_a_name.set("Cチーム")

            elif key == "4":
                self.app.team_a_name.set("Dチーム")

            elif key == "5":
                self.app.team_b_name.set("Aチーム")

            elif key == "6":
                self.app.team_b_name.set("Bチーム")

            elif key == "7":
                self.app.team_b_name.set("Cチーム")

            elif key == "8":
                self.app.team_b_name.set("Dチーム")

        # Aチーム加点
        if key == "q":
            self.app.score_manager.add_a(1)

        elif key == "w":
            self.app.score_manager.add_a(2)

        elif key == "e":
            self.app.score_manager.add_a(7)

        # Aチーム減点
        elif key == "a":
            self.app.score_manager.sub_a(1)

        elif key == "s":
            self.app.score_manager.sub_a(2)

        elif key == "d":
            self.app.score_manager.sub_a(7)

        # Bチーム加点
        elif key == "i":
            self.app.score_manager.add_b(1)

        elif key == "o":
            self.app.score_manager.add_b(2)

        elif key == "p":
            self.app.score_manager.add_b(7)

        # Bチーム減点
        elif key == "k":
            self.app.score_manager.sub_b(1)

        elif key == "l":
            self.app.score_manager.sub_b(2)

        elif key == "semicolon":
            self.app.score_manager.sub_b(7)

        # スペース：タイマー開始・停止
        elif key == "space":

            if self.app.timer_manager.running:
                self.app.timer_manager.stop_timer()

            else:
                self.app.timer_manager.start_timer()

        # R：タイマーリセット
        elif key == "r":
            self.app.timer_manager.reset_timer()

        # T：得点リセット
        elif key == "t":
            self.app.score_manager.reset_score()

        # フェーズ変更
        if not self.app.timer_manager.running:

            if key == "z":
                self.app.timer_manager.set_phase(0)

            elif key == "x":
                self.app.timer_manager.set_phase(1)

            elif key == "c":
                self.app.timer_manager.set_phase(2)

            elif key == "v":
                self.app.timer_manager.set_phase(3)

    def key_up(self, event):

        key = event.keysym.lower()

        self.pressed_keys.discard(key)
