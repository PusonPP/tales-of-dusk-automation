extends Node

func _ready() -> void:
	await get_tree().process_frame
	SceneRouter.go_to_title()
