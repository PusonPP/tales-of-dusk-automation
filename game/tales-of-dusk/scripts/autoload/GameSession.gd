extends Node

var current_chapter_id: String = ""
var current_room_id: String = ""
var current_room_state: String = "Preview"

var chapter_supply: int = 0
var core_shards: int = 0

func reset_run() -> void:
	current_chapter_id = ""
	current_room_id = ""
	current_room_state = "Preview"
	chapter_supply = 0

func start_chapter(chapter_id: String, initial_supply: int) -> void:
	current_chapter_id = chapter_id
	current_room_id = ""
	current_room_state = "Preview"
	chapter_supply = initial_supply
