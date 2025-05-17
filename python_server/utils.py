import platform

def get_active_window():
    try:
        if platform.system() == 'Windows':
            import win32gui
            return win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return "Unknown Window"
    except Exception as e:
        return f"Error: {e}"

def is_distracting(title, keywords):
    return any(keyword.lower() in title.lower() for keyword in keywords)
