#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import random


class SimpleCorridor(MiniGridEnv):
    

    def __init__(self, size=19, agent_pos=None, goal_pos=None, obstacle_type=None):
        self.obstacle_type = obstacle_type
        self._agent_default_pos = agent_pos
        self.goal_type = 0

        super().__init__(grid_size=size, max_steps=100)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)
        
        middle_height = height // 2
        middle_widht = width // 2

        self._agent_default_pos = (middle_height, middle_widht - 1 + random.randint(0, 1))

        # random goal type
        goalType = (self.goal_type + 1) % 4 

        
        self.goal_type = goalType

        if (goalType == 0):
            goal_pos = (4 + random.randint(0, 1), 1)
        elif (goalType == 1):
            goal_pos = (width - 5 + random.randint(0, 1), 1)
        elif (goalType == 2):
            goal_pos = (4 + random.randint(0, 1), height-2)
        elif (goalType == 3):
            goal_pos = (width - 5 + random.randint(0, 1), height-2)
        
        self._goal_default_pos = goal_pos


        # Generate the surrounding walls
        self.grid.horz_wall(3, 0, 4)
        self.grid.horz_wall(3, height - 1, 4)
        

        self.grid.vert_wall(middle_height - 2, 0, middle_height - 2)
        self.grid.vert_wall(middle_height - 2, middle_height + 3, middle_height - 2)

        self.grid.horz_wall(middle_height - 2, middle_height - 2, middle_height - 4)
        self.grid.horz_wall(middle_height - 2, middle_height + 2, middle_height - 4)

        self.grid.vert_wall(middle_height + 2, 0, middle_height - 2)
        self.grid.vert_wall(middle_height + 2, middle_height + 3, middle_height - 2)

        self.grid.horz_wall(middle_height + 3, 0, 3)
        self.grid.horz_wall(middle_height + 3, height - 1, 3)

        self.grid.vert_wall(3, 0, height)
        self.grid.vert_wall(width - 4, 0, height)
        

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
        else:
            self.place_obj(Goal())

        
        self.mission = (
            "Get to the green goal square"
        )

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        
        return obs, reward, done, info

class SimpleCorridor16x16(MiniGridEnv):
    

    def __init__(self, agent_pos=None, goal_pos=None, obstacle_type=None, numObjs=4):
        self.obstacle_type = obstacle_type
        self._agent_default_pos = agent_pos
        self.numObjs = numObjs
        
        super().__init__(grid_size=16, max_steps=100, agent_view_size=7)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)
        

        self._agent_default_pos = (6 + self._rand_int(0, 8), 7 + self._rand_int(0, 2))

        # random goal type
        goalType = self._rand_int(1, 4)
        
        self.goal_type = goalType

        if (goalType == 1):
            goal_pos = (1,7 + self._rand_int(0, 2))
        elif (goalType == 2):
            goal_pos = (13 + self._rand_int(0, 2), 1 )
        elif (goalType == 3):
            goal_pos = (13 + self._rand_int(0, 2),14)

        self._goal_default_pos = goal_pos

        self._goal_default_pos = goal_pos
        
        # Generate the surrounding walls
        

        self.grid.horz_wall(0, 6, 12)
        self.grid.horz_wall(0, 9, 12)
        
        self.grid.vert_wall(0, 6, 3)

        self.grid.vert_wall(12, 0, 7)
        self.grid.vert_wall(12, 9, 6)

        self.grid.horz_wall(12, 0, 3)
        self.grid.horz_wall(12, 15, 3)
        self.grid.vert_wall(15, 0, 16)
        

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
        else:
            self.place_obj(Goal())

        
        self.mission = (
            "Get to the green goal square"
        )

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        
        return obs, reward, done, info

class SimpleCorridor18x18(MiniGridEnv):
    

    def __init__(self, agent_pos=None, goal_pos=None, obstacle_type=None, numObjs=4):
        self.obstacle_type = obstacle_type
        self._agent_default_pos = agent_pos
        self.numObjs = numObjs
        self.goal_type = 0
        
        super().__init__(grid_size=18, max_steps=100, agent_view_size=7)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)
        
        agent_pos = (6 + random.randint(0, 7), 8 + random.randint(0, 2))
        
        

        # random goal type
        goalType = (self.goal_type + 1) % 3 

        
        self.goal_type = goalType

        if (goalType == 0):
            goal_pos = (1, 8 + self._rand_int(0, 2))
        elif (goalType == 1):
            goal_pos = (13 + self._rand_int(0, 2), 1 )
        elif (goalType == 2):
            goal_pos = (13 + self._rand_int(0, 2),16)


        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        
        # Generate the surrounding walls
        

        self.grid.horz_wall(0, 7, 12)
        self.grid.horz_wall(0, 10, 12)
        
        self.grid.vert_wall(0, 7, 3)

        self.grid.vert_wall(12, 0, 8)
        self.grid.vert_wall(12, 10, 8)

        self.grid.horz_wall(12, 0, 3)
        self.grid.horz_wall(12, 17, 3)
        self.grid.vert_wall(15, 0, 18)
        

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
        else:
            self.place_obj(Goal())

        
        self.mission = (
            "Get to the green goal square"
        )

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        
        return obs, reward, done, info

