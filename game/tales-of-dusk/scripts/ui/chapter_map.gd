extends Control

@onready var btn_enter_room_test: Button = $CenterContainer/VBoxContainer/BtnEnterRoomTest
@onready var btn_back_to_title: Button = $CenterContainer/VBoxContainer/BtnBackToTitle

func _ready() -> void:
	btn_enter_room_test.pressed.connect(_on_enter_room_test_pressed)
	btn_back_to_title.pressed.connect(_on_back_to_title_pressed)

func _on_enter_room_test_pressed() -> void:
	GameSession.current_chapter_id = "chapter_01"
	GameSession.current_room_id = "room_test"
	EventBus.chapter_selected.emit("chapter_01")
	EventBus.room_entered.emit("room_test")
	SceneRouter.go_to_room_test()

func _on_back_to_title_pressed() -> void:
	SceneRouter.go_to_title()
