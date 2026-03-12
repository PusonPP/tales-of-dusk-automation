class_name RoomDef
extends Resource

enum RoomType {
    NORMAL,
    ELITE,
    BOSS,
    EVENT
}

@export_group("Identity")
@export var room_id: StringName
@export var display_name: String
@export var room_type: RoomType = RoomType.NORMAL

@export_group("Narrative")
@export_multiline var preview_text: String = ""

@export_group("Rewards")
@export var supply_reward: int = 0
@export var core_shard_reward: int = 0

@export_group("Combat")
@export var waves: Array[WaveDef] = []