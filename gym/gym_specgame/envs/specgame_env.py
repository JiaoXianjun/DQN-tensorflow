import gym
from gym import error, spaces
import numpy as np
import cfg_set

class specgame_env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        #self._action_set = [0, 1]
        #self.action_space = spaces.Discrete(len(self._action_set))
        #self.action_space = [0,1]
        self.action_space = spaces.Discrete(2)
        
        self.lives=10

        self.test_fid = open(cfg_set.test_filename,'rb')
        self.num_consume = 0
        self.num_sample = 0
        self.read_buf = []
        self.lane_traffic = ''
        for i in range(cfg_set.len_lane):
          self.lane_traffic = self.lane_traffic + ' ' # an empty high way at first!
        self.screen = np.zeros((1,cfg_set.len_lane),dtype=np.int8)
        #print '__init__'

    def _step(self, action):
        #print '_step'
        """

        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        if self.num_consume == 0:
          self.read_buf = self.test_fid.read(cfg_set.len_read)
          if len(self.read_buf) < cfg_set.len_read:
            self.test_fid.seek(0)
            self.read_buf = self.test_fid.read(cfg_set.len_read)
        
        channel_current = self.read_buf[self.num_consume]
        self.num_consume = self.num_consume + 1
        if self.num_consume == cfg_set.len_read:
          self.num_consume = 0
        
        self._take_action(action, channel_current)
        return self.lane_traffic, self.reward, self.episode_over, {}

    def _take_action(self, action, channel_current):
        tmp_pad = channel_current
        self.reward = 0
        self.episode_over = False
        if action==1:
          if tmp_pad=='A':
            tmp_pad = 'X'
          else:
            tmp_pad = 'B'
            self.reward = 1
    
        self.lane_traffic = self.lane_traffic[1:cfg_set.len_lane]+tmp_pad
        self.screen[0] = np.array([ord(self.lane_traffic[i]) for i in range(len(self.lane_traffic))],dtype=np.int8)
        
        self.num_sample = self.num_sample + 1
        if self.num_sample == cfg_set.num_sample_per_episode:
          self.num_sample = 0
          self.episode_over = True
          
    def _reset(self):
        print '_reset'
        pass

    def reset(self):
        print 'reset'
        pass

    def _render(self, mode='human', close=False):
        pass

    def _get_reward(self):
        """ Reward is given for XY. """
        if self.status == False:
            return 1
        elif self.status == True:
            return 2
        else:
            return 0
