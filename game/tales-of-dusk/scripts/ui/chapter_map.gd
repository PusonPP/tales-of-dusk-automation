extends Control

const DEFAULT_CHAPTER_ID: StringName = &"chapter_01"

@onready var btn_enter_room_test: Button = $CenterContainer/VBoxContainer/BtnEnterRoomTest
@onready var btn_back_to_title: Button = $CenterContainer/VBoxContainer/BtnBackToTitle


func _ready() -> void:
	btn_enter_room_test.pressed.connect(_on_enter_room_test_pressed)
	btn_back_to_title.pressed.connect(_on_back_to_title_pressed)


func _on_enter_room_test_pressed() -> void:
	var chapter := DataCatalog.load_chapter(DEFAULT_CHAPTER_ID)
	if chapter == null:
		push_error("ChapterMap failed to load chapter: %s" % String(DEFAULT_CHAPTER_ID))
		return

	var first_room_id := DataCatalog.get_first_room_id_for_chapter(DEFAULT_CHAPTER_ID)
	if first_room_id == &"":
		push_error("ChapterMap failed to resolve first room for chapter: %s" % String(DEFAULT_CHAPTER_ID))
		return

	GameSession.start_chapter(DEFAULT_CHAPTER_ID, chapter.starting_supply)
	GameSession.begin_room(first_room_id, 0)

	EventBus.chapter_selected.emit(DEFAULT_CHAPTER_ID)
	EventBus.room_entered.emit(first_room_id)

	SceneRouter.go_to_room_test()


func _on_back_to_title_pressed() -> void:
	SceneRouter.go_to_title()
