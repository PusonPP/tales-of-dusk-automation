extends Control

const MAX_DEPLOY_UNITS: int = 2

var current_room: RoomDef = null
var available_units: Array[UnitDef] = []
var deploy_selected_ids: Array[StringName] = []

var lbl_room_title: Label
var lbl_room_preview: Label
var lbl_supply: Label
var lbl_reward: Label
var btn_start_deploy: Button

var btn_select_guard: Button
var btn_select_archer: Button
var lbl_deploy_summary: Label
var btn_start_combat: Button

var lbl_combat_summary: Label
var btn_resolve_combat: Button

var lbl_result_summary: Label
var btn_back_to_map: Button
var btn_retry_room: Button

var lbl_room_state: Label


func _ready() -> void:
	_bind_nodes()
	_connect_signals()
	_load_runtime_context()
	_enter_preview()


func _bind_nodes() -> void:
	lbl_room_title = _find_required_label("LblRoomTitle")
	lbl_room_preview = _find_required_label("LblRoomPreview")
	lbl_supply = _find_required_label("LblSupply")
	lbl_reward = _find_required_label("LblReward")
	btn_start_deploy = _find_required_button("BtnStartDeploy")

	btn_select_guard = _find_required_button("BtnSelectGuard")
	btn_select_archer = _find_required_button("BtnSelectArcher")
	lbl_deploy_summary = _find_required_label("LblDeploySummary")
	btn_start_combat = _find_required_button("BtnStartCombat")

	lbl_combat_summary = _find_required_label("LblCombatSummary")
	btn_resolve_combat = _find_required_button("BtnResolveCombat")

	lbl_result_summary = _find_required_label("LblResultSummary")
	btn_back_to_map = _find_required_button("BtnBackToMap")

	btn_retry_room = _find_optional_button("BtnRetryRoom")
	lbl_room_state = _find_optional_label("LblRoomState")


func _connect_signals() -> void:
	btn_start_deploy.pressed.connect(_on_start_deploy_pressed)
	btn_select_guard.pressed.connect(func() -> void: _toggle_unit(&"guard"))
	btn_select_archer.pressed.connect(func() -> void: _toggle_unit(&"archer"))
	btn_start_combat.pressed.connect(_on_start_combat_pressed)
	btn_resolve_combat.pressed.connect(_on_resolve_combat_pressed)
	btn_back_to_map.pressed.connect(_on_back_to_map_pressed)

	if btn_retry_room != null:
		btn_retry_room.pressed.connect(_on_retry_room_pressed)


func _load_runtime_context() -> void:
	current_room = DataCatalog.load_room_by_id(GameSession.current_room_id)
	available_units = DataCatalog.load_default_units()

	if current_room == null:
		push_error("RoomTest failed to load current room: %s" % String(GameSession.current_room_id))
		_show_fatal_error("Failed to load room data.")
		return


func _enter_preview() -> void:
	if current_room == null:
		return

	deploy_selected_ids.clear()
	GameSession.clear_selected_units()
	GameSession.set_room_state(GameSession.ROOM_STATE_PREVIEW)
	_emit_room_state_changed()

	_set_phase_visibility(
		true,   # preview
		false,  # deploy
		false,  # combat
		false   # result
	)

	if lbl_room_state != null:
		lbl_room_state.text = "State: Preview"

	lbl_room_title.text = current_room.display_name
	lbl_room_preview.text = current_room.preview_text
	lbl_supply.text = "Supply: %d" % GameSession.chapter_supply
	lbl_reward.text = "Reward: +%d Supply / +%d Core Shards | Waves: %d" % [
		current_room.supply_reward,
		current_room.core_shard_reward,
		current_room.waves.size(),
	]


func _enter_deploy() -> void:
	if current_room == null:
		return

	deploy_selected_ids.clear()
	GameSession.clear_selected_units()
	GameSession.set_room_state(GameSession.ROOM_STATE_DEPLOY)
	_emit_room_state_changed()

	_set_phase_visibility(
		false,
		true,
		false,
		false
	)

	if lbl_room_state != null:
		lbl_room_state.text = "State: Deploy"

	lbl_supply.text = "Supply: %d" % GameSession.chapter_supply
	lbl_reward.text = "Room Reward on Victory: +%d Supply / +%d Core Shards" % [
		current_room.supply_reward,
		current_room.core_shard_reward,
	]

	_update_deploy_summary()


