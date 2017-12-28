# before run this
# please sudo pip install -e gym

import gym
import gym_specgame
env=gym.make('specgame_env-v0')
env.reset()
env.render()
