from gym.envs.registration import register

register(
    id='specgame_env-v0',
    entry_point='gym_specgame.envs:specgame_env',
)
register(
    id='specgame_extrahard_env-v0',
    entry_point='gym_specgame.envs:specgame_extrahard_env',
)