func _enter_combat() -> void:
	if current_room == null:
		return

	GameSession.set_room_state(GameSession.ROOM_STATE_COMBAT)
	_emit_room_state_changed()

	_set_phase_visibility(
		false,
		false,
		true,
		false
	)

	if lbl_room_state != null:
		lbl_room_state.text = "State: Combat"

	_update_combat_summary()


func _enter_result() -> void:
	GameSession.set_room_state(GameSession.ROOM_STATE_RESULT)
	_emit_room_state_changed()

	_set_phase_visibility(
		false,
		false,
		false,
		true
	)

	if lbl_room_state != null:
		lbl_room_state.text = "State: Result"

	_update_result_summary()

	if btn_retry_room != null:
		btn_retry_room.visible = not GameSession.last_room_victory


func _on_start_deploy_pressed() -> void:
	_enter_deploy()


func _on_start_combat_pressed() -> void:
	if deploy_selected_ids.is_empty():
		lbl_deploy_summary.text = "Select at least one unit before starting combat."
		return

	var total_cost := _compute_selected_cost(deploy_selected_ids)
	if not GameSession.can_afford(total_cost):
		lbl_deploy_summary.text = "Not enough supply. Need %d, have %d." % [
			total_cost,
			GameSession.chapter_supply,
		]
		return

	if not GameSession.try_spend_supply(total_cost):
		lbl_deploy_summary.text = "Failed to spend supply for deployment."
		return

	GameSession.set_selected_units(deploy_selected_ids)
	_enter_combat()


func _on_resolve_combat_pressed() -> void:
	var unit_power := _compute_selected_power(GameSession.selected_unit_ids)
	var room_threat := _compute_room_threat(current_room)
	var victory := unit_power >= room_threat

	GameSession.apply_room_result(
		victory,
		current_room.supply_reward,
		current_room.core_shard_reward
	)

	_enter_result()


func _on_back_to_map_pressed() -> void:
	SceneRouter.go_to_chapter_map()


func _on_retry_room_pressed() -> void:
	if current_room == null:
		return

	GameSession.begin_room(current_room.room_id, GameSession.current_room_index)
	_load_runtime_context()
	_enter_preview()


func _toggle_unit(unit_id: StringName) -> void:
	var unit := DataCatalog.load_unit_by_id(unit_id)
	if unit == null:
		lbl_deploy_summary.text = "Failed to load unit: %s" % String(unit_id)
		return

	if deploy_selected_ids.has(unit_id):
		deploy_selected_ids.erase(unit_id)
		_update_deploy_summary()
		return

	if deploy_selected_ids.size() >= MAX_DEPLOY_UNITS:
		lbl_deploy_summary.text = "You can select at most %d units." % MAX_DEPLOY_UNITS
		return

	var new_total_cost := _compute_selected_cost(deploy_selected_ids) + unit.supply_cost
	if new_total_cost > GameSession.chapter_supply:
		lbl_deploy_summary.text = "Not enough supply for %s. Need %d, have %d." % [
			unit.display_name,
			new_total_cost,
			GameSession.chapter_supply,
		]
		return

	deploy_selected_ids.append(unit_id)
	_update_deploy_summary()


func _update_deploy_summary() -> void:
	var names := _selected_unit_names(deploy_selected_ids)
	var total_cost := _compute_selected_cost(deploy_selected_ids)

	var selected_text := "None"
	if not names.is_empty():
		selected_text = ", ".join(names)

	lbl_deploy_summary.text = "Selected Units: %s\nTotal Cost: %d | Current Supply: %d" % [
		selected_text,
		total_cost,
		GameSession.chapter_supply,
	]


func _update_combat_summary() -> void:
	var names := _selected_unit_names(GameSession.selected_unit_ids)
	var selected_text := "None"
	if not names.is_empty():
		selected_text = ", ".join(names)

	var unit_power := _compute_selected_power(GameSession.selected_unit_ids)
	var room_threat := _compute_room_threat(current_room)

	lbl_supply.text = "Supply: %d" % GameSession.chapter_supply
	lbl_combat_summary.text = "Selected Units: %s\nUnit Power: %d | Room Threat: %d\nPress Resolve Combat to continue." % [
		selected_text,
		unit_power,
		room_threat,
	]


