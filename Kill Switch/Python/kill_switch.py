import keyboard
import psutil
import os
import tkinter as tk
import getpass
import win32gui
import win32con
import win32process

HOTKEY = "ctrl+alt+k"

PROTECTED_PROCESSES = {
    "system",
    "system idle process",
    "registry",
    "smss.exe",
    "csrss.exe",
    "wininit.exe",
    "winlogon.exe",
    "services.exe",
    "lsass.exe",
    "svchost.exe",
    "fontdrvhost.exe",
    "dwm.exe",
    "explorer.exe",
    "sihost.exe",
    "taskhostw.exe",
    "ctfmon.exe",
    "searchhost.exe",
    "searchindexer.exe",
    "runtimebroker.exe",
    "applicationframehost.exe",
    "startmenuexperiencehost.exe",
    "shellexperiencehost.exe",
    "textinputhost.exe",
    "securityhealthservice.exe",
    "securityhealthsystray.exe",
    "msmpeng.exe",
    "conhost.exe",
    "openconsole.exe",

    # Keep Kill Switch alive
    "python.exe",
    "pythonw.exe",
    "py.exe",
    "cmd.exe",
    "powershell.exe",
    "windowsterminal.exe",
    "kill_switch.exe",
}

def show_popup(title, message, duration_ms=2500):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    width = 640
    height = 300

    x = int((root.winfo_screenwidth() / 2) - (width / 2))
    y = int((root.winfo_screenheight() / 2) - (height / 2))

    root.geometry(f"{width}x{height}+{x}+{y}")
    root.configure(bg="#111111")

    frame = tk.Frame(
        root,
        bg="#111111",
        highlightbackground="#ff3333",
        highlightthickness=4
    )
    frame.pack(fill="both", expand=True, padx=8, pady=8)

    tk.Label(
        frame,
        text=title,
        bg="#111111",
        fg="#ff3333",
        font=("Segoe UI", 22, "bold")
    ).pack(pady=(34, 16))

    tk.Label(
        frame,
        text=message,
        bg="#111111",
        fg="white",
        font=("Segoe UI", 14),
        wraplength=560,
        justify="center"
    ).pack(pady=(4, 20))

    root.after(duration_ms, root.destroy)
    root.mainloop()

def close_file_explorer_windows():
    def enum_handler(hwnd, _):
        try:
            if not win32gui.IsWindowVisible(hwnd):
                return

            class_name = win32gui.GetClassName(hwnd)

            # CabinetWClass = normal File Explorer windows
            # ExploreWClass = older/alternate Explorer windows
            if class_name not in {"CabinetWClass", "ExploreWClass"}:
                return

            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            proc = psutil.Process(pid)

            if proc.name().lower() == "explorer.exe":
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

        except Exception:
            pass

    win32gui.EnumWindows(enum_handler, None)

def should_skip_process(proc, current_pid, current_user):
    try:
        pid = proc.info["pid"]
        name = (proc.info["name"] or "").lower()
        username = proc.info.get("username")

        if pid == current_pid:
            return True

        if name in PROTECTED_PROCESSES:
            return True

        if not username:
            return True

        if current_user.lower() not in username.lower():
            return True

        return False

    except Exception:
        return True

def hard_force_stop_user_apps():
    current_pid = os.getpid()
    current_user = getpass.getuser()

    processes_to_kill = []

    for proc in psutil.process_iter(["pid", "name", "username"]):
        try:
            if should_skip_process(proc, current_pid, current_user):
                continue

            processes_to_kill.append(proc)

        except Exception:
            pass

    for proc in processes_to_kill:
        try:
            proc.kill()
        except Exception:
            pass

def kill_switch():
    show_popup(
        "THE KILL SWITCH",
        "This button should only be pressed\n"
        "when all other options are exhausted.\n\n"
        "Your PC is about to be given\n"
        "a fresh new start.",
        3000
    )

    close_file_explorer_windows()
    hard_force_stop_user_apps()

def main():
    keyboard.add_hotkey(HOTKEY, kill_switch)
    keyboard.wait()

if __name__ == "__main__":
    main()