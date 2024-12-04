class Settings:
    """Класс для хранения всех настроек игры "Инопланетное второжение"."""

    def __init__(self) -> None:
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (0, 0, 250)