func _update_result_summary() -> void:
	lbl_supply.text = "Supply: %d" % GameSession.chapter_supply

	if GameSession.last_room_victory:
		lbl_result_summary.text = "Victory!\nRewards Gained: +%d Supply / +%d Core Shards\nCurrent Core Shards: %d" % [
			GameSession.last_room_reward_supply,
			GameSession.last_room_reward_core_shards,
			GameSession.core_shards,
		]
	else:
		lbl_result_summary.text = "Defeat.\nNo room rewards granted.\nCurrent Core Shards: %d" % [
			GameSession.core_shards,
		]


func _compute_selected_cost(unit_ids: Array[StringName]) -> int:
	var total := 0
	for unit_id in unit_ids:
		var unit := DataCatalog.load_unit_by_id(unit_id)
		if unit != null:
			total += max(unit.supply_cost, 0)
	return total


func _compute_selected_power(unit_ids: Array[StringName]) -> int:
	var total := 0
	for unit_id in unit_ids:
		var unit := DataCatalog.load_unit_by_id(unit_id)
		if unit != null:
			total += unit.attack_power
			total += int(unit.max_hp / 10)
	return total


func _compute_room_threat(room: RoomDef) -> int:
	if room == null:
		return 9999

	var total := 0
	for wave in room.waves:
		if wave == null:
			continue

		for spawn in wave.spawns:
			if spawn == null:
				continue

			total += max(spawn.count, 0)

			var enemy_id_text := String(spawn.enemy_type_id).to_lower()
			if enemy_id_text.contains("big") or enemy_id_text.contains("boss"):
				total += max(spawn.count, 0)

	if room.room_type == RoomDef.RoomType.BOSS:
		total += 2

	return total


func _selected_unit_names(unit_ids: Array[StringName]) -> Array[String]:
	var names: Array[String] = []
	for unit_id in unit_ids:
		var unit := DataCatalog.load_unit_by_id(unit_id)
		if unit != null:
			names.append(unit.display_name)
	return names


func _set_phase_visibility(
	show_preview: bool,
	show_deploy: bool,
	show_combat: bool,
	show_result: bool
) -> void:
	_set_visible(lbl_room_title, show_preview)
	_set_visible(lbl_room_preview, show_preview)
	_set_visible(lbl_reward, show_preview)
	_set_visible(btn_start_deploy, show_preview)

	_set_visible(btn_select_guard, show_deploy)
	_set_visible(btn_select_archer, show_deploy)
	_set_visible(lbl_deploy_summary, show_deploy)
	_set_visible(btn_start_combat, show_deploy)

	_set_visible(lbl_combat_summary, show_combat)
	_set_visible(btn_resolve_combat, show_combat)

	_set_visible(lbl_result_summary, show_result)
	_set_visible(btn_back_to_map, show_result)

	if btn_retry_room != null:
		_set_visible(btn_retry_room, show_result and not GameSession.last_room_victory)

	# Common labels stay visible across phases.
	_set_visible(lbl_supply, true)


func _show_fatal_error(message: String) -> void:
	if lbl_room_title != null:
		lbl_room_title.text = "Room Load Error"
	if lbl_room_preview != null:
		lbl_room_preview.text = message
	if lbl_supply != null:
		lbl_supply.text = "Supply: %d" % GameSession.chapter_supply
	if lbl_reward != null:
		lbl_reward.text = ""

	_set_phase_visibility(false, false, false, true)

	if lbl_result_summary != null:
		lbl_result_summary.text = message

	if btn_back_to_map != null:
		btn_back_to_map.visible = true

	if btn_retry_room != null:
		btn_retry_room.visible = false


func _emit_room_state_changed() -> void:
	if EventBus != null and EventBus.has_signal("room_state_changed"):
		EventBus.emit_signal("room_state_changed", GameSession.current_room_state)


func _set_visible(node: CanvasItem, visible_value: bool) -> void:
	if node != null:
		node.visible = visible_value


func _find_required_label(node_name: String) -> Label:
	var node := find_child(node_name, true, false)
	if node == null or not (node is Label):
		push_error("RoomTest missing required Label node: %s" % node_name)
		return null
	return node as Label


func _find_required_button(node_name: String) -> Button:
	var node := find_child(node_name, true, false)
	if node == null or not (node is Button):
		push_error("RoomTest missing required Button node: %s" % node_name)
		return null
	return node as Button


func _find_optional_label(node_name: String) -> Label:
	var node := find_child(node_name, true, false)
	if node != null and node is Label:
		return node as Label
	return null


func _find_optional_button(node_name: String) -> Button:
	var node := find_child(node_name, true, false)
	if node != null and node is Button:
		return node as Button
	return null
