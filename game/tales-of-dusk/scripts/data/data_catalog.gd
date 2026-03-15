class_name DataCatalog
extends RefCounted

const CHAPTER_PATHS := {
	&"chapter_01": "res://data/defs/chapters/chapter_01.tres",
}

const ROOM_PATHS := {
	&"room_01": "res://data/defs/rooms/room_01.tres",
	&"room_02": "res://data/defs/rooms/room_02.tres",
	&"room_boss": "res://data/defs/rooms/room_boss.tres",
}

const UNIT_PATHS := {
	&"guard": "res://data/defs/units/unit_guard.tres",
	&"archer": "res://data/defs/units/unit_archer.tres",
}


static func _load_resource(path: String) -> Resource:
	var res := ResourceLoader.load(path)
	if res == null:
		push_error("DataCatalog failed to load resource: %s" % path)
	return res


static func load_chapter(chapter_id: StringName) -> ChapterDef:
	var path: String = CHAPTER_PATHS.get(chapter_id, "")
	if path.is_empty():
		push_error("DataCatalog unknown chapter_id: %s" % String(chapter_id))
		return null

	return _load_resource(path) as ChapterDef


static func load_room_by_id(room_id: StringName) -> RoomDef:
	var path: String = ROOM_PATHS.get(room_id, "")
	if path.is_empty():
		push_error("DataCatalog unknown room_id: %s" % String(room_id))
		return null

	return _load_resource(path) as RoomDef


static func load_unit_by_id(unit_id: StringName) -> UnitDef:
	var path: String = UNIT_PATHS.get(unit_id, "")
	if path.is_empty():
		push_error("DataCatalog unknown unit_id: %s" % String(unit_id))
		return null

	return _load_resource(path) as UnitDef


static func load_default_units() -> Array[UnitDef]:
	var result: Array[UnitDef] = []

	var guard := load_unit_by_id(&"guard")
	if guard != null:
		result.append(guard)

	var archer := load_unit_by_id(&"archer")
	if archer != null:
		result.append(archer)

	return result


static func get_default_unit_ids() -> Array[StringName]:
	return [
		&"guard",
		&"archer",
	]


static func get_first_room_id_for_chapter(chapter_id: StringName) -> StringName:
	var chapter := load_chapter(chapter_id)
	if chapter == null:
		return &""

	if chapter.rooms.is_empty():
		push_error("DataCatalog chapter has no rooms: %s" % String(chapter_id))
		return &""

	var first_room := chapter.rooms[0]
	if first_room == null:
		push_error("DataCatalog first room is null for chapter: %s" % String(chapter_id))
		return &""

	return first_room.room_id
