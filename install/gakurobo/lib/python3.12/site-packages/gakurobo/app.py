import tkinter as tk

from gakurobo.config import PHASES
from gakurobo.score_manager import ScoreManager
from gakurobo.timer_manager import TimerManager
from gakurobo.keyboard_manager import KeyboardManager


class ScoreBoardApp:

    def __init__(self):

        self.root = tk.Tk()

        self.root.attributes("-fullscreen", True)

        self.root.bind(
            "<Escape>",
            lambda e: self.root.attributes(
                "-fullscreen",
                False
            )
        )

        self.root.configure(bg="white")
        self.root.title("Score Board")

        # -------------------------
        # チーム名
        # -------------------------

        self.team_a_name = tk.StringVar(
            value="Aチーム"
        )

        self.team_b_name = tk.StringVar(
            value="Bチーム"
        )

        # -------------------------
        # マネージャー
        # -------------------------

        self.score_manager = ScoreManager(self)

        self.timer_manager = TimerManager(self)

        self.keyboard_manager = KeyboardManager(self)

        # -------------------------
        # メイン画面
        # -------------------------

        self.create_main_window()

        # -------------------------
        # 得点履歴画面
        # -------------------------

        self.create_score_log_window()

        # -------------------------
        # キーボード
        # -------------------------

        self.root.bind_all(
            "<KeyPress>",
            self.keyboard_manager.key_down
        )

        self.root.bind_all(
            "<KeyRelease>",
            self.keyboard_manager.key_up
        )

        # -------------------------
        # メモ
        # -------------------------

        self.load_memo()

        self.memo_text.bind(
            "<KeyRelease>",
            self.auto_save
        )

        # -------------------------
        # タイマー初期表示
        # -------------------------

        self.timer_manager.update_timer()

        # -------------------------
        # 終了処理
        # -------------------------

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

        self.score_log.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

    # ==================================================
    # メイン画面
    # ==================================================

    def create_main_window(self):

        self.root.geometry("1200x700")

        # タイマー
        timer_frame = tk.Frame(
            self.root,
            bg="black",
            height=120
        )

        timer_frame.pack(fill="x")

        self.phase_label = tk.Label(
            timer_frame,
            text=PHASES[0][0],
            font=("Arial", 30, "bold"),
            fg="white",
            bg="black"
        )

        self.phase_label.pack()

        self.timer_label = tk.Label(
            timer_frame,
            text="00:30",
            font=("Arial", 60),
            fg="white",
            bg="black"
        )

        self.timer_label.pack(pady=15)

        # メインフレーム
        main_frame = tk.Frame(self.root)

        main_frame.pack(
            fill="both",
            expand=True
        )

        # A側
        left_frame = tk.Frame(
            main_frame,
            bg="#E74C3C"
        )

        left_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        # B側
        right_frame = tk.Frame(
            main_frame,
            bg="#3498DB"
        )

        right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ==================================================
        # Aチーム
        # ==================================================

        frame_a = tk.Frame(
            left_frame,
            bg="black",
            pady=10
        )

        frame_a.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tk.Label(
            frame_a,
            textvariable=self.team_a_name,
            font=("Arial", 32, "bold"),
            fg="white",
            bg="black"
        ).pack(
            padx=10,
            pady=(20, 10)
        )

        tk.Frame(
            frame_a,
            bg="#E74C3C",
            height=20
        ).pack(fill="x")

        self.label_a = tk.Label(
            frame_a,
            text="0",
            font=("Arial", 180),
            fg="white",
            bg="black"
        )

        self.label_a.pack(expand=True)

        # ==================================================
        # Bチーム
        # ==================================================

        frame_b = tk.Frame(
            right_frame,
            bg="black",
            pady=10
        )

        frame_b.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tk.Label(
            frame_b,
            textvariable=self.team_b_name,
            font=("Arial", 32, "bold"),
            fg="white",
            bg="black"
        ).pack(
            padx=10,
            pady=(20, 10)
        )

        tk.Frame(
            frame_b,
            bg="#3498DB",
            height=20
        ).pack(fill="x")

        self.label_b = tk.Label(
            frame_b,
            text="0",
            font=("Arial", 180),
            fg="white",
            bg="black"
        )

        self.label_b.pack(expand=True)

    # ==================================================
    # 得点履歴画面
    # ==================================================

    def create_score_log_window(self):

        self.score_log = tk.Toplevel(self.root)

        self.score_log.title("得点履歴")

        self.score_log.attributes(
            "-fullscreen",
            True
        )

        self.score_log.bind(
            "<Escape>",
            lambda e: self.score_log.attributes(
                "-fullscreen",
                False
            )
        )

        self.score_log.configure(
            bg="black"
        )

        tk.Label(
            self.score_log,
            text="得点履歴",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="black"
        ).pack(pady=10)

        score_log_area = tk.Frame(
            self.score_log,
            bg="white"
        )

        score_log_area.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # 左：履歴
        log_area = tk.Frame(
            score_log_area,
            bg="white"
        )

        log_area.pack(
            side="left",
            fill="both",
            expand=True
        )

        # 右：メモ
        memo_area = tk.Frame(
            score_log_area,
            bg="white",
            width=700
        )

        memo_area.pack(
            side="right",
            fill="y"
        )

        memo_area.pack_propagate(False)

        # ==================================================
        # Aチーム履歴
        # ==================================================

        score_log_a = tk.Frame(
            log_area,
            bg="white",
            width=300
        )

        score_log_a.pack(
            side="left",
            fill="both",
            expand=True
        )

        score_log_a.pack_propagate(False)

        tk.Label(
            score_log_a,
            textvariable=self.team_a_name,
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack()

        self.score_log_box_a = tk.Text(
            score_log_a,
            font=("Consolas", 14),
            wrap="none",
            state="disabled"
        )

        self.score_log_box_a.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # Bチーム履歴
        # ==================================================

        score_log_b = tk.Frame(
            log_area,
            bg="white",
            width=300
        )

        score_log_b.pack(
            side="right",
            fill="both",
            expand=True
        )

        score_log_b.pack_propagate(False)

        tk.Label(
            score_log_b,
            textvariable=self.team_b_name,
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack()

        self.score_log_box_b = tk.Text(
            score_log_b,
            font=("Consolas", 14),
            wrap="none",
            state="disabled"
        )

        self.score_log_box_b.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # メモ
        # ==================================================

        tk.Label(
            memo_area,
            text="メモ",
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack()

        self.memo_text = tk.Text(
            memo_area,
            font=("Meiryo", 14),
            wrap="word",
            width=40
        )

        self.memo_text.pack(
            fill="both",
            expand=True
        )

    # ==================================================
    # メモ
    # ==================================================

    def save_memo(self):

        with open(
            "memo.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                self.memo_text.get(
                    "1.0",
                    tk.END
                )
            )

    def load_memo(self):

        try:

            with open(
                "memo.txt",
                "r",
                encoding="utf-8"
            ) as f:

                self.memo_text.insert(
                    "1.0",
                    f.read()
                )

        except FileNotFoundError:

            pass

    def auto_save(self, event=None):

        self.save_memo()

    # ==================================================
    # 終了
    # ==================================================

    def on_close(self):

        self.save_memo()

        self.root.destroy()

    # ==================================================
    # 起動
    # ==================================================

    def run(self):

        self.root.mainloop()
def main():
    app = ScoreBoardApp()
    app.run()


if __name__ == "__main__":
    main()
