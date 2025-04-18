

from datetime import datetime
import flet as ft

current_hour = datetime.now().hour
current_time = datetime.now()

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.SYSTEM
    greeting_text = ft.Text('Hello World!')

    History_file = 'history.txt'

    greeting_history = {}

    def load_history():
        try:
            with open(History_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    name = line.strip()
                    if name:
                        greeting_history.append(name)
                history_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
                page.update()
        except FileNotFoundError:
            pass

    def save_history():
        with open(History_file, 'w', encoding='utf-8') as file:
            for name in greeting_history:
                file.write(name+'\n')

    history_text = ft.Text('History of greetings',size = 'bodyMedium')

    def one_button_click(_):
        name = name_input.value.strip()

        if name:
            current_hour = datetime.now().hour  # get latest time
            if 6 <= current_hour < 12:
                greeting_text.value = f'Good morning, {name}'
            elif 12 <= current_hour < 18:
                greeting_text.value = f'Good afternoon, {name}'
            elif 18 <= current_hour <= 23:
                greeting_text.value = f'Good evening, {name}'
            else:
                greeting_text.value = f'Good night, {name}'

            greet_button.text = 'Greet again'
            name_input.value = ''

            current_time = datetime.now().strftime('%c')
            greeting_history[current_time] = name

            history_text.value = 'History of greetings:\n' + '\n'.join(
                f"{time} - {name}" for time, name in greeting_history.items()
            )
        else:
            greeting_text.value = 'Insert name, please'
        page.update()


    name_input = ft.TextField(label = 'Insert name', autofocus = True, on_submit = one_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'History greetings'
        page.update()

    def history_visibility(_):
        history_text.visible = not history_text.visible
        toggle_button.text = "Show history" if not history_text.visible else "Hide history"
        page.update()

    def toggle_theme(_):
        if page.theme_mode ==ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()


    greet_button = ft.ElevatedButton('Greet', on_click = one_button_click)

    clear_button = ft.TextButton('Clear History', on_click = clear_history)

    clear_button2 = ft.IconButton(icon = ft.icons.DELETE,
                                    tooltip='Clear history',
                                    on_click=clear_history)

    theme_button = ft.IconButton(icon = ft.icons.BRIGHTNESS_6,tooltip = 'Change theme', on_click=toggle_theme)

    toggle_button = ft.ElevatedButton("Скрыть историю", on_click=history_visibility)

   #page.add(greeting_text, name_input, greet_button, history_text, clear_button, theme_button)

    page.add(ft.Row([theme_button, clear_button, clear_button2], alignment=ft.MainAxisAlignment.CENTER), 
                                                                greeting_text,
                                                                name_input,
                                                                greet_button,
                                                                toggle_button,
                                                               ft.Column([history_text], alignment=ft.MainAxisAlignment.CENTER))

ft.app(main)