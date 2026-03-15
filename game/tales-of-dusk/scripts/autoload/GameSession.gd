extends Node

const ROOM_STATE_PREVIEW: StringName = &"Preview"
const ROOM_STATE_DEPLOY: StringName = &"Deploy"
const ROOM_STATE_COMBAT: StringName = &"Combat"
const ROOM_STATE_RESULT: StringName = &"Result"

var current_chapter_id: StringName = &""
var current_room_id: StringName = &""
var current_room_state: StringName = ROOM_STATE_PREVIEW

var current_room_index: int = -1

var chapter_supply: int = 0
var core_shards: int = 0

var selected_unit_ids: Array[StringName] = []

var last_room_victory: bool = false
var last_room_reward_supply: int = 0
var last_room_reward_core_shards: int = 0


func _ready() -> void:
	reset_run()


func reset_run() -> void:
	current_chapter_id = &""
	current_room_id = &""
	current_room_state = ROOM_STATE_PREVIEW
	current_room_index = -1

	chapter_supply = 0
	core_shards = 0

	selected_unit_ids.clear()

	last_room_victory = false
	last_room_reward_supply = 0
	last_room_reward_core_shards = 0


func start_chapter(chapter_id: StringName, starting_supply: int) -> void:
	current_chapter_id = chapter_id
	chapter_supply = max(starting_supply, 0)
	core_shards = 0

	current_room_id = &""
	current_room_index = -1
	current_room_state = ROOM_STATE_PREVIEW

	selected_unit_ids.clear()

	last_room_victory = false
	last_room_reward_supply = 0
	last_room_reward_core_shards = 0


func begin_room(room_id: StringName, room_index: int) -> void:
	current_room_id = room_id
	current_room_index = room_index
	current_room_state = ROOM_STATE_PREVIEW

	selected_unit_ids.clear()

	last_room_victory = false
	last_room_reward_supply = 0
	last_room_reward_core_shards = 0


func set_room_state(room_state: StringName) -> void:
	current_room_state = room_state


func set_selected_units(unit_ids: Array[StringName]) -> void:
	selected_unit_ids = unit_ids.duplicate()


func clear_selected_units() -> void:
	selected_unit_ids.clear()


func can_afford(cost: int) -> bool:
	return chapter_supply >= max(cost, 0)


func try_spend_supply(cost: int) -> bool:
	var safe_cost := max(cost, 0)
	if chapter_supply < safe_cost:
		return false

	chapter_supply -= safe_cost
	return true


func refund_supply(amount: int) -> void:
	chapter_supply += max(amount, 0)


func apply_room_result(victory: bool, supply_reward: int, core_shard_reward: int) -> void:
	last_room_victory = victory

	if victory:
		last_room_reward_supply = max(supply_reward, 0)
		last_room_reward_core_shards = max(core_shard_reward, 0)

		chapter_supply += last_room_reward_supply
		core_shards += last_room_reward_core_shards
	else:
		last_room_reward_supply = 0
		last_room_reward_core_shards = 0


func get_selected_unit_count() -> int:
	return selected_unit_ids.size()
