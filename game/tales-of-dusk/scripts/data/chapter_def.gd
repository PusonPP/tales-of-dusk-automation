class_name ChapterDef
extends Resource

@export_group("Identity")
@export var chapter_id: StringName
@export var display_name: String

@export_group("Economy")
@export var starting_supply: int = 10

@export_group("Structure")
@export var rooms: Array[RoomDef] = []