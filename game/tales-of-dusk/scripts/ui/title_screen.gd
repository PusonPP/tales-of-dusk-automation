extends Control

@onready var btn_start: Button = $CenterContainer/VBoxContainer/BtnStart
@onready var btn_continue: Button = $CenterContainer/VBoxContainer/BtnContinue
@onready var btn_settings: Button = $CenterContainer/VBoxContainer/BtnSettings
@onready var btn_quit: Button = $CenterContainer/VBoxContainer/BtnQuit

func _ready() -> void:
	btn_start.pressed.connect(_on_start_pressed)
	btn_continue.pressed.connect(_on_continue_pressed)
	btn_settings.pressed.connect(_on_settings_pressed)
	btn_quit.pressed.connect(_on_quit_pressed)

func _on_start_pressed() -> void:
	EventBus.game_started.emit()
	SceneRouter.go_to_chapter_map()

func _on_continue_pressed() -> void:
	print("Continue is not implemented yet.")

func _on_settings_pressed() -> void:
	print("Settings is not implemented yet.")

func _on_quit_pressed() -> void:
	get_tree().quit()
