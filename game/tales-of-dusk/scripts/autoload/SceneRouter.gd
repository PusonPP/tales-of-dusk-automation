extends Node

signal scene_change_started(scene_path: String)
signal scene_change_finished(scene_path: String)

const BOOT_SCENE := "res://scenes/boot/boot.tscn"
const TITLE_SCENE := "res://scenes/title/title.tscn"
const CHAPTER_MAP_SCENE := "res://scenes/chapter_map/chapter_map.tscn"
const ROOM_TEST_SCENE := "res://scenes/rooms/room_test.tscn"

var current_scene_path: String = ""

func go_to_file(scene_path: String) -> void:
	scene_change_started.emit(scene_path)

	var err := get_tree().change_scene_to_file(scene_path)
	if err != OK:
		push_error("Failed to change scene to: %s" % scene_path)
		return

	current_scene_path = scene_path
	scene_change_finished.emit(scene_path)

func go_to_title() -> void:
	go_to_file(TITLE_SCENE)

func go_to_chapter_map() -> void:
	go_to_file(CHAPTER_MAP_SCENE)

func go_to_room_test() -> void:
	go_to_file(ROOM_TEST_SCENE)