class SimpleCorridor23x23(SimpleCorridor):
    def __init__(self, **kwargs):
        super().__init__(size=23, **kwargs)

class LineCorridor(MiniGridEnv):
    

    def __init__(self, size=22, agent_pos=None, goal_pos=None, obstacle_type=None):
        self.obstacle_type = obstacle_type
        self._agent_default_pos = agent_pos
        self.goal_type = 0

        super().__init__(grid_size=size, max_steps=100)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)
        
        middle_height = height // 2
        middle_widht = width // 2

        self._agent_default_pos = (middle_height, middle_widht - 1 + random.randint(0, 1))

        # random goal type
        goalType = (self.goal_type + 1) % 2 
        self.goal_type = goalType

        if (goalType == 0):
            goal_pos = (1, middle_height - 1 + random.randint(0, 2))
        elif (goalType == 1):
            goal_pos = (width - 2, middle_height - 1 + random.randint(0, 2))

        
        self._goal_default_pos = goal_pos

        # Generate the surrounding walls
        self.grid.horz_wall(0, middle_height - 2, width)
        self.grid.horz_wall(0, middle_height + 2, width)
        self.grid.vert_wall(0, middle_height - 2, 4)
        self.grid.vert_wall(height - 1, middle_height - 2, 4)


        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
        else:
            self.place_obj(Goal())

        
        self.mission = (
            "Get to the green goal square"
        )

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        
        return obs, reward, done, info

class LineCorridor19x19(LineCorridor):
    def __init__(self, **kwargs):
        super().__init__(size=19, **kwargs)

class LineCorridor25x25(LineCorridor):
    def __init__(self, **kwargs):
        super().__init__(size=25, **kwargs)

class LineCorridor28x28(LineCorridor):
    def __init__(self, **kwargs):
        super().__init__(size=28, **kwargs)

class OneLineCorridor(MiniGridEnv):
    

    def __init__(self, size=22, agent_pos=None, goal_pos=None, obstacle_type=None):
        self.obstacle_type = obstacle_type
        self._agent_default_pos = agent_pos
        self.goal_type = 0

        super().__init__(grid_size=size, max_steps=100)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)
        
        middle_height = height // 2
        middle_widht = width // 2

        self._agent_default_pos = (middle_height, middle_widht)

        # random goal type
        goalType = (self.goal_type + 1) % 2 
        self.goal_type = goalType

        if (goalType == 0):
            goal_pos = (1, middle_height)
        elif (goalType == 1):
            goal_pos = (width - 2, middle_height)

        
        self._goal_default_pos = goal_pos

        # Generate the surrounding walls
        self.grid.horz_wall(0, middle_height - 1, width)
        self.grid.horz_wall(0, middle_height + 1, width)
        self.grid.vert_wall(0, middle_height - 1, 3)
        self.grid.vert_wall(height - 1, middle_height - 1, 3)


        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
        else:
            self.place_obj(Goal())

        
        self.mission = (
            "Get to the green goal square"
        )

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        
        return obs, reward, done, info

class OneLineCorridor25x25(OneLineCorridor):
    def __init__(self, **kwargs):
        super().__init__(size=25, **kwargs)


register(
    id='MiniGrid-Customs-SimpleCorridor-v0',
    entry_point='gym_minigrid.envs:SimpleCorridor'
)

register(
    id='MiniGrid-Customs-SimpleCorridor16x16-v0',
    entry_point='gym_minigrid.envs:SimpleCorridor16x16'
)

register(
    id='MiniGrid-Customs-SimpleCorridor18x18-v0',
    entry_point='gym_minigrid.envs:SimpleCorridor18x18'
)

register(
    id='MiniGrid-Customs-LineCorridor-v0',
    entry_point='gym_minigrid.envs:LineCorridor'
)

register(
    id='MiniGrid-Customs-LineCorridor19x19-v0',
    entry_point='gym_minigrid.envs:LineCorridor19x19'
)

register(
    id='MiniGrid-Customs-LineCorridor25x25-v0',
    entry_point='gym_minigrid.envs:LineCorridor25x25'
)

register(
    id='MiniGrid-Customs-LineCorridor28x28-v0',
    entry_point='gym_minigrid.envs:LineCorridor28x28'
)

register(
    id='MiniGrid-Customs-OneLineCorridor-v0',
    entry_point='gym_minigrid.envs:OneLineCorridor'
)

register(
    id='MiniGrid-Customs-OneLineCorridor25x25-v0',
    entry_point='gym_minigrid.envs:OneLineCorridor25x25'
)
